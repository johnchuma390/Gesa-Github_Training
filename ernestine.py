# Simple Student Marks Comment Program
# Author: John Chuma

def student_comment():
    marks = int(input("Enter the student's marks (0-100): "))

    if marks >= 80:
        print("🌟 Excellent work! Keep it up.")
    elif marks >= 60:
        print("👍 Good job, but there is room for improvement.")
    elif marks >= 40:
        print("🙂 Fair effort, try to work harder next time.")
    else:
        print("⚠️ Needs a lot of improvement. Don’t give up!")

# Run the program
if __name__ == "__main__":
    student_comment()
