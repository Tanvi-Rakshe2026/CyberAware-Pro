from scoring import calculate_score, calculate_category_scores, performance_label
from recommendations import get_recommendations

def test_score_normal():
    assert calculate_score(4, 8) == 50.0

def test_score_empty():
    assert calculate_score(0, 0) == 0.0

def test_category_scores():
    rows = [
        {"category": "Phishing", "correct": True},
        {"category": "Phishing", "correct": False},
        {"category": "Privacy", "correct": True},
    ]
    result = calculate_category_scores(rows)
    assert result["Phishing"]["score"] == 50.0
    assert result["Privacy"]["score"] == 100.0

def test_recommendation_for_weak_category():
    scores = {"Phishing": {"score": 50.0, "correct": 1, "total": 2}}
    result = get_recommendations(scores)
    assert len(result) == 1
    assert result[0]["category"] == "Phishing"

def test_performance_label():
    assert performance_label(90) == "Strong"
    assert performance_label(75) == "Good"
    assert performance_label(55) == "Developing"
    assert performance_label(20) == "Needs Improvement"
