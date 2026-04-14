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
        image = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
        itinerary = [
            "Day 1: Relax at Kudle Beach",
            "Day 2: Beach trekking & sunset",
            "Day 3: Cafe hopping"
        ]

    elif mood == "Adventure" and preference == "Mountains":
        place = "Spiti Valley"
        image = "https://images.unsplash.com/photo-1501785888041-af3ef285b470"
        itinerary = [
            "Day 1: Arrival & acclimatization",
            "Day 2: Visit monasteries",
            "Day 3: Trekking"
        ]

    else:
        place = "Varkala"
        image = "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"
        itinerary = [
            "Day 1: Cliff walk",
            "Day 2: Ayurvedic spa",
            "Day 3: Beach sunset"
        ]

    st.subheader(f"📍 Destination: {place}")
    
    try:
        st.image(image, caption=place)
    except:
        st.write("Image not available")

    st.subheader("🗺️ Itinerary")
    for day in itinerary:
        st.write(day)

    # NEW FEATURE 🔥
    st.subheader("💡 Why this place?")
    st.write("This destination matches your mood and preference, offering a unique and less crowded experience.")
