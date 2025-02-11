import streamlit as st
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

a.metric("Name", "John Doe",border=True)
b.metric("Experience", "1+ year",border=True)

import streamlit as st

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
    value=70,
    key="my_circular_progress",
    color="green",
)

my_circular_progress.st_circular_progress()
st.title("Skills")

@st.dialog("Questions")
def skill_modal(skill):
    st.write(f"Hiii this is {skill}")

# Skill List
skills = ["Python", "Java", "C++", "C", "JavaScript", "HTML", "CSS", "SQL", "Swift", "Go"]

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

# Display selected skill
if st.session_state.selected_skill:
    st.write(f"✅ You selected: **{st.session_state.selected_skill}**")
