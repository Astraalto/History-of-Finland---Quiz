# Software Requirements Specification

## Purpose

Develop a command-line quiz game that tests the player's knowledge of Finnish history.

## Functional Requirements

- Display a welcome message.
- Present multiple-choice questions.
- Each question has four possible answers (A–D).
- Accept user input regardless of uppercase or lowercase.
- Validate user input.
- Inform the player whether the answer is correct.
- Keep track of the player's score.
- Display the final score.
- Display a short performance message based on the score.

## Non-functional Requirements

- Written in Python 3.
- Easy to understand and maintain.
- Modular source code.
- Runs from the command line.
- No external libraries required.

## Data

Questions are stored separately from the game logic to improve maintainability.

## Future Improvements

- Randomize question order.
- Add difficulty levels.
- Save high scores.
- Add a graphical user interface.