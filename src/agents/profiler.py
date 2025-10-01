# src/agents/profiler.py
from crewai import Agent
from src.config.llm import get_llm
from src.utils.tools import scrape_tool, search_tool, read_resume, semantic_search_resume

def create_profiler():
    return Agent(
        role="Personal Profiler for Engineers",
        goal="Do incredible research on job applicants to help them stand out",
        tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
        llm=get_llm(),
        verbose=True,
        backstory=(
            "Equipped with analytical prowess, you dissect and synthesize "
            "information from diverse sources to craft comprehensive "
            "personal and professional profiles."
        )
    )