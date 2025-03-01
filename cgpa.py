import streamlit as st

# Function to calculate CGPA
def calculate_cgpa(gpas):
    if not gpas:
        return 0.0
    total_gpa = sum(gpas)
    return total_gpa / len(gpas)

# Main function for the app
def main():
    st.set_page_config(page_title="CGPA Calculator", page_icon="🎓")

    # Authenticate users
    auth_status = st.login("Login with your identity provider")
    
    if auth_status:
        st.success("You are successfully logged in!")
        
        st.markdown(
            """
            <style>
            .stApp {
                background-color: lavender;
            }
            .stMarkdown, .stButton, .stNumberInput, h1, h2, h3, h4, h5, h6, p, label, .title {
                color: black !important;
            }
            .st-bx {
                color: black;
            }
            .st-eb {
                color: black;
            }
            div[data-baseweb="input"] > input {
                color: black !important;
            }
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
            .low-cgpa {
                color: red !important;
                font-weight: bold;
            }
            .good-cgpa {
                color: green !important;
                font-weight: bold;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<h1 class='title'>CGPA Calculator</h1>", unsafe_allow_html=True)

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

    else:
        st.warning("Please log in to use the CGPA calculator.")

if __name__ == "__main__":
    main()
