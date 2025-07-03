from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import ComplianceRequirement, Document, Notification
from .serializers import (
    ComplianceRequirementSerializer,
    DocumentSerializer,
    NotificationSerializer
)

# Create your views here.

class ComplianceRequirementViewSet(viewsets.ModelViewSet):
    queryset = ComplianceRequirement.objects.all()
    serializer_class = ComplianceRequirementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
