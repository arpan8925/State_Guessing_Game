# State Guessing Game

This project is a simple state guessing game implemented in Python using the `turtle` and `pandas` libraries. The game displays a blank map of the United States and prompts the user to guess the names of the states. As the user correctly guesses the states, their names are written on the map in their corresponding locations.

## Features

-   Interactive gameplay using the `turtle` module for graphics and user input.
-   Uses `pandas` to read state data (name, x, y coordinates) from a CSV file (`50_states.csv`).
-   Keeps track of the user's score and displays it in the window title.
-   Provides an option to exit the game by typing "exit".
-   Congratulates the user upon correctly guessing all the states.

## Files

-   `50_states.csv`: Contains the state names and their corresponding x and y coordinates on the map.
-   `main.py`: The main Python script containing the game logic.
-   `README.md`: Provides an overview of the project.

## How to Play

1.  Make sure you have Python installed on your system.
2.  Install the `turtle` and `pandas` libraries:

    ```bash
    pip install turtle pandas
    ```
3.  Download the repository, including the `50_states.csv` file and `blank_states_img.gif` (you will need to find a suitable gif image and place it in the same directory as the python script).
4.  Run the `main.py` script:

```bash
python main.py
```

5.  A window will appear with a blank map of the United States.
6.  Enter the name of a state in the input prompt and press Enter.
7.  If the state is correct, its name will appear on the map in the correct location, and your score will be updated.
8.  Continue guessing states until you have guessed all 50, or type "exit" to quit the game.

## Code Explanation

### `main.py`

-   Imports the necessary modules: `turtle` for graphics and `pandas` for data manipulation.
-   Reads the state data from the `50_states.csv` file into a pandas DataFrame.
-   Sets up the game screen and background image.
-   Defines a function `state_selector` to write the state names on the map.
-   Implements the main game loop, which prompts the user for state names, checks if the guess is correct, and updates the score.

### `50_states.csv`

-   A CSV file containing the names of the 50 US states and their corresponding x and y coordinates on the map.

## Improvements

-   Add a list of the states already guessed
-   Keep track of the states missed and provide a way to learn them at the end of the game.
-   Implement a graphical user interface (GUI) for a better user experience.