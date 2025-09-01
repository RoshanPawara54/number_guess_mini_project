# number_guess_mini_project

# Number Guessing Game (Python)

A simple **Number Guessing Game** built in Python.  
The computer randomly selects a number, and the player tries to guess it within a limited number of attempts.

##  Features

-  Three difficulty levels:
  - **Easy (10 attempts)**
  - **Medium (7 attempts)**
  - **Hard (5 attempts)**
-  Provides hints if the guess is too high or too low
-  Runs directly in the terminal/command prompt


# Number Guessing Game (Streamlit)

An interactive **Number Guessing Game** built with **Streamlit**.  
Pick a difficulty level, make your guess, and see hints in real time.  
The game is deployed online and can be played on **mobile, desktop, or tablet**.  

 **Live Demo:** [Play Here](https://numberguessgame.streamlit.app/)


## 📸 Screenshot

![Number Guessing Game Screenshot](Screenshot%202025-09-01%20235536.png)

---

##  Features

-  **Three Difficulty Levels**
  - **Easy (10 attempts)**
  - **Medium (7 attempts)**
  - **Hard (5 attempts)**  
-  **Smart Hints**
  - Easy → hints when very close (within 5 or 20)
  - Medium → hints when within 5
  - Hard → hints only when attempts are few
-  **Responsive UI**  
  Works seamlessly on **mobile browsers** and desktops.
-  **Replay Support**  
  Restart or go back to Home anytime.

##  Project Structure

number_guess_mini_project/
│── number_guessing_game.py # Main Streamlit app (Home)
│── requirements.txt # Package dependencies
└── README.md # Project documentation


##  How to Run Locally

1. **Clone the repo**:
   ```bash
   git clone https://github.com/RoshanPawara54/number_guess_mini_project.git
   cd number_guess_mini_project
