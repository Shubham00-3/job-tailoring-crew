from crewai_tools import FileReadTool, MDXSearchTool, ScrapeWebsiteTool, SerperDevTool
from pathlib import Path
from src.config.settings import SERPER_API_KEY

def build_tools(resume_path: str):
    rp = Path(resume_path)
    if not rp.exists():
        rp.write_text("# Placeholder resume\n\nUpdate this with your real resume.", encoding="utf-8")

    tools = {
        "scrape": ScrapeWebsiteTool(),
        "search": SerperDevTool() if SERPER_API_KEY else None,
        "read_resume": FileReadTool(file_path=str(rp)),
        # "semantic_resume": MDXSearchTool(mdx=str(rp))
    }
    return {k: v for k, v in tools.items() if v is not None}
