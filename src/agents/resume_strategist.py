from crewai import Agent
from src.config.llm import get_llm
from src.utils.tools import build_tools

def create_resume_strategist(resume_path: str):
    tools = build_tools(resume_path)
    return Agent(
        role="Resume Strategist",
        goal="Refine and tailor resumes so they align perfectly with job postings.",
        tools=[tools["scrape"], tools.get("search"), tools["read_resume"]],
        llm=get_llm(),
        verbose=True,
        backstory=(
            "You refine resumes to highlight the most relevant "
            "skills and experiences, ensuring they resonate with recruiters."
        )
    )
