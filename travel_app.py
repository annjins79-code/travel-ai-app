import streamlit as st
import random

# Page config
st.set_page_config(page_title="AI Travel Planner", layout="centered")

# Custom styling 🎨
st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🌍 AI Mood-Based Travel Planner</p>', unsafe_allow_html=True)
st.write("✨ Discover underrated places in India based on your mood")

# Inputs
mood = st.selectbox("Select your mood", ["Relax", "Adventure", "Solo Healing"])
preference = st.selectbox("Preference", ["Beach", "Mountains", "Nature"])

if st.button("Generate Plan"):

    places = []

    if mood == "Relax" and preference == "Beach":
        places = [
            ("Gokarna", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"),
            ("Varkala", "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"),
            ("Marari Beach", "https://images.unsplash.com/photo-1500375592092-40eb2168fd21")
        ]

    elif mood == "Adventure" and preference == "Mountains":
        places = [
            ("Spiti Valley", "https://images.unsplash.com/photo-1501785888041-af3ef285b470"),
            ("Tawang", "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429"),
            ("Kasol", "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0")
        ]

    else:
        places = [
            ("Coorg", "https://images.unsplash.com/photo-1501785888041-af3ef285b470"),
            ("Hampi", "https://images.unsplash.com/photo-1524492449090-1d9a1a5b3c0d"),
            ("Wayanad", "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429")
        ]

    st.subheader("📍 Recommended Destinations")

    for place, image in places:

        st.markdown(f"## 🌟 {place}")
        st.image(image)

        # Hidden gem score 💎
        score = random.randint(7, 10)
        st.write(f"💎 Hidden Gem Score: {score}/10")

        # 7-day itinerary
        st.write("🗺️ 7-Day Itinerary:")
        itinerary = [
            "Day 1: Arrival & local exploration",
            "Day 2: Visit major attractions",
            "Day 3: Adventure activities",
            "Day 4: Explore hidden spots",
            "Day 5: Cultural experience",
            "Day 6: Relax & shopping",
            "Day 7: Wrap up & departure"
        ]

        for day in itinerary:
            st.write(day)

        st.write("💡 Why visit?")
        st.write("Perfect match for your mood with unique experiences and fewer crowds.")

        st.markdown("---")
