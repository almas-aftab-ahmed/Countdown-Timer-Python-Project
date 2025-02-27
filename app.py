import streamlit as st
import time

# --- UI Customization ---
st.markdown(
    """
    <style>
        body {background-color: #ffe4e1;}
        .title {color: #ff1493; text-align: center; font-size: 50px; font-weight: bold;}
        .stButton>button {background-color: #ff69b4; color: white; font-size: 20px; border-radius: 15px; padding: 10px;}
        .stNumberInput>div>div>input {font-size: 18px; text-align: center; background-color: #fffaf0; border-radius: 10px; padding: 5px;}
        .timer {text-align: center; font-size: 50px; font-weight: bold; color: #ff4500;}
        .signature {text-align: center; font-size: 18px; font-weight: bold; color: #ff1493;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='title'>⏳ Countdown Timer 🎀</h1>", unsafe_allow_html=True)

# --- Timer Input ---
minutes = st.number_input("Enter Minutes", min_value=0, max_value=60, value=1)
seconds = st.number_input("Enter Seconds", min_value=0, max_value=59, value=0)

# Convert to total seconds
total_time = minutes * 60 + seconds

# --- Session State ---
if "time_left" not in st.session_state:
    st.session_state.time_left = total_time
if "running" not in st.session_state:
    st.session_state.running = False

# --- Timer Buttons ---
col1, col2, col3 = st.columns(3)
if col1.button("Start ⏯️"):
    st.session_state.running = True
if col2.button("Pause ⏸️"):
    st.session_state.running = False
if col3.button("Reset 🔄"):
    st.session_state.running = False
    st.session_state.time_left = total_time
    st.rerun()

# --- Timer Display ---
timer_placeholder = st.empty()

if st.session_state.running:
    while st.session_state.time_left > 0 and st.session_state.running:
        mins, secs = divmod(st.session_state.time_left, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        timer_placeholder.markdown(f"<h2 class='timer'>{timer_display}</h2>", unsafe_allow_html=True)
        time.sleep(1)
        st.session_state.time_left -= 1
        st.rerun()

# --- Time's Up Action ---
if st.session_state.time_left == 0 and st.session_state.running:
    st.balloons()
    st.session_state.running = False
    st.audio("https://www.soundjay.com/button/beep-07.wav")  # Online beep sound
    st.markdown("<h2 class='timer'>🎉 Time's Up! 🎊</h2>", unsafe_allow_html=True)

# --- Signature ---
st.markdown("<p class='signature'>Made with 💖 by Almas ❤️</p>", unsafe_allow_html=True)
