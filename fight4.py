import streamlit as st

st.set_page_config(page_title="Student Result", page_icon="📘")
st.title("📘 Student Result Generator")


name = st.text_input("Enter student name")
roll_number = st.number_input("Enter roll number", step=1, format="%d")
math = st.number_input("Enter marks for Math", min_value=0.0, max_value=100.0)
english = st.number_input("Enter marks for English", min_value=0.0, max_value=100.0)
computer = st.number_input("Enter marks for Computer", min_value=0.0, max_value=100.0)

if st.button("Generate Result"):
    total = math + english + computer
    percentage = (total / 300) * 100

   
    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'F'

    
    st.subheader("🎓 Result Summary")
    st.write(f"**Name:** {name}")
    st.write(f"**Roll Number:** {int(roll_number)}")
    st.write(f"**Math Marks:** {math}")
    st.write(f"**English Marks:** {english}")
    st.write(f"**Computer Marks:** {computer}")
    st.write(f"**Total Marks:** {total} / 300")
    st.write(f"**Percentage:** {percentage:.2f}%")
    st.write(f"**Grade:** {grade}")