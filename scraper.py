import os
import feedparser
from markdownify import markdownify as md

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCES = {
    "01_Top_Conference_Papers": [
        ("CVPR", "http://cvpr2024.thecvf.com/feed.xml"),
        ("ICCV", "https://iccv2023.thecvf.com/feed.xml"),
        ("NeurIPS", "https://blog.neurips.cc/feed/"),
    ],
    "02_Tech_Company_Blogs": [
        ("Google_AI", "https://ai.googleblog.com/atom.xml"),
        ("Meta_AI", "https://ai.meta.com/blog/rss/"),
        ("Kakao_Tech", "https://tech.kakao.com/feed/"),
        ("Naver_D2", "https://d2.naver.com/d2.atom")
    ],
    "03_Major_IT_News": [
        ("GeekNews", "https://news.hada.io/rss"),
        ("ITWorld_Korea", "https://www.itworld.co.kr/rss")
    ],
    "04_Specialized_Research": [
        ("Computer_Vision_Foundation", "https://www.thecvf.com/feed"),
        ("IEEE_Robotics", "https://spectrum.ieee.org/feeds/topic/robotics.rss")
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

def scrape_source(category_dir, source_info, max_entries=7):
    source_name, url = source_info
    print(f"\nScraping {source_name} from {url}...")
    feed = feedparser.parse(url)
    if not feed.entries:
        print(f"  - No entries found for {source_name}.")
        return

    for entry in feed.entries[:max_entries]:
        title = entry.title
        link = entry.link
        summary = entry.get('summary', 'No summary available.')
        content = f"# {title}\n\n**출처:** [{source_name}]({link})\n\n## 요약\n{md(summary)}\n"
        save_markdown(category_dir, source_name, title, content)

if __name__ == "__main__":
    for category, source_list in SOURCES.items():
        for source in source_list:
            scrape_source(category, source)
    print("\nDaily scraping finished!")