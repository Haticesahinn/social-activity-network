import {useEffect, useState} from "react";
import {toast} from "react-toastify";
import {Modal, Post, LoadingPost, LoadingForm, FormCreatePost} from "../..";
import InfiniteScroll from "react-infinite-scroll-component";

const Center = ({activities, loading, token, autoFetch, setOneState, dark, user, getAllActivities, setActivities, getNewActivities, error, isQrCode,}) => {

    const [attachment, setAttachment] = useState("");
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [totalPlayerCount, setTotalPlayerCount] = useState();
    const [startDate, setStartDate] = useState();
    const [endDate, setEndDate] = useState();
    const [address, setAddress] = useState({
        address_line1: "",
        city: "",
        postal_code:"",
        country: "",
    });
    const [category, setCategory] = useState("");
    const [price, setPrice] = useState();
    const [openModal, setOpenModal] = useState(false);
    const [loadingCreateNewActivity, setLoadingCreateNewActivity] = useState(false);

    // Modal
    useEffect(() => {
        setOneState("openModal", openModal);
    }, [openModal]);

    // get activities
    useEffect(() => {
        if (token) {
            getAllActivities();
        }
    }, [token]);

    const createNewActivity = async (formData) => {
        setLoadingCreateNewActivity(true);
        if (!title && !description) {
            toast.error("Error. You must type something...");
            return;
        }
        try {
            // let image = null;
            // if (formData) {
            //     const {data} = await autoFetch.post(
            //         `/activities/upload-image`,
            //         formData
            //     );
            //     image = {url: data.url, public_id: data.public_id};
            // }

            const {data} = await autoFetch.post(`/activities/`, {
                title: title,
                description: description,
                address: address,
                category: category,
                activity_price: price,
                start_date: startDate,
                end_date: endDate,
                total_player_count: totalPlayerCount,
                image: formData ? formData : null,
            });
            setActivities([data, ...activities]);
        } catch (error) {
            toast.error("Error...");
        }
        setLoadingCreateNewActivity(false);
    };
    const content = () => {
        if (loading) {
            return (
                <div>
                    <LoadingPost />
                </div>
            );
        }
        if (error) {
            return (
                <div
                    className={`bg-white ${
                        !dark && "shadow-post"
                    } dark:bg-[#242526] rounded-lg w-full text-center text-xl font-bold py-10 `}>
                    <div>No activity found... Try again!</div>
                </div>
            );
        }
        if (activities?.length === 0) {
            return (
                <div className='w-full text-center text-xl font-semibold pt-[20vh] flex-col '>
                    <div>
                        You don't activity anything and don't follow anyone.
                        <br />
                        Let's do something! :3
                    </div>
                </div>
            );
        }
        return (
            <InfiniteScroll
                dataLength={activities?.length}
                next={getNewActivities}
                hasMore={true}
                loader={<LoadingPost />}>
                {activities.map((activity) => (
                    <Post
                        key={activity?.id}
                        currentActivity={activity}
                        user_img={activity?.avatar}
                        userId={activity?.userId}
                        className={!dark ? "shadow-post" : ""}
                        userRole={activity?.role}
                    />
                ))}
            </InfiniteScroll>
        );
    };

    const form = () => {
        if (error) {
            return <>{error}</>;
        }
        if (loading) return <LoadingForm />;
        return (
            <FormCreatePost
                setAttachment={setAttachment}
                setOpenModal={setOpenModal}
                title={title}
                description={description}
                totalPlayerCount={totalPlayerCount}
                startDate={startDate}
                endDate={endDate}
                address={address}
                category={category}
                price={price}
                user={user}
            />
        );
    };

    return (
        <div className=''>
            {form()}

            {openModal && !isQrCode && (
                <Modal
                    setOpenModal={setOpenModal}
                    title={title}
                    setTitle={setTitle}
                    description={description}
                    setDescription={setDescription}
                    totalPlayerCount={totalPlayerCount}
                    setTotalPlayerCount={setTotalPlayerCount}
                    startDate={startDate}
                    setStartDate={setStartDate}
                    endDate={endDate}
                    setEndDate={setEndDate}
                    address={address}
                    setAddress={setAddress}
                    category={category}
                    setCategory={setCategory}
                    price={price}
                    setPrice={setPrice}
                    attachment={attachment}
                    setAttachment={setAttachment}
                    createNewActivity={createNewActivity}
                />
            )}
            {loadingCreateNewActivity && <LoadingPost className='mb-4' />}
            {content()}
        </div>
    );
};

export default Center;