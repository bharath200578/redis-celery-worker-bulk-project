import time
from celery import shared_task
from .models import ReportRecord

@shared_task(bind=True)
def process_heavy_data_report(self, report_id):
    try:
        # Fetch the record and update status to processing
        record = ReportRecord.objects.get(id=report_id)
        record.status = 'PROCESSING'
        record.task_id = self.request.id
        record.save()

        # Simulate heavy data workload
        time.sleep(10)

        # Mark success
        record.status = 'SUCCESS'
        record.save()
        
        return {"report_id": report_id, "status": "Completed"}
    
    except Exception as e:
        # Handle failure state gracefully
        record = ReportRecord.objects.get(id=report_id)
        record.status = 'FAILURE'
        record.save()
        raise e