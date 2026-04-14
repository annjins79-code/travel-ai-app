import streamlit as st
import random

st.set_page_config(page_title="AI Travel Planner", layout="wide")

# 🌿 Premium UI Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f8f9fa, #e9ecef);
    }

    h1 {
        text-align: center;
        color: #2c3e50;
        font-size: 50px;
        font-family: 'Segoe UI', sans-serif;
    }

    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
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
            ("Gokarna", "Karnataka", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"),
            ("Varkala", "Kerala", "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"),
            ("Marari Beach", "Kerala", "https://images.unsplash.com/photo-1500375592092-40eb2168fd21")
        ]
        tags = "🏖️ Chill | ☕ Cafes | 🌅 Sunset"

    elif mood == "Adventure" and preference == "Mountains":
        places = [
            ("Spiti Valley", "Himachal Pradesh", "https://images.unsplash.com/photo-1501785888041-af3ef285b470"),
            ("Tawang", "Arunachal Pradesh", "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429"),
            ("Kasol", "Himachal Pradesh", "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0")
        ]
        tags = "⛰️ Trekking | 🚵 Adventure | ❄️ Scenic"

    else:
        places = [
            ("Coorg", "Karnataka", "https://images.unsplash.com/photo-1501785888041-af3ef285b470"),
            ("Hampi", "Karnataka", "https://images.unsplash.com/photo-1524492449090-1d9a1a5b3c0d"),
            ("Wayanad", "Kerala", "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429")
        ]
        tags = "🌿 Nature | 🧘 Peace | 📸 Photography"

    st.subheader("📍 Recommended Destinations")

    for place, state, image in places:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown(f"### 🌟 {place}, {state}")
        st.image(image)

        # 💎 Hidden Gem Score with progress bar
        score = random.randint(7, 10)
        st.write(f"💎 Hidden Gem Score: {score}/10")
        st.progress(score * 10)

        # 🏷️ Tags
        st.write(f"🏷️ {tags}")

        # 💰 Budget
        budget = random.randint(5000, 15000)
        st.write(f"💰 Estimated Budget: ₹{budget} for 7 days")

        # 🗺️ Itinerary
        st.write("🗺️ 7-Day Itinerary:")
        itinerary = [
            "Day 1: Arrival & local exploration",
            "Day 2: Visit major attractions",
            "Day 3: Adventure / activities",
            "Day 4: Hidden spots",
            "Day 5: Cultural experiences",
            "Day 6: Relax & shopping",
            "Day 7: Departure"
        ]

        for day in itinerary:
            st.write(day)

        # 🧳 Packing suggestions
        st.write("🧳 Packing Suggestions:")
        st.write("- Comfortable clothes")
        st.write("- Power bank")
        st.write("- Camera / phone")
        st.write("- Essentials (ID, medicines)")

        st.markdown('</div>', unsafe_allow_html=True)
