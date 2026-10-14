"""Scoring helpers used by the assessment and test suite."""

def calculate_score(correct, total):
    if total <= 0:
        return 0.0
    return round((correct / total) * 100, 2)

def calculate_category_scores(answer_rows):
    results = {}
    for row in answer_rows:
        category = row["category"]
        results.setdefault(category, {"correct": 0, "total": 0})
        results[category]["total"] += 1
        if row["correct"]:
            results[category]["correct"] += 1
    for values in results.values():
        values["score"] = calculate_score(values["correct"], values["total"])
    return results

def performance_label(score):
    if score >= 85:
        return "Strong"
    if score >= 70:
        return "Good"
    if score >= 50:
        return "Developing"
    return "Needs Improvement"
