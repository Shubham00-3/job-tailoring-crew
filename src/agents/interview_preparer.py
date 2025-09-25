from crewai import Agent
from src.config.llm import get_llm
from src.utils.tools import build_tools

def create_interview_preparer(resume_path: str):
    tools = build_tools(resume_path)
    return Agent(
        role="Interview Preparer",
        goal="Generate interview questions and talking points tailored to resume & job requirements.",
        tools=[tools["scrape"], tools.get("search"), tools["read_resume"]],
        llm=get_llm(),
        verbose=True,
        backstory=(
            "You anticipate interview dynamics and craft questions "
            "that help candidates connect their experience to the role."
        )
    )
