import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SUMMARY_DIR = os.path.join(BASE_DIR, "weekly-summaries")
CATEGORIES = sorted([d for d in os.listdir(BASE_DIR) if os.path.isdir(d) and d.startswith(('01', '02', '03', '04'))])

os.makedirs(SUMMARY_DIR, exist_ok=True)

def generate_weekly_summary():
    today = datetime.now()
    if today.weekday() not in [0, 3]:
        print("Today is not Monday or Thursday. Skipping summary generation.")
        return

    print(f"It's {today.strftime('%A')}! Generating bi-weekly summary...")
    
    one_week_ago = today - timedelta(days=7)
    summary_content = f"# Bi-Weekly Tech Summary: {today.strftime('%Y-%m-%d')}\n\n"

    for category_dir in CATEGORIES:
        category_path = os.path.join(BASE_DIR, category_dir)
        category_name = category_dir.split('_', 1)[1].replace('_', ' ').title()
        summary_content += f"## 📚 {category_name}\n\n"
        is_empty_category = True
        source_dirs = sorted([d for d in os.listdir(category_path) if os.path.isdir(os.path.join(category_path, d))])

        for source_dir in source_dirs:
            source_path = os.path.join(category_path, source_dir)
            found_articles = []
            for filename in sorted(os.listdir(source_path)):
                if filename.endswith(".md"):
                    file_path = os.path.join(source_path, filename)
                    file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                    if file_mtime > one_week_ago:
                        relative_path = os.path.join(category_dir, source_dir, filename).replace("\\", "/")
                        title = filename[:-3]
                        found_articles.append(f"  - [{title}](<../{relative_path}>)")
            
            if found_articles:
                is_empty_category = False
                summary_content += f"### 🗞️ {source_dir.replace('_', ' ')}\n"
                summary_content += "\n".join(found_articles) + "\n\n"

        if is_empty_category:
            summary_content += "지난 주에 새로 수집된 글이 없습니다.\n\n"

    summary_filename = f"{today.strftime('%Y-%m-%d')}_Summary.md"
    summary_filepath = os.path.join(SUMMARY_DIR, summary_filename)

    with open(summary_filepath, "w", encoding="utf-8") as f:
        f.write(summary_content)
    
    print(f"Summary file saved to: {summary_filepath}")

if __name__ == "__main__":
    generate_weekly_summary()