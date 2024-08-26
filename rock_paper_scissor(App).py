import random
import streamlit as st

# Initialize counters
if "user_wins" not in st.session_state:
    st.session_state.user_wins = 0
if "computer_wins" not in st.session_state:
    st.session_state.computer_wins = 0

# Define the options and corresponding animation paths (GIFs)
options = ["rock", "paper", "scissors"]
animations = {
    "rock": "https://media.tenor.com/tBccMJz1fBAAAAAC/rock-everythingeverywhereallatonce.gif",
    "paper": "https://clipart-library.com/images/rcLoRReXi.gif",
    "scissors": "https://clipart-library.com/images/6Tr56da8c.gif"
}

# Title of the app
st.title("Rock-Paper-Scissors Game")



# Display the options in a vertical layout
st.write("Choose your option:")

# Button and image display
user_input = None

# Create columns for layout
col1, col2, col3 = st.columns(3)

# User input initialization
user_input = None

# Rock
with col1:
    if st.button("Rock"):
        user_input = "rock"
    if user_input == "rock" or not user_input:
        st.image(animations["rock"], caption="Rock", width=150)

# Paper
with col2:
    if st.button("Paper"):
        user_input = "paper"
    if user_input == "paper" or not user_input:
        st.image(animations["paper"], caption="Paper", width=150)

# Scissors
with col3:
    if st.button("Scissors"):
        user_input = "scissors"
    if user_input == "scissors" or not user_input:
        st.image(animations["scissors"], caption="Scissors", width=150)

if user_input:
    # Generate computer's pick
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    
    st.write("Computer picked:")
    st.image(animations[computer_pick], caption=computer_pick.capitalize(), width=150)

    # Determine the winner
    if user_input == computer_pick:
        st.write("### It's a tie!")
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        st.write("### You won!")
        st.session_state.user_wins += 1
    else:
        st.write("### You lost!")
        st.session_state.computer_wins += 1

# Display the scores
st.write("You won", st.session_state.user_wins, "times.")
st.write("Computer won", st.session_state.computer_wins, "times.")

# Quit button
if st.button("Quit"):
    st.write("Goodbye!")
    st.stop()