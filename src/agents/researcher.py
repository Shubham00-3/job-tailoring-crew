# src/agents/researcher.py
from crewai import Agent
from src.config.llm import get_llm
from src.utils.tools import scrape_tool, search_tool

def create_researcher():
    return Agent(
        role="Tech Job Researcher",
        goal="Make sure to do amazing analysis on job posting to help job applicants",
        tools=[scrape_tool, search_tool],
        llm=get_llm(),
        verbose=True,
        backstory=(
            "As a Job Researcher, your prowess in "
            "navigating and extracting critical "
            "information from job postings is unmatched."
        )
    )