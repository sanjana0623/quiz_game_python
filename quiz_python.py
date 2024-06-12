#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")

    def get_user_answer(self):
        user_answer = input("Enter your answer (1-4): ")
        return int(user_answer) - 1

    def check_answer(self, question, user_answer):
        correct_option = question['options'].index(question['answer'])
        if user_answer == correct_option:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}")

    def provide_feedback(self, question, user_answer):
        correct_option = question['options'].index(question['answer'])
        if user_answer == correct_option:
            print("Well done! You got it right.")
        else:
            print("Oops! Better luck next time.")
            print(f"The correct answer is: {question['answer']}")

    def play_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            self.display_question(question)
            user_answer = self.get_user_answer()
            self.check_answer(question, user_answer)
            choice = input("Would you like to view feedback for this question? (yes/no): ").lower()
            if choice == 'yes':
                self.provide_feedback(question, user_answer)
            print()  
        print(f"Your final score is: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    questions = [
        {
            'question': "What is the capital of France?",
            'options': ["Paris", "London", "Berlin", "Rome"],
            'answer': "Paris"
        },
        {
            'question': "What is 2+2?",
            'options': ["3", "4", "5", "6"],
            'answer': "4"
        },
        {
            'question': "Which planet is known as the Red Planet?",
            'options': ["Mars", "Venus", "Jupiter", "Mercury"],
            'answer': "Mars"
        },
        {
            'question': "Who wrote 'Romeo and Juliet'?",
            'options': ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"],
            'answer': "William Shakespeare"
        },
        {
            'question': "What is the largest mammal?",
            'options': ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            'answer': "Blue Whale"
        },
        {
            'question': "What is the tallest mountain in the world?",
            'options': ["Mount Everest", "K2", "Kangchenjunga", "Makalu"],
            'answer': "Mount Everest"
        },
        {
            'question': "Who painted the Mona Lisa?",
            'options': ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"],
            'answer': "Leonardo da Vinci"
        }
    ]
    quiz = Quiz(questions)
    quiz.play_quiz()


# This quiz game reinforces Python fundamentals:
# 
# Data Structures: The quiz game relies on dictionaries to store each question, which includes the question text, options, and correct answer. This demonstrates the usage of dictionaries as a flexible data structure for organizing related data.
# 
# Control Flow: The game utilizes control flow constructs such as loops (for looping through questions), conditionals (for checking user answers), and function calls (for providing feedback and displaying the final score). This reinforces the concept of controlling the flow of program execution based on conditions and iterative processes.
# 
# User Input Handling: The game interacts with the user by accepting input for answering questions and for choosing whether to view feedback. It handles user input using the input() function and converts it to the appropriate data type (integer) for further processing. This demonstrates how Python handles user input and converts it into usable data.

# In[ ]:




