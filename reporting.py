"""CSV and text report helpers."""
from datetime import datetime

def build_text_report(participant_id, assessment_type, correct, total, score, category_scores, recommendations):
    lines = [
        "CYBERAWARE PRO — ASSESSMENT REPORT",
        "=" * 40,
        f"Anonymous participant ID: {participant_id}",
        f"Assessment type: {assessment_type.upper()}",
        f"Generated: {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z')}",
        f"Correct answers: {correct}/{total}",
        f"Overall score: {score:.2f}%",
        "",
        "CATEGORY SCORES",
        "-" * 40,
    ]
    for category, values in category_scores.items():
        lines.append(f"{category}: {values['score']:.2f}% ({values['correct']}/{values['total']})")
    lines += ["", "RECOMMENDATIONS", "-" * 40]
    if not recommendations:
        lines.append("No category was below the recommendation threshold. Continue practising safe habits.")
    for item in recommendations:
        lines.append(f"{item['category']} — {item['score']:.2f}%")
        lines.extend(f"  • {tip}" for tip in item["tips"])
    lines += ["", "Educational awareness tool only; this is not a security certification."]
    return "\n".join(lines)
