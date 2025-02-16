import streamlit as st
import pandas as pd
from st_circular_progress import CircularProgress
from backend.basic_checker import get_personal_info
from backend.constants import (
    EXPERIENCE_COL,
    EXPERIENCE_COL_KEY,
    EDUCATION_COL,
    EDUCATION_COL_KEYS,
    ACHIEVEMENTS_COL,
    ACHIEVEMENTS_COL_KEY,
    CERTIFICATION_COL,
    CERTIFICATION_COL_KEY
)


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

def show_table(columns, data):
    df = pd.DataFrame(data ,columns = columns)
    df.reset_index(drop = True, inplace=True)
    st.table(df)

def run(key):
    if st.session_state.get("personal_info"):
        return st.session_state["personal_info"][key]
    with st.spinner("Fetching Details..."):
        st.session_state["personal_info"] = get_personal_info(st.session_state["current_candidate"].resume_content)
    return st.session_state["personal_info"][key]


@st.dialog("Personal Information", width = "large")
def show_modal(key, columns, columns_key):
    data = run(key)
    if(key == "certification"):
        final_data = [[val] for val in data]
    else:
        final_data = [[row.get(key) for key in columns_key] for row in data]
    show_table(columns, final_data)

col1, col2, col3, col4, col5 = st.columns(5)


# Buttons inside columns
with col1:
    if st.button("💼 Experience"):
        show_modal("company_wise_experience", EXPERIENCE_COL, EXPERIENCE_COL_KEY)

with col2:
    if st.button("🎓 Education"):
        show_modal("education", EDUCATION_COL, EDUCATION_COL_KEYS)

with col3:
    if st.button("🎖️ Achievements"):
        show_modal("achievements", ACHIEVEMENTS_COL, ACHIEVEMENTS_COL_KEY)
        
with col4:
    if st.button("📜 Certificates"):
        show_modal("certification", CERTIFICATION_COL, CERTIFICATION_COL_KEY)

with col5:
    if st.button("📞 Contact"):
        cols = ["Category", "Value"]
        cols_key = ["category", "value"]
        show_modal("personal_information", cols, cols_key)
        
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