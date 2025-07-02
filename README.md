# HealthGuard-API

Study project in Django for a simple Healthcare Compliance Dashboard

## User Endpoints
    - POST /api/register/ - Register a new user
    - POST /api/login/ - User login
    - GET /api/users/ - List users (admin only)

## Compliance Requirement Endpoints
    - GET /api/compliance/ - List compliance requirements for the authenticated user
    - POST /api/compliance/ - Create a new compliance requirement
    - GET /api/compliance/{id}/ - Retrieve a specific compliance requirement
    - PUT /api/compliance/{id}/ - Update a compliance requirement
    - DELETE /api/compliance/{id}/ - Delete a compliance requirement

## Document Endpoints
    - POST /api/documents/ - Upload a document for a compliance requirement
    - GET /api/documents/{id}/ - Retrieve document details
    - DELETE /api/documents/{id}/ - Delete a document

## Notification Endpoints
    - GET /api/notifications/ - List notifications for the authenticated user
    - POST /api/notifications/ - Create a new notification
    - PUT /api/notifications/{id}/ - Mark a notification as read
