
from django.urls import path
from .views import trigger_report_view, check_task_status_view

urlpatterns = [
    path('generate/', trigger_report_view, name='generate_report'),
    path('status/<int:report_id>/', check_task_status_view, name='check_status'),
]