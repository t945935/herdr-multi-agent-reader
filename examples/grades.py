"""Shared chapter 2/4/5/6 contract; competition ranking uses unrounded totals."""

from collections.abc import Mapping
from math import isfinite

SUBJECTS = frozenset({"國文", "英文", "數學"})


def validate_scores(scores):
    if not isinstance(scores, Mapping) or set(scores) != SUBJECTS:
        raise ValueError("scores must contain exactly 國文、英文、數學")
    for value in scores.values():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Scores must be numeric, not bool")
        if not isfinite(value) or not 0 <= value <= 100:
            raise ValueError("Scores must be finite and between 0 and 100")
    return scores


def calculate_total(scores):
    return sum(validate_scores(scores).values())


def calculate_average(scores):
    return calculate_total(scores) / 3


def get_grade(average):
    if isinstance(average, bool) or not isinstance(average, (int, float)):
        raise ValueError("Average must be numeric")
    if not isfinite(average) or not 0 <= average <= 100:
        raise ValueError("Average must be between 0 and 100")
    return "及格" if average >= 60 else "不及格"


def rank_students(students):
    if not isinstance(students, list):
        raise ValueError("students must be a list")
    rows = []
    for student in students:
        if not isinstance(student, Mapping):
            raise ValueError("Each student must be an object")
        name = student.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name is required")
        total = calculate_total(student.get("scores"))
        average = total / 3
        rows.append({"name": name.strip(), "scores": dict(student["scores"]),
                     "total": total, "average": average, "grade": get_grade(average)})
    rows.sort(key=lambda row: row["total"], reverse=True)
    previous = None
    rank = 0
    for index, row in enumerate(rows, 1):
        if previous is None or row["total"] != previous:
            rank = index
        previous = row["total"]
        row["rank"] = rank
    return rows
