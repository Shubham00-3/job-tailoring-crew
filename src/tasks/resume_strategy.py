from crewai import Task

def create_resume_strategy_task(agent, context):
    return Task(
        description=(
            "Using the profile and job requirements from previous tasks, "
            "tailor the resume to highlight the most relevant areas. "
            "Do not invent info. Update summary, experience, skills, "
            "and education to match the posting."
        ),
        expected_output=(
            "An updated resume tailored for the job posting."
        ),
        output_file="tailored_resume.md",
        context=context,
        agent=agent
    )
