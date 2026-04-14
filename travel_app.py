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
        font-family: 'Georgia', serif;
        letter-spacing: 1px;
    }

    h2, h3 {
        color: #6b4f4f;
        font-family: 'Georgia', serif;
    }

    p {
        font-family: 'Segoe UI', sans-serif;
        color: #4e4e4e;
    }

    .card {
        background-color: #fffaf3;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    .stButton>button {
        background-color: #c97b63;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🌍 AI Mood-Based Travel Planner")
st.write("✨ Discover underrated places in India based on your mood")

# Inputs
mood = st.selectbox("Select your mood", ["Relax", "Adventure", "Solo Healing"])
preference = st.selectbox("Preference", ["Beach", "Mountains", "Nature"])

if st.button("Generate Plan"):

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

    st.subheader("📍 Recommended Destinations")

    for place, state, images in places:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown(f"### 🌟 {place}, {state}")

        # 🖼️ Smaller image grid
        cols = st.columns(3)
        for i, img in enumerate(images):
            with cols[i % 3]:
                st.image(img, width=220)

        # 💎 Hidden Gem Score
        score = random.randint(7, 10)
        st.write(f"💎 Hidden Gem Score: {score}/10")
        st.progress(score * 10)

        # 💰 Budget
        budget = random.randint(5000, 15000)
        st.write(f"💰 Estimated Budget: ₹{budget} for 7 days")

        # 🗺️ Itinerary
        st.write("🗺️ 7-Day Itinerary:")
        itinerary = [
            "Day 1: Arrival & local exploration",
            "Day 2: Visit major attractions",
            "Day 3: Activities & sightseeing",
            "Day 4: Hidden gems exploration",
            "Day 5: Cultural experiences",
            "Day 6: Relax & shopping",
            "Day 7: Departure"
        ]

        for day in itinerary:
            st.write(day)

        st.markdown('</div>', unsafe_allow_html=True)wn('</div>', unsafe_allow_html=True)
