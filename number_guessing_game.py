import random
import streamlit as st   

def back():
  if st.button("Play Again"):
    st.session_state.clear()
    st.rerun()

def game():
  st.write("Soch liya..")
  st.write(st.session_state.select)
  guess = st.number_input("Guess Batao 1 to 100 :", min_value=1, max_value=100)
  if st.button("Check Guess"):
    if st.session_state.attempt_left == 0:
      st.error(f"Ops.. Sab attempt khatam Hogaye. Attempt left : {st.session_state.attempt_left} Secret Number was : {st.session_state.select}")
      back()
    else:
      if guess==st.session_state.select:
        if st.session_state.attempt_left in (10,7,5):
          st.success("7 cr....... Sahi Javab in First Try")
          st.success("Tum Jit Gaye! congrats.")
          back()
        else:
          remain = st.session_state.attempt_left - 1
          st.success(f"Tum Jit Gaye! congrats.Attempt left : {remain}")
          back()
      elif guess < st.session_state.select:
        remain = st.session_state.attempt_left - 1
        st.warning(f"Bahut chota number Guess kiya. Attempt left : {remain}")
        if st.session_state.a == 10:
          if (st.session_state.select - guess) <= 5:
             st.info("Hint: Tumhara guess 5 ke range me hai.")
          elif (st.session_state.select - guess) <= 20:
            st.info("Hint: Tumhara guess 20 ke range me hai.")
        elif st.session_state.a == 7:
          if (st.session_state.select - guess) <= 5:
            st.info("Hint: tumhara guess bahut karib hai")
        elif st.session_state.a == 5:
          if st.session_state.attempt_left <= 3:
            if st.button("Hint"):
              if st.session_state.select < 50:
                st.info("Hint: Number 51 se chota hai..")
              else:
                st.info("Hint: Number 50 se bada Hai..")
        st.session_state.attempt_left -= 1
      else:
        remain = st.session_state.attempt_left - 1
        st.warning(f"Bahut Bada number Guess Kiya. Attempt left : {remain}")
        if st.session_state.a == 10:
          if (guess - st.session_state.select) <= 5:
            st.info("Hint: Tumhara guess 5 ke range me hai.")
          elif (guess - st.session_state.select) <= 20:
            st.info("Hint: Tumhara guess 20 ke range me hai.")
        elif st.session_state.a == 7:
          if (guess - st.session_state.select) <= 5:
            st.info("Hint: tumhara guess bahut karib hai")
        elif st.session_state.a == 5:
          if st.session_state.attempt_left <= 3:
            if st.button("Hint"):
              if st.session_state.select < 50:
                st.info("Hint: Number 51 se chota hai..")
              else:
                st.info("Hint: Number 50 se bada Hai..")
        st.session_state.attempt_left -= 1

def start(ch):
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
      st.write("Ruko jara Sabar karo, Secret Number Sochne Do")
      st.session_state.select = random.randint(1,100)
      game()

def number_guessing_game():
  st.title("Number Guessing Game")
  st.write("Level 1 : Easy 10 attempts ::: Level 2 : Medium 7 attempt :::67 Level 3 : Hard 5 attempts")
  ch = st.radio("Choose Tum konsi level khelna chahate ho:", [1, 2, 3], format_func=lambda x: f"Level {x}")
  start(ch)

number_guessing_game()
