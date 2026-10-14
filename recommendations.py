"""Rule-based, educational recommendations for weak assessment categories."""

TIPS = {
    "Phishing": [
        "Check the sender address and exact link destination before interacting.",
        "Be cautious of urgency, unexpected prizes, threats, and requests for credentials.",
        "Verify requests using a known official channel rather than replying to the message.",
    ],
    "Passwords": [
        "Use a long, unique password or passphrase for every account.",
        "Consider a reputable password manager to generate and store unique passwords.",
        "Enable multi-factor authentication on important accounts.",
    ],
    "Privacy": [
        "Never disclose OTPs, recovery codes, or passwords to callers or messages.",
        "Review app permissions and privacy settings periodically.",
        "Think before posting: images and posts can reveal location or personal details.",
    ],
    "Safe Browsing": [
        "Check the full domain and use trusted bookmarks or official apps.",
        "Keep your browser and operating system updated.",
        "Do not enable macros or install software just because a page asks you to.",
    ],
}

def get_recommendations(category_scores, threshold=70):
    recommendations = []
    for category, result in category_scores.items():
        if result.get("score", 0) < threshold:
            tips = TIPS.get(category, ["Review safe cybersecurity practices for this topic."])
            recommendations.append({
                "category": category,
                "score": result.get("score", 0),
                "tips": tips,
            })
    return recommendations
