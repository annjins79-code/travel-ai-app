import streamlit as st
import random

st.set_page_config(page_title="AI Travel Planner", layout="wide")

st.title("🌍 AI Mood-Based Travel Planner")
st.write("✨ Discover underrated places in India")

# Inputs
mood = st.selectbox("Mood", ["Relax", "Adventure", "Solo Healing"])
preference = st.selectbox("Preference", ["Beach", "Mountains", "Nature"])

if st.button("Generate Plan"):

    # ✅ Correct mapping
    if mood == "Relax" and preference == "Beach":
        places = [
            ("Gokarna", "Karnataka", [
                "https://picsum.photos/seed/gokarna1/400",
                "https://picsum.photos/seed/gokarna2/400",
                "https://picsum.photos/seed/gokarna3/400"
            ]),
            ("Varkala", "Kerala", [
                "https://picsum.photos/seed/varkala1/400",
                "https://picsum.photos/seed/varkala2/400",
                "https://picsum.photos/seed/varkala3/400"
            ])
        ]

    elif mood == "Adventure" and preference == "Mountains":
        places = [
            ("Spiti Valley", "Himachal Pradesh", [
                "https://picsum.photos/seed/spiti1/400",
                "https://picsum.photos/seed/spiti2/400",
                "https://picsum.photos/seed/spiti3/400"
            ]),
            ("Tawang", "Arunachal Pradesh", [
                "https://picsum.photos/seed/tawang1/400",
                "https://picsum.photos/seed/tawang2/400",
                "https://picsum.photos/seed/tawang3/400"
            ])
        ]

    elif mood == "Solo Healing" and preference == "Nature":
        places = [
            ("Coorg", "Karnataka", [
                "https://picsum.photos/seed/coorg1/400",
                "https://picsum.photos/seed/coorg2/400",
                "https://picsum.photos/seed/coorg3/400"
            ]),
            ("Wayanad", "Kerala", [
                "https://picsum.photos/seed/wayanad1/400",
                "https://picsum.photos/seed/wayanad2/400",
                "https://picsum.photos/seed/wayanad3/400"
            ])
        ]

    else:
        places = [
            ("Hampi", "Karnataka", [
                "https://picsum.photos/seed/hampi1/400",
                "https://picsum.photos/seed/hampi2/400",
                "https://picsum.photos/seed/hampi3/400"
            ])
        ]

    st.subheader("📍 Recommended Destinations")

    # ✅ Display properly
    for place, state, images in places:

        st.markdown(f"## 🌟 {place}, {state}")

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

        st.markdown("---")
