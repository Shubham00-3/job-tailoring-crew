import os
from crewai_tools import FileReadTool, ScrapeWebsiteTool, SerperDevTool
from pathlib import Path

# This line tells the ScrapeWebsiteTool to use Browserless for JavaScript rendering
os.environ["BROWSERLESS_API_KEY"] = os.getenv("BROWSERLESS_API_KEY")

def build_tools(resume_path: str):
    rp = Path(resume_path)
    if not rp.exists():
        rp.write_text(
            "# Placeholder resume\n\nUpdate this with your real resume.",
            encoding="utf-8",
        )

    tools = {
        "scrape": ScrapeWebsiteTool(),
        "search": SerperDevTool(),
        "read_resume": FileReadTool(file_path=str(rp)),
    }
    return {k: v for k, v in tools.items() if v is not None}