import streamlit as st

st.set_page_config(page_title="AI Travel Planner")

st.title("🌍 AI Mood-Based Travel Planner")
st.write("Discover underrated places in India based on your mood ✨")

# Inputs
mood = st.selectbox("Select your mood", ["Relax", "Adventure", "Solo Healing"])
preference = st.selectbox("Preference", ["Beach", "Mountains", "Nature"])
days = st.slider("Number of days", 1, 7)

if st.button("Generate Plan"):

    if mood == "Relax" and preference == "Beach":
        place = "Gokarna"
        image = "https://upload.wikimedia.org/wikipedia/commons/6/6e/Gokarna_beach.jpg"
        itinerary = [
            "Day 1: Relax at Kudle Beach",
            "Day 2: Beach trekking & sunset",
            "Day 3: Cafe hopping"
        ]

    elif mood == "Adventure" and preference == "Mountains":
        place = "Spiti Valley"
        image = "https://upload.wikimedia.org/wikipedia/commons/3/3e/Spiti_Valley.jpg"
        itinerary = [
            "Day 1: Arrival & acclimatization",
            "Day 2: Visit monasteries",
            "Day 3: Trekking"
        ]

    else:
        place = "Varkala"
        image = "https://upload.wikimedia.org/wikipedia/commons/9/9f/Varkala_beach.jpg"
        itinerary = [
            "Day 1: Cliff walk",
            "Day 2: Ayurvedic spa",
            "Day 3: Beach sunset"
        ]

    st.subheader(f"📍 Destination: {place}")
    st.image(image)

    st.subheader("🗺️ Itinerary")
    for day in itinerary:
        st.write(day)
