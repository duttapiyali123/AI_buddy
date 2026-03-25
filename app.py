import streamlit as st
from openai import OpenAI
import os

# Get API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Study Buddy", page_icon="📚")

st.title("📚 AI Study Buddy")
st.write("Ask any topic and get a simple explanation!")

topic = st.text_input("Enter your topic:", placeholder="e.g. Photosynthesis")

system_prompt = """
You are a friendly teacher for a 16-year-old student.

Explain topics in:
- simple words
- short sentences
- bullet points

Structure:
1. What is it?
2. Key Points
3. Example
4. Summary
"""

if st.button("Explain"):
    if topic:
        with st.spinner("Thinking... 🤔"):
           result = f"""
📘 What is {topic}?
This is a simple explanation of {topic}.

🧠 Key Points:
- It is an important concept
- Used in studies and real life
- Helps in understanding basics

🌍 Example:
Think of {topic} like something you use in daily life.

📌 Summary:
{topic} is easy when explained step by step.
"""

            st.markdown("### 📖 Explanation:")
            st.write(result)
    else:
        st.warning("Please enter a topic!")
