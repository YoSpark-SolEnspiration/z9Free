import streamlit as st

def run_quiz():
    st.header("Answer 4 Quick Questions")
    q1 = st.slider("Decision-making style", 1, 10, 5)
    q2 = st.slider("Social energy level", 1, 10, 5)
    q3 = st.slider("Pace and steadiness", 1, 10, 5)
    q4 = st.slider("Attention to detail", 1, 10, 5)
    return {"D": q1, "I": q2, "S": q3, "C": q4}
