import streamlit as st

# Function to calculate CGPA
def calculate_cgpa(gpas):
    if not gpas:
        return 0.0
    total_gpa = sum(gpas)
    return total_gpa / len(gpas)
# Function to calculate average marks 
def calculate_average(marks):
    if not marks:
        return 0.0
    total_marks = sum(marks)
    return total_marks / len(marks)

# Function to calculate Maths cutoff
def calculate_cutoff(maths, physics, chemistry):
    return (maths ) + (physics / 2) + (chemistry / 2)

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title="CGPA, Marks Average, and Engineering Cutoff Calculator", page_icon="🎓")

    # Custom Styling
    st.markdown(
        """
        <style>
        .stApp { background-color: lavender; }
        .stMarkdown, .stButton, .stNumberInput, h1, h2, h3, h4, h5, h6, p, label, .title { color: black !important; }
        div[data-baseweb="input"] > input { color: black !important; }
        .stButton > button { 
            color: black !important; 
            background-color: white !important; 
            border: 1px solid black !important; 
            transition: all 0.3s ease; 
        }
        .stButton > button:hover { 
            background-color: #4CAF50 !important; 
            color: white !important; 
            border: 1px solid #4CAF50 !important; 
        }
        .low-cgpa { color: red !important; font-weight: bold; }
        .good-cgpa { color: green !important; font-weight: bold; }
        .low-average { color: red !important; font-weight: bold; }
        .good-average { color: green !important; font-weight: bold; }
        .low-result { color: red !important; font-weight: bold; }
        .high-result{color: green !important; font-weight: bold;}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title
    st.markdown("<h1 class='title'>CGPA, Marks Average, and Engineering Cutoff Calculator</h1>", unsafe_allow_html=True)

    # CGPA Calculation Section
    st.subheader("Calculate CGPA")
    semester_count = st.number_input("Enter the number of semesters completed", min_value=1, step=1)

    gpas = []
    for i in range(int(semester_count)):
        gpa = st.number_input(f"Enter GPA for Semester {i+1}", min_value=0.0, max_value=10.0, step=0.01)
        gpas.append(gpa)

    if st.button("Calculate CGPA"):
        cgpa = calculate_cgpa(gpas)
        if cgpa < 8.0:
            st.markdown(f"<p class='low-cgpa'>Your CGPA is {cgpa:.2f}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p class='good-cgpa'>Your CGPA is {cgpa:.2f}</p>", unsafe_allow_html=True)

    # Average Marks Calculation Section
    st.subheader("Calculate Average Marks")
    subject_count = st.number_input("Enter the number of subjects", min_value=1, step=1)

    marks = []
    for i in range(int(subject_count)):
        mark = st.number_input(f"Enter marks for Subject {i+1}", min_value=0.0, max_value=100.0, step=0.01)
        marks.append(mark)

    if st.button("Calculate Average Marks"):
        average_marks = calculate_average(marks)
        if average_marks > 80:
            st.markdown(f"<p class='good-average'>Your Average Marks are: {average_marks:.2f}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p class='low-average'>Your Average Marks are: {average_marks:.2f}</p>", unsafe_allow_html=True)

    # Maths Cutoff Calculation Section
    st.subheader("Calculate Engineering Cutoff")
    maths_marks = st.number_input("Enter your Maths marks", min_value=0.0, max_value=100.0, step=0.01)
    physics_marks = st.number_input("Enter your Physics marks", min_value=0.0, max_value=100.0, step=0.01)
    chemistry_marks = st.number_input("Enter your Chemistry marks", min_value=0.0, max_value=100.0, step=0.01)

    if st.button("Calculate Cutoff"):
        cutoff = calculate_cutoff(maths_marks, physics_marks, chemistry_marks)
        if cutoff>180:
            st.markdown(f"<p class='high-result'>Your Maths Cutoff is: {cutoff:.2f}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p class='low-result'>Your Maths Cutoff is: {cutoff:.2f}</p>", unsafe_allow_html=True)
# Run the app
if __name__ == "__main__":
    main()
