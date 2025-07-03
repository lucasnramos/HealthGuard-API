from rest_framework import routers
from .views import ComplianceRequirementViewSet, DocumentViewSet, NotificationViewSet

router = routers.DefaultRouter()
router.register(r'compliance', ComplianceRequirementViewSet, basename='compliance')
router.register(r'documents', DocumentViewSet, basename='documents')
router.register(r'notifications', NotificationViewSet, basename='notifications')

urlpatterns = router.urls
