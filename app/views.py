from django.http import JsonResponse
from celery.result import AsyncResult
from .models import ReportRecord
from .tasks import process_heavy_data_report

def trigger_report_view(request):
    # 1. Create a placeholder record in the database
    record = ReportRecord.objects.create(
        title="Insurance Policy Data Report",
        status='PENDING'
    )

    # 2. Trigger the background task, passing the database record ID
    task = process_heavy_data_report.delay(record.id)

    # 3. Save the task ID to the model record
    record.task_id = task.id
    record.save()

    return JsonResponse({
        "message": "Report generation started in the background.",
        "report_id": record.id,
        "task_id": task.id
    })

def check_task_status_view(request, report_id):
    try:
        record = ReportRecord.objects.get(id=report_id)
        result = AsyncResult(record.task_id) if record.task_id else None

        return JsonResponse({
            "report_id": record.id,
            "db_status": record.status,
            "celery_status": result.status if result else "NO_TASK",
        })
    except ReportRecord.DoesNotExist:
        return JsonResponse({"error": "Report not found"}, status=404)