import streamlit as st
import anthropic
import os

# Get API key from Streamlit secrets
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

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
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1000,
                system=system_prompt,
                messages=[{"role": "user", "content": f"Explain: {topic}"}]
            )
            result = response.content[0].text
            st.markdown("### 📖 Explanation:")
            st.write(result)
    else:
        st.warning("Please enter a topic!")
