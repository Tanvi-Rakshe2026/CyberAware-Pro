# CyberAware Pro
### Cybersecurity Awareness Assessment & Adaptive Learning System

CyberAware Pro is a student-project prototype that assesses basic awareness of phishing, passwords, privacy, and safe browsing. It calculates scores, identifies lower-scoring topics, recommends learning tips, stores anonymous summaries in SQLite, and displays aggregate results.

## Features
- Pre-test and post-test modes
- Eight educational multiple-choice questions
- Overall and category scoring
- Rule-based recommendations for category scores below 70%
- Local SQLite persistence
- Dashboard with score distribution and pre/post comparison
- Downloadable text report and CSV summary
- Unit tests for scoring and recommendations

## Requirements
- Python 3.10 or newer
- Internet access for initial package installation

## Run on Ubuntu/Linux
```bash
cd CyberAware_Pro
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```
Streamlit will print a local URL, usually `http://localhost:8501`. Open it in the browser on the same machine.

## Run tests
```bash
pytest -q
```

## Data and privacy
- The database `cyberaware.db` is created locally on first run.
- Use anonymous IDs such as P001, not names, phone numbers, email addresses, or student roll numbers.
- Collect real participant data only after your project guide approves the method and you have informed consent.
- Do not publish the database or identifiable participant information to GitHub.
- Delete test records before sharing or demonstrating if they contain real participant results.

## Project workflow
1. Get topic and study approval from the project guide.
2. Run a consent-based pre-test using anonymous IDs.
3. Provide an approved short awareness lesson.
4. Run a post-test using the same anonymous IDs.
5. Export the aggregate summary and report the results honestly.

## Limitations
This is an educational prototype, not a security certification or an automated phishing detector. The sample question bank is small, and score changes alone do not prove long-term behavior change. Document the sample size, collection procedure, and limitations in the report.

## Suggested report sections
1. Abstract
2. Introduction and problem statement
3. Aim, objectives, scope, and limitations
4. Related work
5. Requirements and system architecture
6. Methodology and implementation
7. Ethical data collection procedure
8. Testing and results
9. Conclusion and future scope
10. References and appendices

## Folder structure
```text
CyberAware_Pro/
├── app.py
├── questions.py
├── scoring.py
├── recommendations.py
├── database.py
├── reporting.py
├── requirements.txt
├── tests/
│   └── test_scoring.py
├── evidence/
└── reports/
```
