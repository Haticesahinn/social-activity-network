from rest_framework import serializers
from .models import Comment


class CommentReadSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)
    activity_title = serializers.CharField(source='activity.title', read_only=True)
    activity_owner_username = serializers.CharField(source='activity.owner.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'owner', 'owner_username', 'activity', 'activity_title', 'activity_owner_username', 'comment', 'created_at', 'last_modified_at', 'is_public')
        read_only_fields = ('created_at', 'last_modified_at')


class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'owner', 'activity', 'comment', 'is_public', 'created_at')
        read_only_fields = ('owner', 'created_at', 'last_modified_at')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.is_public = validated_data.get('is_public', instance.is_public)
        instance.save()
        return instance