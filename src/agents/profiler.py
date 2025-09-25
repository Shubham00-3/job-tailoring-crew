from crewai import Agent
from src.config.llm import get_llm
from src.utils.tools import build_tools

def create_profiler(resume_path: str):
    tools = build_tools(resume_path)
    return Agent(
        role="Personal Profiler for Engineers",
        goal="Build a comprehensive personal & professional profile from resumes, GitHub, and notes.",
        tools=[tools["scrape"], tools.get("search"), tools["read_resume"]],
        llm=get_llm(),
        verbose=True,
        backstory=(
            "You synthesize resumes, GitHub contributions, and write-ups "
            "to produce a strong candidate profile."
        )
    )
