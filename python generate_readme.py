import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(BASE_DIR, "README.md")

# 유형별 폴더 순서 지정
CATEGORY_ORDER = [
    "Queue", "Stack", "Sort", "Implementation", "BruteForce"
]

CATEGORY_NAMES = {
    "Queue": "🛠 자료구조 (큐)",
    "Stack": "🛠 자료구조 (스택)",
    "Sort": "📊 정렬",
    "Implementation": "🧠 구현",
    "BruteForce": "🧠 완전탐색"
}

def generate_links():
    result = []
    for category in CATEGORY_ORDER:
        category_path = os.path.join(BASE_DIR, category)
        if not os.path.exists(category_path):
            continue
        
        result.append(f"### {CATEGORY_NAMES[category]}")
        for filename in sorted(os.listdir(category_path)):
            if filename.endswith(".md"):
                title = filename.replace(".md", "").replace("_", " ")
                link = f"./{category}/{filename}"
                result.append(f"- [{title}]({link})")
        result.append("")  # 카테고리 간 공백
    return "\n".join(result)

def update_readme():
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_content = f.read()

    start_marker = "## 📂 문제 유형별 목록"
    end_marker = "## 🗂️ 폴더 구조"

    start_idx = readme_content.find(start_marker)
    end_idx = readme_content.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print("❌ README.md에 마커 위치를 찾을 수 없습니다.")
        return

    before = readme_content[:start_idx + len(start_marker)]
    after = readme_content[end_idx:]

    new_content = before + "\n\n" + generate_links() + "\n" + after

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✅ README.md 업데이트 완료!")

if __name__ == "__main__":
    update_readme()
