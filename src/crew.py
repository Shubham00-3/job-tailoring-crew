# src/crew.py
from crewai import Crew
from src.agents.researcher import create_researcher
from src.agents.profiler import create_profiler
from src.agents.resume_strategist import create_resume_strategist
from src.agents.interview_preparer import create_interview_preparer
from src.tasks.research import create_research_task
from src.tasks.profile import create_profile_task
from src.tasks.resume_strategy import create_resume_strategy_task
from src.tasks.interview_prep import create_interview_prep_task

def build_and_run(inputs: dict):
    # Create agents
    researcher = create_researcher()
    profiler = create_profiler()
    resume_strategist = create_resume_strategist()
    interview_preparer = create_interview_preparer()

    # Create tasks, now including context
    research_task = create_research_task(researcher)
    profile_task = create_profile_task(profiler)
    
    resume_strategy_task = create_resume_strategy_task(
        resume_strategist,
        context=[research_task, profile_task]
    )
    
    interview_preparation_task = create_interview_prep_task(
        interview_preparer,
        context=[research_task, profile_task, resume_strategy_task]
    )

    # Build Crew
    job_application_crew = Crew(
        agents=[researcher, profiler, resume_strategist, interview_preparer],
        tasks=[research_task, profile_task, resume_strategy_task, interview_preparation_task],
        verbose=True
    )

    # Run Crew
    result = job_application_crew.kickoff(inputs=inputs)
    return result