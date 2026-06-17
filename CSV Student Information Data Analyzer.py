"""
学员数据分析器
================
读取学员 CSV 文件（姓名、邮箱、加入日期、所在国家、对赌状态），
统计总人数、各国家人数、对赌完成率，并将结果保存为 report.json。

使用方法（在 VS Code 终端中运行）：
    python student_analyzer.py students.csv

如果不传参数，默认读取当前目录下的 students.csv。
"""

import sys
import json
from pathlib import Path

import pandas as pd


def load_data(csv_path: str) -> pd.DataFrame:
    """读取 CSV 文件并返回 DataFrame，文件不存在则报错退出。"""
    path = Path(csv_path)
    if not path.exists():
        print(f"❌ 找不到文件: {csv_path}")
        sys.exit(1)

    df = pd.read_csv(path)

    required_cols = {"name", "email", "joined_date", "country", "bet_status"}
    missing = required_cols - set(df.columns)
    if missing:
        print(f"❌ CSV 缺少必要的列: {missing}")
        sys.exit(1)

    return df


def analyze(df: pd.DataFrame) -> dict:
    """用 Pandas 进行统计分析，返回结果字典。"""

    # 总人数
    total_students = len(df)

    # 各国家人数（按人数从高到低排序）
    country_counts = (
        df["country"]
        .value_counts()
        .sort_values(ascending=False)
        .to_dict()
    )

    # 对赌状态分布（active / completed / failed 等）
    status_counts = df["bet_status"].value_counts().to_dict()

    # 对赌完成率 = completed 人数 / 总人数
    completed_count = int((df["bet_status"] == "completed").sum())
    completion_rate = round(completed_count / total_students, 4) if total_students else 0.0

    # 各国家的对赌完成率（附加细分统计，方便分析）
    country_completion = (
        df.assign(is_completed=df["bet_status"] == "completed")
        .groupby("country")["is_completed"]
        .mean()
        .round(4)
        .to_dict()
    )

    report = {
        "total_students": total_students,
        "country_counts": country_counts,
        "bet_status_counts": status_counts,
        "completed_count": completed_count,
        "completion_rate": completion_rate,
        "completion_rate_percent": f"{completion_rate * 100:.2f}%",
        "completion_rate_by_country": country_completion,
    }

    return report


def save_report(report: dict, output_path: str = "report.json") -> None:
    """将统计结果保存为 JSON 文件（UTF-8，中文不转码）。"""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"✅ 统计结果已保存到: {output_path}")


def print_summary(report: dict) -> None:
    """在终端打印一份易读的统计摘要。"""
    print("\n=== 学员数据统计摘要 ===")
    print(f"总人数: {report['total_students']}")

    print("\n各国家人数:")
    for country, count in report["country_counts"].items():
        print(f"  {country}: {count}")

    print(f"\n对赌完成率: {report['completion_rate_percent']} "
          f"({report['completed_count']}/{report['total_students']})")

    print("\n各国家对赌完成率:")
    for country, rate in report["completion_rate_by_country"].items():
        print(f"  {country}: {rate * 100:.2f}%")
    print("========================\n")


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "students.csv"

    df = load_data(csv_path)
    report = analyze(df)
    print_summary(report)
    save_report(report)


if __name__ == "__main__":
    main()
