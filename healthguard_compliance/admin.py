from django.contrib import admin
from .models import ComplianceRequirement, Document, Notification

# Register your models here.
admin.site.register(ComplianceRequirement)
admin.site.register(Document)
admin.site.register(Notification)
