#------z9Free.py------
import streamlit as st
from z9_spiral_logic import map_disc_to_stage
from trait_summary import summarize_trait
from visuals import generate_radar_chart
from utils import load_json_file
from opportunity_loader import load_basic_opportunities

# Tailored Stage Explanations by primary DISC trait for Stages 1–8
STAGE_EXPLANATIONS = {
    # … (your existing content) …
}

def main():
    st.set_page_config(page_title="Z9 Discovery Tool (Free v1.1)", layout="centered")
    st.title("🧩 Z9Free Discovery Tool – A 4-Question Check-In")
    st.markdown("🆕 *Welcome to z9Free! Test out the new wave of self coaching check in tools!*")
    st.markdown("---")

    # Mood selector
    mood = st.slider(
        "🌀 How are you feeling right now (Helps to stretch the results)? (0 = low, 10 = high)",
        0, 10, 5, 1
    )
    st.markdown(f"**Your current mood level:** {mood}/10")
    st.markdown("---")

    # DISC sliders
    st.markdown("Answer each question, based upon how you currently feel, on a scale from 1 (low) to 5 (high):")
    d = st.slider("1️⃣ Do I want to take charge? (Dominance)", 1, 5, 3)
    i = st.slider("2️⃣ Do I want to inspire others? (Influence)", 1, 5, 3)
    s = st.slider("3️⃣ Do I want to seek harmony? (Steadiness)", 1, 5, 3)
    c = st.slider("4️⃣ Do I want to value structure? (Conscientiousness)", 1, 5, 3)

    if st.button("📊 Get My Quick Insight"):
        scores = {k: float(v) for k, v in {"D": d, "I": i, "S": s, "C": c}.items()}
        stage = map_disc_to_stage(d, i, s, c)
        primary = max(scores, key=lambda k: scores[k])
        score_value = scores[primary]

        # Stage & trait explanation
        st.success(f"Your Z9 Spiral Stage: **{stage}**")
        template = STAGE_EXPLANATIONS.get(primary, {}).get(stage, "")
        if template:
            st.markdown(f"**{template.format(score=score_value)}**")
        st.markdown(f"**Your primary DISC style is {primary} with a score of {score_value}.**")

        # Personalized summary (trait + stage + mood)
        summary = summarize_trait(scores, stage, mood)
        st.subheader("🔍 Your Personalized Summary")
        st.markdown(summary)

        # Radar chart
        fig = generate_radar_chart(scores)
        st.subheader("🔵 DISC Radar Chart")
        st.pyplot(fig)

        # Quick remedy links
        remedies = load_json_file("remedy_traits.json").get(primary, {})
        for idx, link in enumerate(remedies.get("products", []), 1):
            st.markdown(f"- [🎁 Remedy Option {idx} →]({link})")

        # Opportunity Snapshot
        opps = load_basic_opportunities(scores, mood)
        if opps:
            st.subheader("🔮 Opportunity Snapshot")
            for o in opps:
                st.markdown(f"- {o}")
        else:
            st.write("No quick opportunities found right now.")

    # 🚀 Upgrade CTA: Spiral Start → CoachFree
    st.markdown("---")
    st.subheader("🚀 Try More Z9 Paths")

    col2, col3 = st.columns([1, 1])

    with col2:
        st.markdown("""
        <div style="
            padding: 20px;
            background: #FFFACD;  /* LemonChiffon (light yellow) */
            border: 2px solid #FFD700;  /* Gold border */
            border-radius: 10px;
            text-align: center;
        ">
            <a href="https://payhip.com/b/Ct8Nl" target="_blank">
                <button style="
                    background-color: #228B22;  /* ForestGreen */
                    color: white;
                    padding: 12px 24px;
                    font-size: 16px;
                    border: none;
                    border-radius: 6px;
                    cursor: pointer;
                ">
                    🌿 Spiral Start Coaching
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="
            padding: 20px;
            background: #FFFACD;  /* LemonChiffon */
            border: 2px solid #FFD700;
            border-radius: 10px;
            text-align: center;
        ">
            <a href="https://z9coachfree.streamlit.app/" target="_blank">
                <button style="
                    background-color: #228B22;
                    color: white;
                    padding: 12px 24px;
                    font-size: 16px;
                    border: none;
                    border-radius: 6px;
                    cursor: pointer;
                ">
                    🌿 Try z9CoachFree
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)



if __name__ == "__main__":
    main()
