import streamlit as st
import random

st.set_page_config(page_title="AI Travel Planner", layout="wide")

# 🌿 BOHO AESTHETIC UI
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #fdf6ec, #f3e5d8);
}
h1 {
    text-align: center;
    color: #5a3e36;
    font-size: 48px;
    font-family: Georgia, serif;
}
h2, h3 {
    color: #6b4f4f;
}
.block {
    background-color: #fffaf3;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 20px;
}
.stButton>button {
    background-color: #c97b63;
    color: white;
    border-radius: 8px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 AI Mood-Based Travel Planner")
st.write("✨ Discover underrated places in India based on your vibe")

# Inputs
mood = st.selectbox("Mood", ["Relax", "Adventure", "Solo Healing"])
preference = st.selectbox("Preference", ["Beach", "Mountains", "Nature"])

if st.button("Generate Plan"):

    if mood == "Relax" and preference == "Beach":
        places = [
            ("Gokarna", "Karnataka", [
                "https://images.unsplash.com/photo-1589308454676-7c78a3a2d0a3",
                "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944",
                "https://images.unsplash.com/photo-1593693397690-362cb9666fc2"
            ]),
            ("Varkala", "Kerala", [
                "https://images.unsplash.com/photo-1593693397690-362cb9666fc2",
                "https://images.unsplash.com/photo-1589308454676-7c78a3a2d0a3",
                "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944"
            ])
        ]

    elif mood == "Adventure" and preference == "Mountains":
        places = [
            ("Spiti Valley", "Himachal Pradesh", [
                "https://images.unsplash.com/photo-1549887534-1541e9326642",
                "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
                "https://images.unsplash.com/photo-1519681393784-d120267933ba"
            ]),
            ("Tawang", "Arunachal Pradesh", [
                "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
                "https://images.unsplash.com/photo-1549887534-1541e9326642",
                "https://images.unsplash.com/photo-1519681393784-d120267933ba"
            ])
        ]

    elif mood == "Solo Healing" and preference == "Nature":
        places = [
            ("Coorg", "Karnataka", [
                "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
                "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",
                "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"
            ]),
            ("Wayanad", "Kerala", [
                "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",
                "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
                "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"
            ])
        ]

    else:
        places = [
            ("Hampi", "Karnataka", [
                "https://images.unsplash.com/photo-1524492449090-1d9a1a5b3c0d",
                "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
                "https://images.unsplash.com/photo-1519681393784-d120267933ba"
            ])
        ]

    st.subheader("📍 Recommended Destinations")

    for place, state, images in places:

        st.markdown('<div class="block">', unsafe_allow_html=True)

        st.subheader(f"🌟 {place}, {state}")

        cols = st.columns(3)
        for i in range(3):
            with cols[i]:
                st.image(images[i], use_container_width=True)

        score = random.randint(7, 10)
        st.write(f"💎 Hidden Gem Score: {score}/10")
        st.progress(score * 10)

        st.write("🗺️ 7-Day Plan:")
        for i in range(1, 8):
            st.write(f"Day {i}: Explore & enjoy")

        st.markdown('</div>', unsafe_allow_html=True)
