from crewai import Agent
from src.config.llm import get_llm
from src.utils.tools import build_tools

def create_researcher(resume_path: str):
    tools = build_tools(resume_path)
    return Agent(
        role="Tech Job Researcher",
        goal="Analyze job postings and extract all required skills, experiences, and qualifications.",
        tools=[tools["scrape"], tools.get("search")],
        llm=get_llm(),
        verbose=True,
        backstory=(
            "You are sharp at dissecting job postings, spotting both explicit "
            "and hidden requirements companies are after."
        )
    )
