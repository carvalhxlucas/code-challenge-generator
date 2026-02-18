import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from src.core.generator import generate_challenge
from src.core.patterns import get_patterns_for_level


CODE_LANGUAGE_MAP = {
    "Python": "python",
    "JavaScript": "javascript",
    "TypeScript": "typescript",
    "Go": "go",
    "Java": "java",
    "SQL": "sql",
    "C++": "cpp",
}


if hasattr(st, "dialog"):
    topic_suggestions_dialog = st.dialog("Topic suggestions", width="medium")

    @topic_suggestions_dialog
    def show_topic_suggestions_dialog(patterns, seniority):
        st.markdown(
            "Suggested topics and patterns for this level. "
            "Click one to use it as the challenge topic:"
        )
        for index, pattern in enumerate(patterns):
            if st.button(pattern, key=f"dialog_topic_suggestion_{seniority}_{index}"):
                st.session_state["challenge_topic"] = pattern
                st.rerun()
else:

    def show_topic_suggestions_dialog(patterns, seniority):
        st.warning(
            "Your Streamlit version does not support dialogs. "
            "Please update Streamlit to use topic suggestions in a modal dialog."
        )


def main():
    st.set_page_config(
        page_title="Code Challenge Generator",
        page_icon=":computer:",
        layout="wide",
    )

    language, seniority, topic, generate_button_clicked = render_sidebar()

    st.title("Technical Challenge Generator")
    st.markdown(
        """
        Create custom coding challenges for technical interviews using AI.
        Choose the language, seniority level, and topic to generate a complete problem statement with test cases.
        """
    )

    st.divider()

    if not generate_button_clicked:
        st.info(
            "Configure the parameters in the sidebar and click **Generate challenge** to start."
        )

    if generate_button_clicked:
        if not topic:
            st.warning("Please provide a topic to generate the challenge.")
            return

        with st.spinner(
            f"Generating a {seniority} challenge about {topic} in {language}..."
        ):
            try:
                challenge = generate_challenge(topic, language, seniority)
                render_challenge(challenge, language, seniority, topic)
            except Exception as exception:
                st.error(f"Error while generating the challenge: {exception}")


def render_sidebar():
    with st.sidebar:
        st.header("Challenge configuration")

        language = st.selectbox(
            "Programming language",
            ["Python", "JavaScript", "TypeScript", "Go", "Java", "SQL", "C++"],
        )

        seniority = st.selectbox(
            "Seniority level",
            ["Junior", "Mid-Level", "Senior", "Staff/Principal"],
        )

        topic = st.text_input(
            "Challenge topic",
            value=st.session_state.get("challenge_topic", "Sorting algorithms"),
            placeholder="E.g.: REST API, System Design, Dynamic programming, Graph theory...",
            key="challenge_topic",
        )

        patterns = get_patterns_for_level(seniority)
        if patterns:
            if st.button("See topic suggestions", use_container_width=True):
                show_topic_suggestions_dialog(patterns, seniority)

        generate_button_clicked = st.button(
            "Generate challenge",
            type="primary",
            use_container_width=True,
        )

    return language, seniority, topic, generate_button_clicked


def render_challenge(challenge, language, seniority, topic):
    header_column_left, header_column_right = st.columns([3, 2])

    with header_column_left:
        st.caption("Generated challenge")
        st.subheader(challenge.title)
        st.markdown(f"**Topic:** {topic}")

    with header_column_right:
        st.caption("Challenge summary")
        st.markdown(f"**Seniority:** {seniority}")
        st.markdown(f"**Language:** {language}")
        st.markdown(f"**Estimated difficulty:** {challenge.difficulty}")

    st.markdown("---")

    description_tab, tests_tab, solution_tab = st.tabs(
        ["Description", "Test cases", "Suggested solution"]
    )

    with description_tab:
        st.markdown(challenge.description)

    with tests_tab:
        st.markdown("### Test cases")
        for index, test_case in enumerate(challenge.test_cases):
            label = f"Test case {index + 1}"
            if test_case.is_hidden:
                label = f"{label} (hidden)"

            with st.expander(label):
                st.markdown(f"**Input:** `{test_case.input_val}`")
                st.markdown(f"**Expected output:** `{test_case.output_val}`")
                st.markdown(f"**Hidden:** {'Yes' if test_case.is_hidden else 'No'}")

    with solution_tab:
        st.markdown("### Reference solution")
        code_language = CODE_LANGUAGE_MAP.get(language, "text")
        st.code(challenge.solution, language=code_language)


if __name__ == "__main__":
    main()