"""Question bank for CyberAware Pro. Educational content only."""

QUESTIONS = [
    {
        "id": "PH01", "category": "Phishing",
        "question": "You receive an unexpected email asking you to click a link and verify your bank account immediately. What is the safest action?",
        "options": [
            "Click quickly so the account is not blocked",
            "Reply with your account details",
            "Avoid the link and verify through the bank's official app or known contact",
            "Forward it to friends to ask if it is real",
        ],
        "answer": 2,
        "explanation": "Urgency and requests for sensitive information are common warning signs. Verify independently using a trusted channel.",
    },
    {
        "id": "PH02", "category": "Phishing",
        "question": "A message says you won a prize but asks you to pay a small fee first. What should you do?",
        "options": [
            "Pay the fee to claim the prize",
            "Treat it as suspicious and verify the sender independently",
            "Share your OTP to confirm your identity",
            "Download any attached file",
        ],
        "answer": 1,
        "explanation": "Unexpected prizes that require payment or sensitive information may be scams.",
    },
    {
        "id": "PW01", "category": "Passwords",
        "question": "Which password practice is strongest?",
        "options": [
            "Use the same password everywhere",
            "Use your name and birth year",
            "Use a unique, long password or passphrase for each account",
            "Share passwords with a close friend",
        ],
        "answer": 2,
        "explanation": "Unique, long passwords reduce the risk that one compromised account exposes others. A password manager can help.",
    },
    {
        "id": "PW02", "category": "Passwords",
        "question": "What is the best additional protection for an important account?",
        "options": [
            "Turn off security alerts",
            "Enable multi-factor authentication (MFA)",
            "Use a shorter password",
            "Store the password in a public note",
        ],
        "answer": 1,
        "explanation": "MFA adds another verification step beyond the password.",
    },
    {
        "id": "PR01", "category": "Privacy",
        "question": "An unknown caller asks you to read out a one-time password (OTP). What should you do?",
        "options": [
            "Share it if they know your name",
            "Share only half of it",
            "Do not share it; end the interaction and contact the service through official channels",
            "Post it in a group for advice",
        ],
        "answer": 2,
        "explanation": "Never disclose OTPs or verification codes to callers or messages claiming to be support.",
    },
    {
        "id": "PR02", "category": "Privacy",
        "question": "Before posting a photo publicly, what should you consider?",
        "options": [
            "Whether it exposes private details such as location, ID cards, or personal information",
            "Only whether the photo is clear",
            "Whether everyone can download it",
            "Nothing; public posts are always safe",
        ],
        "answer": 0,
        "explanation": "Photos can reveal personal information, locations, documents, or other details unintentionally.",
    },
    {
        "id": "SB01", "category": "Safe Browsing",
        "question": "A website address looks almost like a familiar shopping website but has an extra word. What should you do?",
        "options": [
            "Enter your card details because the logo looks familiar",
            "Check the exact domain and navigate using a trusted bookmark or official app",
            "Ignore the address",
            "Use the same password to test it",
        ],
        "answer": 1,
        "explanation": "Lookalike domains can imitate legitimate sites. Check the domain carefully and use a trusted route.",
    },
    {
        "id": "SB02", "category": "Safe Browsing",
        "question": "What is a safer approach to an unexpected email attachment?",
        "options": [
            "Enable macros if prompted",
            "Open it on your main computer immediately",
            "Verify the sender and expected file; follow your institution's security process",
            "Disable antivirus first",
        ],
        "answer": 2,
        "explanation": "Unexpected attachments may be malicious. Verify them before opening and follow security procedures.",
    },
]

def get_questions():
    """Return the question bank in its defined order."""
    return QUESTIONS
