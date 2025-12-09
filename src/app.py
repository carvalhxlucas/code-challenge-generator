import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from src.core.generator import generate_challenge

def main():
    st.set_page_config(
        page_title="Code Challenge Generator",
        page_icon=":computer:",
        layout="wide"
    )

    st.title("Technical Interview Generator")
    st.markdown("""
    Generate custom coding challenges for technical interview using AI.
    Define the parameters in the sidebar to create a structured problem statement with test cases.
    """)
    
    st.divider()

    with st.sidebar:
        st.header("⚙️ Configuration")
        
        language = st.selectbox(
            "Programming Language",
            ["Python", "JavaScript", "TypeScript", "Go", "Java", "SQL", "C++"]
        )
        
        seniority = st.selectbox(
            "Seniority Level",
            ["Junior", "Mid-Level", "Senior", "Staff/Principal"]
        )
        
        topic = st.text_input(
            "Specific Topic",
            value="Sorting Algorithms",
            placeholder="e.g., REST API, System Design, Graph Theory..."
        )
        
        generate_btn = st.button("🚀 Generate Challenge", type="primary")

        if generate_btn:
            if not topic:
                st.warning("Please provide a topic to proceed.")
                return

            with st.spinner(f"Generating {seniority} level challenge for {topic} in {language}..."):
                try:
                    challenge = generate_challenge(topic, language, seniority)

                    render_challenge(challenge)

                except Exception as e:
                    st.error(f"Error generating challenge: {e}")
                    return

def render_challenge(challenge):
    col1, col2 = st.columns(2)

    with col1:
        st.caption("Challenge Statement")
        st.subheader(challenge.title)

    with col2:
        st.caption("Estimated Difficulty")
        st.subheader(challenge.difficulty)

    st.markdown("---")
    st.markdown(challenge.description)
    st.markdown("---")
    st.markdown("### Test Cases")
    for i, test in enumerate(challenge.test_cases):
        with st.expander(f"Test Case {i+1}"):
            st.markdown(f"**Input:** {test.input_val}")
            st.markdown(f"**Output:** {test.output_val}")
            st.markdown(f"**Hidden:** {test.is_hidden}")

if __name__ == "__main__":
    main()