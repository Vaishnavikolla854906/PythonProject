import random
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Quiz Questions (Database)
# -------------------------------
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used for Python?",
        "options": ["A. Programming", "B. Markup", "C. Styling", "D. Database"],
        "answer": "A"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    },
    {
        "question": "Which module is used for data analysis?",
        "options": ["A. random", "B. pandas", "C. math", "D. os"],
        "answer": "B"
    },
    {
        "question": "Which module is used for graphs?",
        "options": ["A. matplotlib", "B. random", "C. sys", "D. time"],
        "answer": "A"
    }
]

# -------------------------------
# Initialize Variables
# -------------------------------
score = 0
results = []
user_answers = []

print("===== QUIZ ASSESSMENT SYSTEM =====\n")

# Shuffle questions
random.shuffle(questions)

# -------------------------------
# Quiz Execution
# -------------------------------
for i, q in enumerate(questions):
    print(f"Question {i+1}: {q['question']}")

    for opt in q["options"]:
        print(opt)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    user_answers.append(user_answer)

    # Check answer
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
        results.append(1)
    else:
        print(f"Wrong! Correct answer is {q['answer']}\n")
        results.append(0)

# -------------------------------
# Result Calculation
# -------------------------------
total = len(questions)
percentage = (score / total) * 100

print("\n===== RESULT =====")
print(f"Score: {score}/{total}")
print(f"Percentage: {percentage:.2f}%")

# Performance grading
if percentage >= 75:
    performance = "Excellent"
elif percentage >= 50:
    performance = "Good"
else:
    performance = "Needs Improvement"

print("Performance:", performance)

# -------------------------------
# Data Analysis using Pandas
# -------------------------------
data = {
    "Question_No": list(range(1, total + 1)),
    "User_Answer": user_answers,
    "Result": results
}

df = pd.DataFrame(data)

print("\n===== PERFORMANCE ANALYSIS =====")
print(df)

# Accuracy calculation
accuracy = (sum(results) / total) * 100
print(f"\nAccuracy: {accuracy:.2f}%")

# -------------------------------
# Visualization using Matplotlib
# -------------------------------
correct = results.count(1)
wrong = results.count(0)

labels = ['Correct', 'Wrong']
values = [correct, wrong]

plt.bar(labels, values)
plt.title("Quiz Performance Analysis")
plt.xlabel("Result Type")
plt.ylabel("Number of Questions")
plt.show()
