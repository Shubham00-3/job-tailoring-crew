from crewai import Task

def create_research_task(agent):
    return Task(
        description=(
            "Analyze the job posting URL ({job_posting_url}) "
            "to extract key skills, experiences, and qualifications. "
            "Use your tools to scrape and categorize the requirements."
        ),
        expected_output=(
            "A structured list of job requirements including skills, "
            "qualifications, and experiences."
        ),
        agent=agent,
        async_execution=True
    )
