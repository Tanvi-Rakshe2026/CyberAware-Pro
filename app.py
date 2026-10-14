import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from questions import get_questions
from scoring import calculate_score, calculate_category_scores, performance_label
from recommendations import get_recommendations
from database import init_db, save_assessment, fetch_assessments
from reporting import build_text_report

st.set_page_config(page_title="CyberAware Pro | Security Learning Hub", page_icon="🛡️", layout="wide", initial_sidebar_state="expanded")
init_db()

# ----------------------------- Visual system -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root { --ink:#eaf1ff; --muted:#9eacc7; --panel:#111d33; --panel2:#172641; --line:rgba(174,196,231,.15); --cyan:#64e4d4; --blue:#7c9cff; }
html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
.stApp { background: radial-gradient(ellipse at 12% 0%, #182e50 0%, #0a1222 42%, #080f1d 100%); color:var(--ink); }
[data-testid="stHeader"] { background:rgba(8,15,29,.7); }
[data-testid="stSidebar"] { background:linear-gradient(180deg,#0e1a2d,#0a1220); border-right:1px solid var(--line); }
[data-testid="stSidebar"] * { color:var(--ink); }
.block-container { padding-top:2rem; padding-bottom:3rem; max-width:1450px; }
h1,h2,h3,h4 { font-family:'Space Grotesk',sans-serif !important; letter-spacing:-.035em; color:#f3f7ff !important; }
p, label, .stMarkdown, [data-testid="stCaptionContainer"] { color:var(--ink); }
[data-testid="stMetric"] { background:linear-gradient(145deg,rgba(26,43,70,.92),rgba(16,29,49,.92)); border:1px solid var(--line); padding:18px 20px; border-radius:18px; box-shadow:0 10px 30px rgba(0,0,0,.08); }
[data-testid="stMetricLabel"] { color:#a9b9d4 !important; font-size:.85rem; }
[data-testid="stMetricValue"] { color:#f5f8ff !important; font-family:'Space Grotesk',sans-serif; }
[data-testid="stMetricDelta"] { color:var(--cyan) !important; }
div[data-testid="stForm"] { background:rgba(17,29,51,.72); border:1px solid var(--line); border-radius:20px; padding:24px; }
.stButton button, .stDownloadButton button, [data-testid="stFormSubmitButton"] button { border-radius:12px; min-height:44px; font-weight:700; border:1px solid rgba(100,228,212,.35); }
.stButton button[kind="primary"], [data-testid="stFormSubmitButton"] button[kind="primary"] { background:linear-gradient(100deg,#4bd7c8,#75a4ff); color:#071323; border:0; }
.stTextInput input, .stSelectbox div[data-baseweb="select"] > div { background:#0d192b; color:#f5f8ff; border-color:var(--line); border-radius:10px; }
.stRadio label, .stCheckbox label { color:#e5edfc !important; }
hr { border-color:var(--line); }
[data-testid="stExpander"] { border:1px solid var(--line); border-radius:14px; background:rgba(17,29,51,.55); }
.hero { position:relative; overflow:hidden; padding:32px 34px; border:1px solid rgba(134,166,222,.22); border-radius:24px; background:linear-gradient(120deg,rgba(22,44,75,.98),rgba(19,39,66,.78) 58%,rgba(31,65,86,.72)); margin-bottom:22px; box-shadow:0 18px 48px rgba(0,0,0,.12); }
.hero:after { content:'✳'; position:absolute; right:5%; top:-38px; font-size:190px; color:rgba(100,228,212,.08); transform:rotate(12deg); }
.eyebrow { color:var(--cyan); text-transform:uppercase; letter-spacing:.16em; font-size:.72rem; font-weight:700; }
.hero-title { font-family:'Space Grotesk',sans-serif; font-size:clamp(2rem,4vw,3.2rem); font-weight:700; line-height:1.06; color:#f5f8ff; margin:8px 0 12px; letter-spacing:-.055em; }
.hero-copy { color:#b6c6e0; font-size:1.03rem; max-width:700px; line-height:1.65; }
.pill { display:inline-block; padding:6px 10px; border:1px solid rgba(100,228,212,.3); background:rgba(100,228,212,.08); color:#8ff0e4; border-radius:999px; font-size:.75rem; margin:0 6px 6px 0; }
.section-kicker { color:var(--cyan); text-transform:uppercase; font-size:.73rem; letter-spacing:.14em; font-weight:700; margin-bottom:5px; }
.panel { background:linear-gradient(145deg,rgba(21,37,62,.88),rgba(13,25,43,.86)); border:1px solid var(--line); border-radius:18px; padding:20px 22px; height:100%; transition:transform .18s ease,border-color .18s ease,background .18s ease; }
@media (hover:hover) { .panel:hover { transform:translateY(-3px); border-color:rgba(100,228,212,.38); background:linear-gradient(145deg,rgba(25,46,75,.95),rgba(14,28,48,.92)); } }
[data-testid='stVerticalBlockBorderWrapper'] { border-radius:18px; }
[data-testid='stRadio'] > div { gap:8px; }
[data-testid='stRadio'] label { border:1px solid var(--line); padding:10px 13px; border-radius:12px; background:rgba(12,24,41,.52); }
[data-testid='stRadio'] label:has(input:checked) { border-color:rgba(100,228,212,.65); background:rgba(100,228,212,.08); }
.stTabs [data-baseweb='tab-list'] { gap:8px; }
.stTabs [data-baseweb='tab'] { border-radius:10px 10px 0 0; padding:10px 16px; }
@media (max-width: 700px) { .block-container { padding-top:1rem; padding-left:1rem; padding-right:1rem; } .hero { padding:22px 20px; } .hero-title { font-size:2rem; } .panel { padding:16px; } }
.panel-title { font-family:'Space Grotesk',sans-serif; font-size:1.08rem; font-weight:600; color:#f4f7ff; margin-bottom:6px; }
.panel-copy { color:#aab9d2; font-size:.9rem; line-height:1.55; }
.question-tag { color:#8ff0e4; font-size:.75rem; text-transform:uppercase; letter-spacing:.12em; font-weight:700; }
div[data-testid="stProgressBar"] > div > div { background:linear-gradient(90deg,#4bd7c8,#7c9cff); }
[data-testid="stAlert"] { border-radius:14px; }
footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.markdown("<div style='display:flex;align-items:center;gap:10px;font-family:Space Grotesk;font-size:1.35rem;font-weight:700'><span style='display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:12px;background:rgba(100,228,212,.12);border:1px solid rgba(100,228,212,.25)'>🛡️</span><span>CyberAware <span style='color:#64e4d4'>Pro</span></span></div>", unsafe_allow_html=True)
    st.caption("AWARENESS • ASSESSMENT • INSIGHTS")
    st.divider()
    nav_options = ["✦ Overview", "◉ Take assessment", "▥ Insights dashboard", "ⓘ Project details"]
    if "nav_target" in st.session_state:
        st.session_state["page_nav"] = st.session_state.pop("nav_target")
    if "page_nav" not in st.session_state:
        st.session_state["page_nav"] = nav_options[0]
    page = st.radio("WORKSPACE", nav_options, key="page_nav", label_visibility="visible")
    st.divider()
    st.markdown("<div class='section-kicker'>PRIVACY FIRST</div>", unsafe_allow_html=True)
    st.markdown("<div class='panel-copy'>Use anonymous participant codes only. Never enter real names, contact details, passwords, OTPs, or other personal information.</div>", unsafe_allow_html=True)
    st.markdown("<br><div style='color:#7183a2;font-size:.75rem'>STUDENT PROJECT PROTOTYPE · v2.0 UI</div>", unsafe_allow_html=True)

questions = get_questions()

# Helpers

def render_hero(kicker, title, copy, tags=None):
    tag_html = "".join(f"<span class='pill'>{t}</span>" for t in (tags or []))
    st.markdown(f"<div class='hero'><div class='eyebrow'>{kicker}</div><div class='hero-title'>{title}</div><div class='hero-copy'>{copy}</div><div style='margin-top:16px'>{tag_html}</div></div>", unsafe_allow_html=True)

def make_chart_layout(fig, height=320):
    fig.update_layout(height=height, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      font=dict(color="#dce7fa", family="DM Sans"), margin=dict(l=10,r=10,t=45,b=10),
                      title_font=dict(size=16, color="#f4f7ff"), legend=dict(font=dict(color="#c5d2e8")))
    fig.update_xaxes(gridcolor="rgba(174,196,231,.10)", zerolinecolor="rgba(174,196,231,.10)", tickfont=dict(color="#aab9d2"))
    fig.update_yaxes(gridcolor="rgba(174,196,231,.10)", zerolinecolor="rgba(174,196,231,.10)", tickfont=dict(color="#aab9d2"))
    return fig

if page == "✦ Overview":
    df = fetch_assessments()
    render_hero("CYBERSECURITY LEARNING LAB", "Build safer digital habits.", "An interactive awareness assessment that turns everyday cyber scenarios into clear, practical learning recommendations.", ["Phishing awareness", "Password hygiene", "Privacy", "Safe browsing"])
    if df.empty:
        total_submissions, avg_score, unique_ids = 0, None, 0
    else:
        total_submissions, avg_score, unique_ids = len(df), df["score"].mean(), df["participant_id"].nunique()
    m1, m2, m3 = st.columns(3)
    m1.metric("Assessment submissions", total_submissions, help="Saved locally in the project's SQLite database")
    m2.metric("Average score", f"{avg_score:.1f}%" if avg_score is not None else "—", help="Based on submitted assessments")
    m3.metric("Anonymous participants", unique_ids)
    status_cols = st.columns([1.2, 1, 1])
    with status_cols[0]:
        st.markdown("<div class='panel'><div class='section-kicker'>LEARNING ENGINE</div><div class='panel-title'>Adaptive recommendations</div><div class='panel-copy'>Topic scores are translated into practical next steps after every assessment.</div><br><span class='pill'>● Active</span></div>", unsafe_allow_html=True)
    with status_cols[1]:
        st.markdown("<div class='panel'><div class='section-kicker'>QUESTION BANK</div><div style='font-family:Space Grotesk;font-size:2rem;font-weight:700;color:#f5f8ff'>08 <span style='font-size:.9rem;color:#9eacc7;font-weight:500'>scenarios</span></div><div class='panel-copy'>Phishing, passwords, privacy and safe browsing.</div></div>", unsafe_allow_html=True)
    with status_cols[2]:
        st.markdown("<div class='panel'><div class='section-kicker'>PROJECT MODE</div><div class='panel-title'>Privacy-first</div><div class='panel-copy'>Anonymous codes only. No password or OTP collection.</div><br><span class='pill'>Local prototype</span></div>", unsafe_allow_html=True)
    if not df.empty:
        st.markdown("<br><div class='section-kicker'>AWARENESS SNAPSHOT</div><h2 style='margin-top:0'>Assessment activity</h2>", unsafe_allow_html=True)
        chart_col, insight_col = st.columns([1.35, .65])
        with chart_col:
            trend = df.copy()
            trend["score"] = pd.to_numeric(trend["score"], errors="coerce")
            trend["Attempt"] = range(1, len(trend) + 1)
            fig = px.area(trend, x="Attempt", y="score", markers=True, range_y=[0,100], title="Score trend across submissions")
            fig.update_traces(line_color="#64e4d4", fillcolor="rgba(100,228,212,.10)", marker_size=7)
            st.plotly_chart(make_chart_layout(fig, 280), use_container_width=True)
        with insight_col:
            post_count = int((df["assessment_type"] == "post").sum()) if "assessment_type" in df else 0
            pre_count = int((df["assessment_type"] == "pre").sum()) if "assessment_type" in df else 0
            st.markdown(f"<div class='panel'><div class='panel-title'>Assessment stages</div><div class='panel-copy'>See how the project data is building up.</div><br><div style='display:flex;justify-content:space-between;margin:12px 0 6px'><span>Pre-test</span><b>{pre_count}</b></div><div style='height:7px;border-radius:99px;background:#263854;overflow:hidden'><div style='height:7px;width:{min(100, pre_count/max(1,len(df))*100):.0f}%;background:#7c9cff;border-radius:99px'></div></div><div style='display:flex;justify-content:space-between;margin:14px 0 6px'><span>Post-test</span><b>{post_count}</b></div><div style='height:7px;border-radius:99px;background:#263854;overflow:hidden'><div style='height:7px;width:{min(100, post_count/max(1,len(df))*100):.0f}%;background:#64e4d4;border-radius:99px'></div></div><br><div class='panel-copy'>Use the same anonymous code for paired comparisons.</div></div>", unsafe_allow_html=True)
    st.markdown("<br><div class='section-kicker'>YOUR WORKSPACE</div><h2 style='margin-top:0'>Where would you like to start?</h2>", unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown("<div class='panel'><div class='section-kicker'>01 · ASSESS</div><div class='panel-title'>Check your awareness</div><div class='panel-copy'>Answer realistic multiple-choice questions and get a score with explanations.</div></div>", unsafe_allow_html=True)
        if st.button("Start assessment →", use_container_width=True, key="start_assess"):
            st.session_state["nav_target"] = "◉ Take assessment"
            st.rerun()
    with c2:
        st.markdown("<div class='panel'><div class='section-kicker'>02 · IMPROVE</div><div class='panel-title'>Get tailored tips</div><div class='panel-copy'>Find the topics that need more attention and review actionable safety habits.</div></div>", unsafe_allow_html=True)
        if st.button("Explore learning tips →", use_container_width=True, key="tips_button"):
            st.session_state["show_tips"] = not st.session_state.get("show_tips", False)
    with c3:
        st.markdown("<div class='panel'><div class='section-kicker'>03 · MEASURE</div><div class='panel-title'>Track progress</div><div class='panel-copy'>Compare pre-test and post-test scores and export anonymized summary data.</div></div>", unsafe_allow_html=True)
        if st.button("Open insights →", use_container_width=True, key="open_dash"):
            st.session_state["nav_target"] = "▥ Insights dashboard"
            st.rerun()
    if st.session_state.get("show_tips"):
        st.info("Quick safety checklist: pause before clicking urgent links, use unique passwords, enable MFA, never share OTPs, check website domains, and verify unexpected attachments.")
    st.markdown("<br>", unsafe_allow_html=True)
    l,r = st.columns([1.15, .85])
    with l:
        st.markdown("<div class='panel'><div class='panel-title'>Assessment journey</div><div class='panel-copy'>A simple, repeatable workflow for your field project.</div><br><b>1.</b> Run a consent-based pre-test<br><br><b>2.</b> Deliver an approved awareness session<br><br><b>3.</b> Repeat with a post-test using the same anonymous code<br><br><b>4.</b> Review score changes and document limitations</div>", unsafe_allow_html=True)
    with r:
        st.markdown("<div class='panel'><div class='panel-title'>Designed for learning</div><div class='panel-copy'>This tool is an educational prototype, not a certification or a detector of real phishing messages.</div><br><span class='pill'>Python</span><span class='pill'>Streamlit</span><span class='pill'>SQLite</span><span class='pill'>Plotly</span></div>", unsafe_allow_html=True)

elif page == "◉ Take assessment":
    render_hero("KNOWLEDGE CHECK", "Cyber awareness assessment", "Choose a stage, answer each scenario, then review your score and practical recommendations.", [f"{len(questions)} questions", "4 learning categories", "Instant feedback"])
    stage1, stage2, stage3 = st.columns(3)
    for col, number, label, detail in [(stage1,"01","Answer scenarios","Choose the safest response"),(stage2,"02","Review your score","See strengths by topic"),(stage3,"03","Improve","Follow your learning tips")]:
        with col:
            st.markdown(f"<div class='panel' style='padding:14px 16px;margin-bottom:12px'><div style='display:flex;align-items:center;gap:10px'><div style='display:flex;align-items:center;justify-content:center;min-width:34px;height:34px;border-radius:10px;background:rgba(100,228,212,.10);color:#8ff0e4;font-weight:700'>{number}</div><div><div class='panel-title' style='font-size:.95rem'>{label}</div><div class='panel-copy'>{detail}</div></div></div></div>", unsafe_allow_html=True)
    st.progress(0.0, text="Ready when you are · answer all questions to unlock your results")
    with st.form("assessment_form"):
        a,b = st.columns([1,1])
        with a:
            participant_id = st.text_input("Anonymous participant code", placeholder="e.g. P001", max_chars=40, help="Use the same code for pre-test and post-test. Do not use your name.")
        with b:
            assessment_type = st.selectbox("Assessment stage", ["pre", "post"], format_func=lambda x: "Pre-test · Before learning" if x == "pre" else "Post-test · After learning")
        st.markdown("---")
        selected = {}
        categories = list(dict.fromkeys(q["category"] for q in questions))
        for category_index, category in enumerate(categories, start=1):
            group = [q for q in questions if q["category"] == category]
            st.markdown(f"<div class='section-kicker'>MODULE {category_index:02d}</div><h3>{category}</h3>", unsafe_allow_html=True)
            for q in group:
                st.markdown(f"<div class='question-tag'>{q['id']} · SCENARIO</div><div style='font-size:1.04rem;font-weight:600;margin:7px 0 12px;color:#f2f6ff'>{q['question']}</div>", unsafe_allow_html=True)
                selected[q["id"]] = st.radio("Select one answer", q["options"], key=f"answer_{q['id']}", index=None, label_visibility="collapsed")
                st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
            if category_index < len(categories): st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("---")
        consent = st.checkbox("I understand this is an educational activity and agree to submit an anonymous assessment summary for the project analysis.")
        submitted = st.form_submit_button("Submit answers & reveal results →", type="primary", use_container_width=True)
    if submitted:
        if not participant_id.strip():
            st.error("Please enter an anonymous participant code.")
        elif not consent:
            st.error("Please confirm the consent statement before submitting.")
        elif any(selected[q["id"]] is None for q in questions):
            st.error("Almost there — please answer every question before submitting.")
        else:
            answer_rows, correct = [], 0
            for q in questions:
                is_correct = selected[q["id"]] == q["options"][q["answer"]]
                correct += int(is_correct)
                answer_rows.append({"question_id":q["id"],"category":q["category"],"correct":is_correct,"selected":selected[q["id"]],"correct_answer":q["options"][q["answer"]],"explanation":q["explanation"]})
            score = calculate_score(correct, len(questions))
            category_scores = calculate_category_scores(answer_rows)
            tips = get_recommendations(category_scores)
            try:
                record_id = save_assessment(participant_id, assessment_type, len(questions), correct, score, category_scores)
                report = build_text_report(participant_id, assessment_type, correct, len(questions), score, category_scores, tips)
                st.session_state["last_result"] = {"participant_id":participant_id.strip(),"assessment_type":assessment_type,"correct":correct,"total":len(questions),"score":score,"category_scores":category_scores,"recommendations":tips,"report":report,"record_id":record_id,"answer_rows":answer_rows}
                st.success("Your assessment is saved. Your learning summary is ready below.")
            except Exception as exc:
                st.error(f"Could not save assessment: {exc}")
    result = st.session_state.get("last_result")
    if result:
        st.markdown("---")
        st.markdown("<div class='section-kicker'>YOUR PERSONAL SUMMARY</div><h2>Results & next steps</h2>", unsafe_allow_html=True)
        x,y,z = st.columns(3)
        x.metric("Awareness score", f"{result['score']:.0f}%")
        y.metric("Correct answers", f"{result['correct']} / {result['total']}")
        z.metric("Readiness level", performance_label(result["score"]))
        st.progress(min(max(result["score"]/100,0),1), text=f"Overall score · {result['score']:.0f}%")
        left,right = st.columns([1.05,.95])
        with left:
            category_df = pd.DataFrame([{"Category":name,"Score (%)":vals["score"]} for name,vals in result["category_scores"].items()])
            fig = px.bar(category_df, x="Score (%)", y="Category", orientation="h", range_x=[0,100], text="Score (%)", title="Your topic strengths")
            fig.update_traces(marker_color="#64e4d4", texttemplate="%{text:.0f}%", textposition="outside", cliponaxis=False)
            st.plotly_chart(make_chart_layout(fig,300), use_container_width=True)
        with right:
            st.markdown("<div class='panel'><div class='panel-title'>Recommended learning</div><div class='panel-copy'>Focus on topics below 70% first.</div><br>", unsafe_allow_html=True)
            if result["recommendations"]:
                for item in result["recommendations"]:
                    st.markdown(f"**{item['category']} · {item['score']:.0f}%**")
                    for tip in item["tips"]: st.markdown(f"- {tip}")
            else:
                st.success("Strong result across all categories. Keep practising safe habits.")
            st.markdown("</div>", unsafe_allow_html=True)
        with st.expander("Review answers & explanations", expanded=False):
            for row in result["answer_rows"]:
                st.markdown(f"{'✅' if row['correct'] else '❌'} **{row['question_id']} · {row['category']}**")
                st.write(f"Your answer: {row['selected']}")
                if not row["correct"]: st.write(f"Correct answer: {row['correct_answer']}")
                st.caption(row["explanation"])
                st.divider()
        st.download_button("⬇ Download personal report (.txt)", result["report"], file_name=f"cyberaware_{result['assessment_type']}_report.txt", mime="text/plain", use_container_width=True)

elif page == "▥ Insights dashboard":
    render_hero("PROJECT ANALYTICS", "Turn results into insight.", "Explore score patterns, compare assessment stages, and export a summary for your field-project report.", ["Score distribution", "Pre / post comparison", "CSV export"])
    df = fetch_assessments()
    if df.empty:
        st.markdown("<div class='panel'><div class='panel-title'>No results yet</div><div class='panel-copy'>Complete an assessment first. Submitted results will appear here automatically.</div></div>", unsafe_allow_html=True)
        st.info("Tip: use fictional/demo responses while developing. Collect real participant data only after your project guide approves the plan and consent process.")
    else:
        df["score"] = pd.to_numeric(df["score"], errors="coerce")
        a,b,c,d = st.columns(4)
        a.metric("Submissions", len(df))
        b.metric("Average score", f"{df['score'].mean():.1f}%")
        c.metric("Highest score", f"{df['score'].max():.0f}%")
        d.metric("Anonymous IDs", df["participant_id"].nunique())
        left,right = st.columns(2)
        with left:
            fig = px.histogram(df, x="score", nbins=10, range_x=[0,100], title="Score distribution")
            fig.update_traces(marker_color="#7c9cff")
            st.plotly_chart(make_chart_layout(fig), use_container_width=True)
        with right:
            stage_df = df.copy()
            stage_df["Stage"] = stage_df["assessment_type"].map({"pre":"Pre-test","post":"Post-test"})
            fig = px.box(stage_df, x="Stage", y="score", points="all", color="Stage", title="Pre-test vs post-test")
            fig.update_layout(showlegend=False)
            fig.update_traces(marker_color="#64e4d4", line_color="#7c9cff")
            st.plotly_chart(make_chart_layout(fig), use_container_width=True)
        paired = df.pivot_table(index="participant_id", columns="assessment_type", values="score", aggfunc="last").reset_index()
        if "pre" in paired.columns and "post" in paired.columns:
            paired = paired.dropna(subset=["pre","post"])
        else:
            paired = pd.DataFrame()
        st.markdown("<div class='section-kicker'>LEARNING OUTCOME</div><h2>Paired progress</h2>", unsafe_allow_html=True)
        if not paired.empty:
            paired["Change (percentage points)"] = (paired["post"] - paired["pre"]).round(2)
            avg_change = paired["Change (percentage points)"].mean()
            p1,p2 = st.columns([.6,1.4])
            p1.metric("Average change", f"{avg_change:+.1f} pp", help="Post-test minus pre-test, in percentage points")
            with p2:
                fig = px.bar(paired, x="participant_id", y="Change (percentage points)", title="Score change by anonymous participant", text_auto="+.1f")
                fig.update_traces(marker_color="#64e4d4")
                st.plotly_chart(make_chart_layout(fig,280), use_container_width=True)
            st.dataframe(paired, use_container_width=True, hide_index=True)
        else:
            st.info("Paired comparison appears after at least one anonymous participant has both a pre-test and a post-test under the same ID.")
        export_df = df.drop(columns=["category_scores"], errors="ignore")
        st.download_button("⬇ Export anonymized summary as CSV", export_df.to_csv(index=False), file_name="cyberaware_assessment_summary.csv", mime="text/csv", use_container_width=True)
        with st.expander("View saved summary records"):
            st.dataframe(export_df, use_container_width=True, hide_index=True)
        st.warning("Privacy reminder: the local database is not designed for public multi-user hosting. Do not publish or upload participant records.")

else:
    render_hero("FIELD PROJECT", "About CyberAware Pro", "A coded cybersecurity awareness assessment and adaptive learning prototype for educational use.", ["Python application", "Rule-based learning", "Data analysis"])
    st.markdown("### Project at a glance")
    c1,c2 = st.columns(2)
    with c1:
        st.markdown("<div class='panel'><div class='panel-title'>Problem statement</div><div class='panel-copy'>People may recognize cybersecurity terms but still struggle to choose safe actions in realistic situations.</div><br><div class='panel-title'>Aim</div><div class='panel-copy'>Assess basic awareness, identify weaker topics, and recommend learning actions based on category scores.</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='panel'><div class='panel-title'>Technology stack</div><div class='panel-copy'>Python · Streamlit · SQLite · Pandas · Plotly · pytest</div><br><div class='panel-title'>Core features</div><div class='panel-copy'>Scenario-based quiz, score calculation, category analysis, personalized recommendations, downloadable report, CSV export, and pre/post comparison.</div></div>", unsafe_allow_html=True)
    st.markdown("### How the system works")
    flow1,flow2,flow3,flow4 = st.columns(4)
    for col,num,title,desc in [(flow1,"01","Assess","Answer awareness questions"),(flow2,"02","Score","Calculate overall and topic scores"),(flow3,"03","Recommend","Show practical learning tips"),(flow4,"04","Measure","Compare pre/post summaries")]:
        with col:
            st.markdown(f"<div class='panel'><div class='section-kicker'>{num}</div><div class='panel-title'>{title}</div><div class='panel-copy'>{desc}</div></div>", unsafe_allow_html=True)
    st.markdown("### Methodology & ethical use")
    st.write("1. Obtain approval from the project guide before gathering real data.")
    st.write("2. Explain the activity and obtain informed consent.")
    st.write("3. Use anonymous participant codes and collect only what is necessary.")
    st.write("4. Compare pre-test and post-test scores, report limitations, and avoid overstating results.")
    st.warning("Limitations: the question bank is small, recommendations are rule-based, and score improvement alone does not prove long-term behaviour change. This is not a certification, phishing detector, or production data platform.")
    with st.expander("Technical modules"):
        st.code("app.py                 Streamlit user interface\nquestions.py           Scenario question bank\nscoring.py             Score and category calculations\nrecommendations.py     Rule-based learning tips\ndatabase.py             SQLite summary storage\nreporting.py            Text report generation\ntests/                  Unit tests")
