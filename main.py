from datetime import datetime
from pawpal_system import Task, Pet, Owner, Scheduler

# Setup
owner = Owner(name="Mandy", email="mandy@gmail.com")
buddy = Pet(name="Leo", species="dog", breed="Labrador", age=6, owner=owner)
whiskers = Pet(name="Coco", species="cat", breed="Siamese", age=7, owner=owner)
owner.add_pet(buddy)
owner.add_pet(whiskers)

# Add tasks out of order
task1 = Task(
    title="Breakfast",
    task_type="feeding",
    due_datetime=datetime.now().replace(hour=8, minute=0, second=0),
    priority=2,
    pet=buddy,
    frequency="daily"
)
task2 = Task(
    title="Morning Walk",
    task_type="walk",
    due_datetime=datetime.now().replace(hour=7, minute=0, second=0),
    priority=1,
    pet=buddy
)
task3 = Task(
    title="Medication",
    task_type="medication",
    due_datetime=datetime.now().replace(hour=9, minute=0, second=0),
    priority=1,
    pet=whiskers
)
task4 = Task(
    title="Vet Appointment",
    task_type="appointment",
    due_datetime=datetime.now().replace(hour=7, minute=0, second=0),
    priority=1,
    pet=buddy
)

buddy.add_task(task1)
buddy.add_task(task2)
buddy.add_task(task4)
whiskers.add_task(task3)

scheduler = Scheduler()
scheduler.add_owner(owner)
scheduler.add_task(task1)
scheduler.add_task(task2)
scheduler.add_task(task3)
scheduler.add_task(task4)

# Sort by time
print("=" * 40)
print("📅 SORTED BY TIME")
print("=" * 40)
for task in scheduler.sort_by_time():
    print(f"Pet: {task.pet.name} | {task}")

# Sort by priority
print("\n" + "=" * 40)
print("⭐ SORTED BY PRIORITY")
print("=" * 40)
for task in scheduler.sort_by_priority():
    print(f"Pet: {task.pet.name} | {task}")

# Filter by pet
print("\n" + "=" * 40)
print("🐶 LEO'S TASKS ONLY")
print("=" * 40)
for task in scheduler.filter_by_pet("Leo"):
    print(task)

# Filter by status
print("\n" + "=" * 40)
print("❌ INCOMPLETE TASKS")
print("=" * 40)
for task in scheduler.filter_by_status(complete=False):
    print(task)

# Test recurring task
print("\n" + "=" * 40)
print("🔁 RECURRING TASK TEST")
print("=" * 40)
print(f"Before complete: {task1}")
scheduler.mark_task_complete(task1)
print(f"After complete: {task1}")
print(f"New recurring task added: {scheduler.tasks[-1]}")

# Fresh conflict test
print("\n" + "=" * 40)
print("⚠️ CONFLICT DETECTION")
print("=" * 40)
scheduler2 = Scheduler()
task_a = Task(
    title="Walk",
    task_type="walk",
    due_datetime=datetime.now().replace(hour=7, minute=0, second=0),
    priority=1,
    pet=buddy
)
task_b = Task(
    title="Vet",
    task_type="appointment",
    due_datetime=datetime.now().replace(hour=7, minute=0, second=0),
    priority=2,
    pet=buddy
)
scheduler2.add_task(task_a)
scheduler2.add_task(task_b)
scheduler2.print_conflicts()