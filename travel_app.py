import streamlit as st
import random

st.set_page_config(page_title="AI Travel Planner", layout="wide")

# 🌿 BOHO STYLE UI
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #fdf6ec, #f7e9d7);
}
h1 {
    text-align: center;
    color: #5a3e36;
    font-size: 48px;
    font-family: Georgia, serif;
}
.card {
    background-color: #fffaf3;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 AI Mood-Based Travel Planner")

mood = st.selectbox("Mood", ["Relax", "Adventure", "Solo Healing"])
preference = st.selectbox("Preference", ["Beach", "Mountains", "Nature"])

if st.button("Generate Plan"):

    if mood == "Relax":
        places = [
            ("Gokarna", "Karnataka", [
                "https://upload.wikimedia.org/wikipedia/commons/6/6e/Gokarna_beach.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/0/0c/Kudle_Beach.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/5/5b/Om_Beach_Gokarna.jpg"
            ])
        ]

    elif mood == "Adventure":
        places = [
            ("Spiti Valley", "Himachal Pradesh", [
                "https://upload.wikimedia.org/wikipedia/commons/3/3e/Spiti_Valley.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/5/5e/Key_Monastery.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/2/2e/Spiti_River.jpg"
            ])
        ]

    else:
        places = [
            ("Coorg", "Karnataka", [
                "https://upload.wikimedia.org/wikipedia/commons/3/3a/Coorg_hills.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/5/5b/Abbey_Falls.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/4/4f/Coffee_Plantation.jpg"
            ])
        ]

    for place, state, images in places:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader(f"{place}, {state}")

        cols = st.columns(3)
        for i, img in enumerate(images):
            with cols[i % 3]:
                st.image(img, width=200)

        score = random.randint(7, 10)
        st.write(f"Hidden Gem Score: {score}/10")
        st.progress(score * 10)

        st.markdown('</div>', unsafe_allow_html=True)
