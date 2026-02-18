import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from src.core.models import Challenge
from src.core.patterns import get_patterns_for_level


load_dotenv()

language_model_client = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


def generate_challenge(topic: str, language: str, seniority: str) -> Challenge:
    patterns = get_patterns_for_level(seniority)
    patterns_text = (
        " Common patterns for this level that often appear in challenges: "
        + "; ".join(patterns)
        + ". Prefer aligning the challenge with one or more of these patterns when relevant to the topic."
        if patterns
        else ""
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a tech lead specialized in generating code challenges for software engineers.",
            ),
            (
                "human",
                "Generate a code challenge for a {seniority} level software engineer about {topic} to solve in {language}.{patterns_hint}",
            ),
        ]
    )

    structured_language_model = language_model_client.with_structured_output(Challenge)

    chain = prompt | structured_language_model

    return chain.invoke(
        {
            "topic": topic,
            "language": language,
            "seniority": seniority,
            "patterns_hint": patterns_text,
        }
    )