import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from src.core.models import Challenge

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

def generate_challenge(topic: str, language: str, seniority: str) -> Challenge:
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a tech lead specialized in generating code challenges for software engineers."),
        ("human", "Generate a code challenge for a {seniority} level software engineer about {topic} to solve in {language}."),
    ])

    structured_llm = llm.with_structured_output(Challenge)

    chain = prompt | structured_llm

    try:
        result = chain.invoke({
            "topic": topic,
            "language": language,
            "seniority": seniority,
        })
        return result
    except Exception as e:
        st.error(f"Error generating challenge: {e}")
        return None