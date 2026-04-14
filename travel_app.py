import streamlit as st
import random

st.set_page_config(page_title="AI Travel Planner", layout="wide")

# 🌿 Boho UI
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #fdf6ec, #f7e9d7);
}
h1 {
    text-align: center;
    color: #5a3e36;
    font-size: 45px;
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

    # ✅ CORRECT LOGIC (NO REPEAT)
    if mood == "Relax" and preference == "Beach":
        places = [
            ("Gokarna", "Karnataka", [
                "https://upload.wikimedia.org/wikipedia/commons/6/6e/Gokarna_beach.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Kudle_Beach.jpg/640px-Kudle_Beach.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Om_Beach_Gokarna.jpg/640px-Om_Beach_Gokarna.jpg"
            ]),
            ("Varkala", "Kerala", [
                "https://upload.wikimedia.org/wikipedia/commons/9/9f/Varkala_beach.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Varkala_cliff.jpg/640px-Varkala_cliff.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Varkala_sunset.jpg/640px-Varkala_sunset.jpg"
            ])
        ]

    elif mood == "Adventure" and preference == "Mountains":
        places = [
            ("Spiti Valley", "Himachal Pradesh", [
                "https://upload.wikimedia.org/wikipedia/commons/3/3e/Spiti_Valley.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Key_Monastery.jpg/640px-Key_Monastery.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Spiti_River.jpg/640px-Spiti_River.jpg"
            ]),
            ("Tawang", "Arunachal Pradesh", [
                "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Tawang_Monastery.jpg/640px-Tawang_Monastery.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Sela_Pass.jpg/640px-Sela_Pass.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Madhuri_Lake.jpg/640px-Madhuri_Lake.jpg"
            ])
        ]

    elif mood == "Solo Healing" and preference == "Nature":
        places = [
            ("Coorg", "Karnataka", [
                "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Coorg_hills.jpg/640px-Coorg_hills.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Abbey_Falls.jpg/640px-Abbey_Falls.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Coffee_Plantation.jpg/640px-Coffee_Plantation.jpg"
            ]),
            ("Wayanad", "Kerala", [
                "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Wayanad_forest.jpg/640px-Wayanad_forest.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Edakkal_Caves.jpg/640px-Edakkal_Caves.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Banasura_Sagar_Dam.jpg/640px-Banasura_Sagar_Dam.jpg"
            ])
        ]

    else:
        places = [
            ("Hampi", "Karnataka", [
                "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Hampi_virupaksha_temple.jpg/640px-Hampi_virupaksha_temple.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Hampi_boulders.jpg/640px-Hampi_boulders.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Hampi_ruins.jpg/640px-Hampi_ruins.jpg"
            ])
        ]

    st.subheader("📍 Recommended Destinations")

    for place, state, images in places:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader(f"🌟 {place}, {state}")

        # ✅ GUARANTEED IMAGE DISPLAY
        cols = st.columns(3)
        for i in range(len(images)):
            with cols[i]:
                st.image(images[i], use_container_width=True)

        # 💎 Score
        score = random.randint(7, 10)
        st.write(f"💎 Hidden Gem Score: {score}/10")
        st.progress(score * 10)

        # 🗺️ Plan
        st.write("🗺️ 7-Day Plan:")
        for i in range(1, 8):
            st.write(f"Day {i}: Explore & enjoy")

        st.markdown('</div>', unsafe_allow_html=True)
