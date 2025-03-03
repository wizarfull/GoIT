import sys
import os
import re
from collections import defaultdict
from typing import List, Dict


def parse_log_line(line: str) -> dict:
    match = re.match(r'(\S+ \S+) (\S+) (.+)', line)
    if match:
        date_time = match.group(1)
        level = match.group(2)
        message = match.group(3)
        return {"date_time": date_time, "level": level, "message": message}
    return {}


def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log = parse_log_line(line.strip())
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при зчитуванні файлу: {e}")
        sys.exit(1)
    
    return logs


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda log: log["level"].lower() == level.lower(), logs))


def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    level_count = defaultdict(int)
    for log in logs:
        level_count[log["level"]] += 1
    return dict(level_count)


def display_log_counts(counts: Dict[str, int]):
    print(f"{'Рівень логування':<15}| Кількість")
    print("-" * 30)
    for level, count in counts.items():
        print(f"{level:<15}| {count}")
    print()


def display_log_details(logs: List[dict], level: str):
    print(f"Деталі логів для рівня '{level.upper()}':")
    for log in logs:
        if log["level"].lower() == level.lower():
            print(f"{log['date_time']} - {log['message']}")
    print()


def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до файлу логів.")
        sys.exit(1)

    log_file = sys.argv[1]

    logs = load_logs(log_file)
    
    if len(sys.argv) == 3:
        level_filter = sys.argv[2].lower()
        filtered_logs = filter_logs_by_level(logs, level_filter)
        display_log_counts(count_logs_by_level(filtered_logs))
        display_log_details(filtered_logs, level_filter)
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)


if __name__ == "__main__":
    main()
