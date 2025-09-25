from crewai import Task

def create_interview_prep_task(agent, context):
    return Task(
        description=(
            "Create a set of interview questions and talking points "
            "based on the tailored resume and job requirements. "
            "The goal is to prepare the candidate to confidently "
            "highlight their skills and experiences in relation to "
            "the job posting."
        ),
        expected_output=(
            "A document containing potential interview questions and "
            "talking points that showcase the candidate’s fit."
        ),
        output_file="interview_materials.md",
        context=context,
        agent=agent
    )
