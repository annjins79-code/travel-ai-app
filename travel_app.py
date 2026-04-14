import streamlit as st
import random

st.set_page_config(page_title="AI Travel Planner", layout="wide")

# 🌿 BOHO STYLE
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
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 AI Mood-Based Travel Planner")
st.write("✨ Discover underrated places in India")

# Inputs
mood = st.selectbox("Mood", ["Relax", "Adventure", "Solo Healing"])
preference = st.selectbox("Preference", ["Beach", "Mountains", "Nature"])

if st.button("Generate Plan"):

    # ✅ MULTIPLE PLACES PER CONDITION
    if mood == "Relax" and preference == "Beach":
        places = [
            ("Gokarna", "Karnataka", [
                "https://upload.wikimedia.org/wikipedia/commons/6/6e/Gokarna_beach.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/0/0c/Kudle_Beach.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/5/5b/Om_Beach_Gokarna.jpg"
            ]),
            ("Varkala", "Kerala", [
                "https://upload.wikimedia.org/wikipedia/commons/9/9f/Varkala_beach.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/3/3c/Varkala_cliff.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/7/7e/Varkala_sunset.jpg"
            ])
        ]

    elif mood == "Adventure" and preference == "Mountains":
        places = [
            ("Spiti Valley", "Himachal Pradesh", [
                "https://upload.wikimedia.org/wikipedia/commons/3/3e/Spiti_Valley.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/5/5e/Key_Monastery.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/2/2e/Spiti_River.jpg"
            ]),
            ("Tawang", "Arunachal Pradesh", [
                "https://upload.wikimedia.org/wikipedia/commons/4/4f/Tawang_Monastery.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/3/3a/Sela_Pass.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/1/1c/Madhuri_Lake.jpg"
            ])
        ]

    else:
        places = [
            ("Coorg", "Karnataka", [
                "https://upload.wikimedia.org/wikipedia/commons/3/3a/Coorg_hills.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/5/5b/Abbey_Falls.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/4/4f/Coffee_Plantation.jpg"
            ]),
            ("Hampi", "Karnataka", [
                "https://upload.wikimedia.org/wikipedia/commons/0/0c/Hampi_virupaksha_temple.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/6/6e/Hampi_boulders.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/3/3f/Hampi_ruins.jpg"
            ])
        ]

    # ✅ DISPLAY MULTIPLE PLACES
    st.subheader("📍 Recommended Destinations")

    for place, state, images in places:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader(f"🌟 {place}, {state}")

        # ✅ IMAGE GRID FIXED
        cols = st.columns(3)
        for i, img in enumerate(images):
            with cols[i]:
                st.image(img, width=200)

        # 💎 Score
        score = random.randint(7, 10)
        st.write(f"💎 Hidden Gem Score: {score}/10")
        st.progress(score * 10)

        # 🗺️ Itinerary
        st.write("🗺️ 7-Day Plan:")
        for i in range(1, 8):
            st.write(f"Day {i}: Explore and enjoy")

        st.markdown('</div>', unsafe_allow_html=True)
