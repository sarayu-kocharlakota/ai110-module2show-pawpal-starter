import streamlit as st
from datetime import datetime
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

st.markdown("Welcome to **PawPal+** — your smart pet care manager!")

st.divider()

st.subheader("Owner & Pet Info")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name=owner_name, email="owner@pawpal.com")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

if "pet" not in st.session_state:
    st.session_state.pet = Pet(
        name=pet_name,
        species=species,
        breed="Unknown",
        age=1,
        owner=st.session_state.owner
    )
    st.session_state.owner.add_pet(st.session_state.pet)

st.divider()
st.markdown("### Add a Task")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    hour = st.number_input("Hour (0-23)", min_value=0, max_value=23, value=8)
with col3:
    priority = st.selectbox("Priority", [1, 2, 3], index=0)

if st.button("Add task"):
    new_task = Task(
        title=task_title,
        task_type=task_title.lower(),
        due_datetime=datetime.now().replace(hour=int(hour), minute=0, second=0),
        priority=int(priority),
        pet=st.session_state.pet
    )
    st.session_state.pet.add_task(new_task)
    st.session_state.scheduler.add_task(new_task)
    st.session_state.tasks.append(new_task)
    st.success(f"Task '{task_title}' added!")

if st.session_state.tasks:
    st.write("Current tasks:")
    for t in st.session_state.tasks:
        st.write(str(t))
else:
    st.info("No tasks yet. Add one above.")

st.divider()
st.subheader("Build Schedule")

if st.button("Generate schedule"):
    todays_tasks = st.session_state.scheduler.sort_by_priority()
    if todays_tasks:
        st.success("Here is today's schedule!")
        for task in todays_tasks:
            st.write(f"🐾 **{task.pet.name}** — {str(task)}")
    else:
        st.warning("No tasks yet. Add some first!")