import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("model/model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

st.set_page_config(page_title="AI Learning System")

st.title("🎓 AI-Based Personalized Learning & Performance Prediction")

st.markdown("Enter student details below:")

# Input Fields
study_hours = st.number_input("Study Hours per Day", 0.0, 12.0, 2.0)
attendance = st.slider("Attendance (%)", 0, 100, 75)
previous_score = st.number_input("Previous Exam Score", 0, 100, 50)
assignments_completed = st.slider("Assignments Completed (%)", 0, 100, 70)
sleep_hours = st.number_input("Sleep Hours", 0.0, 12.0, 7.0)

if st.button("Predict Performance"):

    input_data = np.array([[study_hours,
                            attendance,
                            previous_score,
                            assignments_completed,
                            sleep_hours]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("✅ Prediction: PASS")
        st.markdown("### 📚 Personalized Recommendation:")
        st.write("- Maintain consistent study routine")
        st.write("- Practice advanced problems")
        st.write("- Try mock tests for higher scores")
    else:
        st.error("❌ Prediction: FAIL")
        st.markdown("### 📚 Personalized Recommendation:")
        st.write("- Increase daily study hours")
        st.write("- Improve attendance")
        st.write("- Revise weak subjects")
        st.write("- Complete all assignments")