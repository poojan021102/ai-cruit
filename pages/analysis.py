import streamlit as st
import pandas as pd
from st_circular_progress import CircularProgress

st.markdown(
    """
<style>
    [data-testid="stSidebar"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

if st.button("⬅️ Back"):
    st.switch_page("app.py")

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Name", st.session_state["current_candidate"].name,border=True)
b.metric("Experience", st.session_state["current_candidate"].experience,border=True)

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

col1, col2, col3, col4, col5 = st.columns(5)

# Buttons inside columns
with col1:
    if st.button("💼 Experience"):
        vote("A")

with col2:
    if st.button("🎓 Education"):
        vote("B")

with col3:
    if st.button("🎖️ Achievements"):
        vote("C")
        
with col4:
    if st.button("📜 Certificates"):
        vote("D")

with col5:
    if st.button("📞 Contact"):
        vote("E")
        
my_circular_progress = CircularProgress(
    label="Matching Score",
    value=st.session_state["current_candidate"].matching_score,
    key="my_circular_progress",
    color="green",
)

my_circular_progress.st_circular_progress()
st.title("Skills")

questions = [
    "What is your name?",
    "What is your experience?",
    "What skills do you have?",
    "Why do you want this job?",
    "What is the difference between @staticmethod, @classmethod, and instance methods?"
]

@st.dialog("Questions")
def skill_modal(skill):
    df = pd.DataFrame({"Que No.": range(1, len(questions) + 1), "Questions": questions})
    df.set_index("Que No.", inplace=True)
    st.table(df)
    

skills = st.session_state["current_candidate"].skills

# Initialize session state to track clicks
if "selected_skill" not in st.session_state:
    st.session_state.selected_skill = None

# Determine number of columns dynamically (max 4 per row for better UI)
num_cols = min(len(skills), 4)  # Adjust the max number of columns if needed
cols = st.columns(num_cols)

# Loop through skills and create buttons dynamically
for i, skill in enumerate(skills):
    with cols[i % num_cols]:  # Distribute buttons across columns
        if st.button(skill):
            skill_modal(skill)

st.title("Summary")
for point in st.session_state["current_candidate"].summary:
    st.write(point)