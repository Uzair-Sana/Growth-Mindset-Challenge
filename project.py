import streamlit as st 
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="📈")
st.title( " 🧠🌱📈 Growth Mindset Challenge: Web App with Streamlit")
st.write("- - -")

st.header("👋 Welcome To Your Growth Mindset Journey!")
st.write("Embarace challenges, Learning from mistakes, and unlocking your full potential. This app helps you develop a growth mindset with reflection, challenge, and achievements!⭐")

st.header("📈🚀 Today's Growth Mindset Quote")
st.write("“Be yourself; everyone else is already taken.""– Oscar Wilde")

st.header("💪⚔️ What's Your Challenge Today? ")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"Challenge You're Facing: **{user_input}.** Keep pushing forward towards your goal!")
else:
    st.warning("🚀 Tell us about your challenge to get started!")

st.header(" 💡 Reflect On Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection: 
    st.success(f" Great Insight! Your reflection: **{reflection}**")
else:
    st.info(" ✨🎇 Reflection on past experience help you grow! Share your difficulties")


st.header("🎉🥳 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f" Amazing! You achieved: **{achievement}** ")
else:
    st.info("Big or small, every achievement counts! Share one now! 🏅")

st.write("- - -")
st.write(" Keep believing in yourself. Growth is a journey, not a destination!")
st.write("**© Created By Uzair Sanaullah**")

