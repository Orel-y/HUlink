from rest_framework import serializers
from .models import Petition, Comment, Announcement


class PetitionSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Petition
        fields = '__all__'
        read_only_fields = ['created_by', 'created_by_username', 'created_at', 'updated_at']


class AnnouncementSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Announcement
        fields = '__all__'
        read_only_fields = ['created_by', 'created_by_username', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'user_username', 'created_at']
