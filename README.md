# Word Guessing Game in Python

## Overview

This project is a Python-based word guessing game designed for learning purposes. The game challenges players to guess a hidden word by suggesting letters within a certain number of guesses. It provides an engaging way to practice Python programming concepts such as loops, conditionals, and object-oriented programming.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Game Mechanics](#game-mechanics)
5. [Attributes](#attributes)
6. [Contributing](#contributing)
7. [License](#license)

## Features

- **Random Word Selection**: A random word is chosen from a predefined list for each game.
- **Guess Tracking**: Tracks the number of missed letters and total guesses.
- **Game Status**: Displays the current status of the game, including the word with correctly guessed letters.
- **Score Calculation**: Calculates the total score based on game performance.
- **Frequency Analysis**: Analyzes the frequency of guessed letters and words.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/gursimran2407/word-guessing-game.git
    cd word-guessing-game
    ```

2. **Install dependencies**:
    - This project does not have any external dependencies. Ensure you have Python installed on your system.

3. **Run the game**:
    ```sh
    python game.py
    ```

## Usage

1. **Start a new game**:
    - Run `game.py` to start a new game.
    - A random word will be selected, and you will be prompted to guess letters.

2. **Gameplay**:
    - Enter a letter to guess.
    - The game will display the current state of the word, the number of missed letters, and the letters you have already guessed.
    - Continue guessing letters until you either guess the word correctly or reach the maximum number of allowed missed guesses.

3. **End game**:
    - The game ends when the word is guessed correctly or the maximum number of missed guesses is reached.
    - The total score and game statistics will be displayed.

## Game Mechanics

- **Random Word Selection**: A random word is selected from a list for each game.
- **Display Word**: The word to be guessed is displayed with underscores representing unguessed letters.
- **Missed Letters**: Tracks the number of incorrect guesses.
- **Game Status**: Indicates whether the game is ongoing, won, or lost.
- **End Game**: A flag indicating if the game has ended.
- **Total Score**: The final score based on game performance.
- **Frequency Analysis**: Tracks the frequency of each guessed letter and the overall frequency of words.

## Attributes

- **random_word**: The word selected for the game.
- **game_Obj**: The `game.py` object list.
- **tuple_word**: The word to be displayed on the screen with correctly guessed letters.
- **missed_letters**: The number of missed letters.
- **game_count**: The number of games played.
- **status**: The current status of the game.
- **end_game**: A flag indicating if the game has ended.
- **total_score**: The final score of the game.
- **frequency_words**: The frequency of words guessed in the game.
- **number_of_times_letter_requested**: The number of times each letter was requested.

## Contributing

1. **Fork the repository**:
    Click the 'Fork' button on the top right corner of this page.

2. **Create a new branch**:
    ```sh
    git checkout -b feature-branch
    ```

3. **Make your changes**:
    - Ensure your code follows the project's coding standards.
    - Include appropriate tests.

4. **Commit your changes**:
    ```sh
    git commit -m "Description of your changes"
    ```

5. **Push to your branch**:
    ```sh
    git push origin feature-branch
    ```

6. **Create a Pull Request**:
    Submit your pull request from your fork's branch to the main repository's `master` branch.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
