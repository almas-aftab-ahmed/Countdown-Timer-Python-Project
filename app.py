import streamlit as st
import time
import pygame

# Initialize pygame for sound
pygame.mixer.init()

def play_alarm():
    pygame.mixer.music.load("https://www.fesliyanstudios.com/play-mp3/4386")  # Online alert sound
    pygame.mixer.music.play()

# UI Customization
st.markdown(
    """
    <style>
        body {background-color: #ffe4e1;}
        .title {color: #ff1493; text-align: center; font-size: 50px; font-weight: bold;}
        .stButton>button {background-color: #ff69b4; color: white; font-size: 20px; border-radius: 15px; padding: 10px;}
        .stSelectbox>div {font-size: 18px;}
        .timer {text-align: center; font-size: 40px; font-weight: bold; color: #ff4500;}
        .signature {text-align: center; font-size: 18px; font-weight: bold; color: #ff1493;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='title'>⏳ Countdown Timer 🎀</h1>", unsafe_allow_html=True)

# Timer Input
minutes = st.number_input("Enter Minutes", min_value=0, max_value=60, value=1)
seconds = st.number_input("Enter Seconds", min_value=0, max_value=59, value=0)

time_left = minutes * 60 + seconds

# Timer Control Buttons
col1, col2, col3 = st.columns(3)
start = col1.button("Start ⏯️")
pause = col2.button("Pause ⏸️")
reset = col3.button("Reset 🔄")

if "running" not in st.session_state:
    st.session_state.running = False

if start:
    st.session_state.running = True
if pause:
    st.session_state.running = False
if reset:
    st.session_state.running = False
    time_left = minutes * 60 + seconds

# Timer Logic
while time_left > 0 and st.session_state.running:
    mins, secs = divmod(time_left, 60)
    timer_display = f"{mins:02d}:{secs:02d}"
    st.markdown(f"<h2 class='timer'>{timer_display}</h2>", unsafe_allow_html=True)
    time.sleep(1)
    time_left -= 1

if time_left == 0 and start:
    st.balloons()
    play_alarm()
    st.markdown("<h2 class='timer'>🎉 Time's Up! 🎊</h2>", unsafe_allow_html=True)

# Signature
st.markdown("<p class='signature'>Made with 💖 by Almas ❤️</p>", unsafe_allow_html=True)
