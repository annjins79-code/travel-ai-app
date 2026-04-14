import streamlit as st
import random

# Page config
st.set_page_config(page_title="AI Travel Planner", layout="wide")

# 🔥 Custom UI Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #89f7fe, #66a6ff);
    }

    h1 {
        color: #ffffff;
        text-align: center;
        font-size: 50px;
        font-family: 'Trebuchet MS', sans-serif;
    }

    h2, h3 {
        color: #2c3e50;
        font-family: 'Verdana', sans-serif;
    }

    .stButton>button {
        background-color: #ff7eb3;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        font-weight: bold;
    }

    .stSelectbox label, .stSlider label {
        font-size: 18px;
        font-weight: bold;
        color: #2c3e50;
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

        score = random.randint(7, 10)
        st.write(f"💎 Hidden Gem Score: {score}/10")

        st.write("🗺️ 7-Day Itinerary:")
        itinerary = [
            "Day 1: Arrival & exploration",
            "Day 2: Major attractions",
            "Day 3: Adventure activities",
            "Day 4: Hidden gems",
            "Day 5: Cultural experience",
            "Day 6: Relax & shopping",
            "Day 7: Departure"
        ]

        for day in itinerary:
            st.write(day)

        st.markdown("---")
