from crewai import Task

def create_profile_task(agent):
    return Task(
        description=(
            "Compile a detailed personal and professional profile "
            "using the GitHub ({github_url}) and personal write-up "
            "({personal_writeup}). Extract and synthesize information."
        ),
        expected_output=(
            "A comprehensive profile document: skills, project experiences, "
            "contributions, interests, and communication style."
        ),
        agent=agent,
        async_execution=True
    )
