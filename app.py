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
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Explain: {topic}"}
                ]
            )

            result = response.choices[0].message.content

            st.markdown("### 📖 Explanation:")
            st.write(result)
    else:
        st.warning("Please enter a topic!")
