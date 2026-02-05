import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager_backend.settings")
django.setup()

from tasks.models import Task

print("Attempting to create a task...")
try:
    t = Task.objects.create(title="Test Task")
    print(f"Success! Created task: {t.id}")
except Exception as e:
    print(f"Failed to create task: {e}")
    import traceback
    traceback.print_exc()
