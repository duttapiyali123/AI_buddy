import streamlit as st

# Page config
st.set_page_config(page_title="AI Study Buddy", page_icon="📚")

# Title
st.title("📚 AI Study Buddy")
st.write("Ask any topic and get a simple explanation like a friendly teacher!")

# Input
topic = st.text_input("Enter your topic:", placeholder="e.g. Photosynthesis")

# Button logic
if st.button("Explain"):
    if topic:
        with st.spinner("Thinking... 🤔"):

            # Dummy AI-like explanation (no API needed)
            result = f"""
📘 **What is {topic}?**
{topic} is an important concept explained in a very simple way for students.

🧠 **Key Points:**
- {topic} is used in studies and real-life situations  
- It helps in building basic understanding  
- It is easier when broken into small parts  

🌍 **Example:**
Think of {topic} like something you use or see in your daily life.

📌 **Summary:**
{topic} becomes easy when you learn step-by-step with simple explanations.
"""

        # OUTPUT (correct indentation)
        st.markdown("### 📖 Explanation:")
        st.markdown(result)

    else:
        st.warning("Please enter a topic!")
