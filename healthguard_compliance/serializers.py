from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ComplianceRequirement, Document, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ComplianceRequirementSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ComplianceRequirement
        fields = ['id', 'user', 'description', 'due_date', 'status', 'created_at', 'updated_at']

class DocumentSerializer(serializers.ModelSerializer):
    requirement = ComplianceRequirementSerializer(read_only=True)

    class Meta:
        model = Document
        fields = ['id', 'requirement', 'file_path', 'status', 'created_at', 'updated_at']

class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'is_read', 'created_at']
