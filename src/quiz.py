import random
from questions import questions

class Quiz:

    def __init__(self):
        self.score = 0

    def play(self):

        print("=" * 40)
        print("FINLAND HISTORY QUIZ")
        print("=" * 40)

        # Randomly choose 5 questions
        selected_questions = random.sample(questions, 5)

        for i, q in enumerate(selected_questions, start=1):

            print(f"\nQuestion {i}/{len(selected_questions)}")
            print(q["question"])

            for letter, option in q["options"].items():
                print(f"{letter}. {option}")

            answer = input("Your answer: ").upper()

            while answer not in ["A", "B", "C", "D"]:
                answer = input("Please enter A, B, C or D: ").upper()

            if answer == q["answer"]:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! Correct answer: {q['answer']}")

        print("\nQuiz finished!")
        print(f"Score: {self.score}/{len(selected_questions)}")

        percentage = self.score / len(selected_questions) * 100

        if percentage == 100:
            print("Excellent!")
        elif percentage >= 75:
            print("Very good!")
        elif percentage >= 50:
            print("Good effort!")
        else:
            print("Keep studying Finnish history!")