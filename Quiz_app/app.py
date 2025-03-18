import streamlit as st
import random
import time
import base64

def load_animation():
    return """
    <style>
        @keyframes balloons {
            0% { transform: translateY(100vh); opacity: 1; }
            100% { transform: translateY(-100vh); opacity: 0; }
        }
        .balloon {
            position: fixed;
            bottom: -100px;
            width: 20px;
            height: 30px;
            background-color: red;
            border-radius: 50%;
            animation: balloons 4s ease-in-out infinite;
        }
    </style>
    <div class='balloon'></div>
    """

def show_balloons():
    st.markdown(load_animation(), unsafe_allow_html=True)
    time.sleep(2)

def main():
    st.markdown("""<h1 style='text-align: center; color: #4CAF50;'>🎉 Quiz App 🎉</h1>""", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Test your knowledge and have fun! ✅</p>", unsafe_allow_html=True)
    
    questions = [
        {"question": "What is the capital of Pakistan?", "options": ["Karachi", "Lahore", "Islamabad", "Quetta"], "answer": "Islamabad"},
        {"question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Bangalore", "Chennai"], "answer": "Delhi"},
        {"question": "What is the capital of Turkey?", "options": ["Istanbul", "Ankara", "Izmir", "Antalya"], "answer": "Ankara"},
        {"question": "What is the capital of USA?", "options": ["New York", "Washington DC", "Los Angeles", "Chicago"], "answer": "Washington DC"},
        {"question": "What is the capital of China?", "options": ["Shanghai", "Beijing", "Guangzhou", "Shenzhen"], "answer": "Beijing"},
        {"question": "What is the capital of UK?", "options": ["Manchester", "Birmingham", "London", "Liverpool"], "answer": "London"},
        {"question": "What is the capital of Australia?", "options": ["Melbourne", "Sydney", "Canberra", "Brisbane"], "answer": "Canberra"},
        {"question": "What is the capital of France?", "options": ["Marseille", "Lyon", "Paris", "Toulouse"], "answer": "Paris"},
        {"question": "What is the capital of Germany?", "options": ["Berlin", "Munich", "Hamburg", "Frankfurt"], "answer": "Berlin"},
        {"question": "What is the capital of Italy?", "options": ["Milan", "Rome", "Naples", "Turin"], "answer": "Rome"},
    ]
    
    if "score" not in st.session_state:
        st.session_state.score = 0
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(questions)
    
    question = st.session_state.current_question
    st.subheader(question["question"])
    selected_option = st.radio("Choose Your Answer:", question["options"], key="answer")
    
    if st.button("Submit"):
        if selected_option == question["answer"]:
            st.success("🎉 Correct Answer!")
            st.session_state.score += 1
            show_balloons()
        else:
            st.error(f"❌ Wrong Answer! Correct Answer is: {question['answer']}")
        time.sleep(2)
        st.session_state.current_question = random.choice(questions)
        st.rerun()
    
if __name__ == "__main__":
    main()
