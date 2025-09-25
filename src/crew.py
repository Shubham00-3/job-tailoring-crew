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
    resume_path = inputs.get("resume_path", "./fake_resume.md")

    # 1. Create agents
    researcher = create_researcher(resume_path)
    profiler = create_profiler(resume_path)
    strategist = create_resume_strategist(resume_path)
    interviewer = create_interview_preparer(resume_path)

    # 2. Create tasks
    research_task = create_research_task(researcher)
    profile_task = create_profile_task(profiler)
    resume_task = create_resume_strategy_task(strategist, [research_task, profile_task])
    interview_task = create_interview_prep_task(interviewer, [research_task, profile_task, resume_task])

    # 3. Build Crew
    crew = Crew(
        agents=[researcher, profiler, strategist, interviewer],
        tasks=[research_task, profile_task, resume_task, interview_task],
        verbose=True
    )

    # 4. Run Crew
    result = crew.kickoff(inputs=inputs)
    return result
