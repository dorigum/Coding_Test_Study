import os
import datetime

# 유형별 폴더 리스트
CATEGORY_DIRS = [
    "Queue",
    "Stack",
    "Sort",
    "Greedy",
    "DFS_BFS",
    "BinarySearch",
    "DynamicProgramming"
]

README_PATH = "README.md"

def generate_readme():
    total_count = 0
    latest_update = None

    readme_lines = []
    readme_lines.append("# 📚 Coding Test Solutions (Java)\n")
    readme_lines.append("코딩 테스트 문제 풀이 및 해설 모음입니다.\n")
    readme_lines.append("> Java 기반 풀이, 문제 유형별 정리\n\n")

    for category in CATEGORY_DIRS:
        if os.path.exists(category):
            readme_lines.append(f"## 📂 {category}\n")
            files = sorted([f for f in os.listdir(category) if f.endswith(".md")])
            total_count += len(files)
            for file in files:
                title = file.replace(".md", "").replace("_", " ")
                link = f"{category}/{file}"
                readme_lines.append(f"- [{title}]({link})")
                # 최신 업데이트 날짜 갱신
                file_time = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(category, file)))
                if latest_update is None or file_time > latest_update:
                    latest_update = file_time
            readme_lines.append("\n")

    # 통계 정보 추가
    readme_lines.insert(3, f"**📌 총 문제 수:** {total_count}개")
    if latest_update:
        readme_lines.insert(4, f"**🕒 최근 업데이트:** {latest_update.strftime('%Y-%m-%d %H:%M:%S')}")
    readme_lines.insert(5, "\n---\n")

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(readme_lines))

    print(f"✅ README 갱신 완료 → {README_PATH}")
    print(f"📌 총 문제 수: {total_count}개")
    if latest_update:
        print(f"🕒 최근 업데이트: {latest_update.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    generate_readme()
