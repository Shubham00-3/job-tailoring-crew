# main.py
from src.crew import build_and_run

if __name__ == "__main__":
    job_application_inputs = {
        'job_posting_url': 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1',
        'github_url': 'https://github.com/joaomdmoura',
        'personal_writeup': """Noah is an accomplished Software
        Engineering Leader with 18 years of experience, specializing in
        managing remote and in-office teams...""", # Truncated for brevity
        "resume_path": "./fake_resume.md" # Keep your resume path
    }

    result = build_and_run(job_application_inputs)
    print("\n\n########################")
    print("## Crew Execution Finished!")
    print("########################\n")
    print("Final result:")
    print(result)