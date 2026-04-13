import streamlit as st

st.title("🌍 AI Travel Planner")

mood = st.selectbox("Mood", ["Relax", "Adventure", "Solo"])

if st.button("Generate"):
    if mood == "Relax":
        st.write("Go to Gokarna 🏖️")
    elif mood == "Adventure":
        st.write("Try Spiti Valley ⛰️")
    else:
        st.write("Visit Varkala 🌊")
