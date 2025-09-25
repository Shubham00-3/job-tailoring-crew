from src.crew import build_and_run

if __name__ == "__main__":
    inputs = {
        "job_posting_url": "https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1",
        "github_url": "https://github.com/Shubham00-3",
        "personal_writeup": """Shubham is a Computer Science Engineer
        passionate about AI/ML and multi-agent systems. He has built
        multiple GenAI projects using LangGraph, CrewAI, and modern
        ML stacks, aiming to apply them in real-world use cases.""",
        "resume_path": "./fake_resume.md"
    }

    result = build_and_run(inputs)
    print("Execution finished. Final result summary:")
    print(result)
