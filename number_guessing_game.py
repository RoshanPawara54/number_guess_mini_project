import random
import streamlit as st
import time

def back():
  """Renders a 'Play Again' button that resets the game state."""
  if st.button("Play Again"):
    # Reset game-specific state variables
    for key in ['game_started', 'attempt_left', 'a', 'select', 'ch']:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

def game():
    """Handles the main game logic when the game is active."""
    st.write("---")
    st.write("I have thought of a number. Now it's your turn to guess!")

    # Handle guess submission
    guess = st.number_input("Guess a number between 1 and 100:", min_value=1, max_value=100, key="guess_input")

    if st.button("Check Guess"):
        st.session_state.attempt_left -= 1

        if guess == st.session_state.select:
            st.success(f"You got it! The number was {st.session_state.select}.")
            st.balloons()
            time.sleep(5)
            st.session_state.game_over = True
            st.rerun()
        elif st.session_state.attempt_left == 0:
            st.error(f"Game Over! You've used all your attempts. The secret number was {st.session_state.select}.")
            time.sleep(5)
            st.session_state.game_over = True
            st.rerun()
        elif guess < st.session_state.select:
            st.warning(f"Too low! You have {st.session_state.attempt_left} attempts left.")
            provide_hint(guess)
        elif guess > st.session_state.select:
            st.warning(f"Too high! You have {st.session_state.attempt_left} attempts left.")
            provide_hint(guess)

    # Display hint button for hard mode
    if st.session_state.a == 5 and st.session_state.attempt_left <= 3:
        if st.button("Need a Hint?"):
            if st.session_state.select < 50:
                st.info("Hint: The number is less than 50.")
            else:
                st.info("Hint: The number is 50 or greater.")

def provide_hint(current_guess):
    """Provides a hint based on the game difficulty."""
    difference = abs(st.session_state.select - current_guess)
    if st.session_state.a == 10: # Easy
        if difference <= 5:
            st.info("Hint: You are very close! (within 5)")
        elif difference <= 10:
            st.info("Hint: You are getting warm... (within 10)")
    elif st.session_state.a == 7: # Medium
        if difference <= 5:
            st.info("Hint: You are very close!")

def start(ch):
    """Initializes game state when 'Start Game' is clicked."""
    if st.button("Start Game"):
        if ch == 1:
            st.session_state.attempt_left = 10
            st.session_state.a = 10
        elif ch == 2:
            st.session_state.attempt_left = 7
            st.session_state.a = 7
        else:
            st.session_state.attempt_left = 5
            st.session_state.a = 5
        st.session_state.ch = ch
        st.session_state.select = random.randint(1, 100)
        st.session_state.game_started = True
        st.session_state.game_over = False
        st.rerun()

def number_guessing_game():
    """Main function to control the app's flow."""
    st.title("Number Guessing Game")

    # If game is running, show game interface
    if st.session_state.get('game_started', False):
        if st.session_state.get('game_over', False):
            back()
        else:
            game()
    # Otherwise, show the setup screen
    else:
        st.write("I will think of a number between 1 and 100. You have to guess it!")
        st.write("---")
        st.write("**Choose your difficulty:**")
        st.write("Level 1 (Easy): 10 attempts")
        st.write("Level 2 (Medium): 7 attempts")
        st.write("Level 3 (Hard): 5 attempts")

        ch = st.radio(
            "Select a level:",
            [1, 2, 3],
            format_func=lambda x: f"Level {x}",
            label_visibility="collapsed"
        )
        start(ch)

number_guessing_game()
