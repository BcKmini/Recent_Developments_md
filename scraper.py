import os
import feedparser
from markdownify import markdownify as md

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCES = {
    "01_Core_Research_Papers": [
        ("ArXiv_Robotics", "http://export.arxiv.org/rss/cs.RO"),
        ("ArXiv_Computer_Vision", "http://export.arxiv.org/rss/cs.CV"),
        ("ArXiv_Machine_Learning", "http://export.arxiv.org/rss/cs.LG"),
    ],
    "02_Leading_AI_Labs": [
        ("OpenAI_Blog", "https://openai.com/blog/rss.xml"),
        ("Google_DeepMind_Blog", "https://deepmind.google/blog/rss.xml"),
        ("Meta_AI_Blog", "https://ai.meta.com/blog/rss/"),
    ],
    "03_Robotics_And_Hardware_News": [
        ("IEEE_Spectrum_Robotics", "https://spectrum.ieee.org/feeds/topic/robotics.rss"),
        ("The_Robot_Report", "https://www.therobotreport.com/feed/"),
    ],
    "04_Tech_Community_And_Blogs": [
        ("GeekNews_AI_Filter", "https://news.hada.io/rss"),
        ("Naver_D2", "https://d2.naver.com/d2.atom"),
    ]
}

def sanitize_filename(name):
    return "".join(c for c in name if c.isalnum() or c in (' ', '.', '_', '-')).rstrip()

def save_markdown(category_dir, source_dir_name, title, content):
    source_path = os.path.join(BASE_DIR, category_dir, source_dir_name)
    os.makedirs(source_path, exist_ok=True)
    safe_title = sanitize_filename(title)
    file_path = os.path.join(source_path, f"{safe_title}.md")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  - Saved to {os.path.join(category_dir, source_dir_name)}: {safe_title}.md")

def scrape_source(category_dir, source_info, max_entries=5):
    source_name, url = source_info
    print(f"\nScraping {source_name} from {url}...")
    feed = feedparser.parse(url)
    if not feed.entries:
        print(f"  - No entries found for {source_name}.")
        return

    saved_count = 0
    for entry in feed.entries:
        if saved_count >= max_entries:
            break

        title = entry.title
        
        if source_name == "GeekNews_AI_Filter":
            keywords = ["ai", "인공지능", "머신러닝", "딥러닝", "llm", "gpt", "로봇"]
            if not any(keyword in title.lower() for keyword in keywords):
                continue
        
        link = entry.link
        summary = entry.get('summary', entry.get('description', 'No summary available.'))
        
        content = f"# {title}\n\n**출처:** [{source_name}]({link})\n\n## 요약\n{md(summary)}\n"
        save_markdown(category_dir, source_name, title, content)
        saved_count += 1

if __name__ == "__main__":
    for category, source_list in SOURCES.items():
        for source in source_list:
            scrape_source(category, source)
    print("\nDaily scraping finished!")