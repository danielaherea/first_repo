from Quiz import Quiz

quiz_questions = [
    "What is the test basis?\n(a) The point during software development when testing should start\n(b) The body of knowledge used for test analysis and design\n(c) The source to determine the actual results from a set of tests\n(d) The method used to systematically devise test conditions\n\n",
    "When the tester verifies the test basis while designing tests early in the lifecycle, which common test objective is being achieved?\n(a) Gaining confidence\n(b) Finding defects\n(c) Preventing defects\n(d) Providing information for decision making\n\n",
    "Which of the following is an example of debugging?\n(a) A tester finds a defect and reports it\n(b) A tester retests a fix from the developer and finds a regression\n(c) A developer finds and fixes a defect\n(d) A developer performs unit testing\n\n",
    "Usability testing is an example of which type of testing?\n(a) Functional\n(b) Non-functional\n(c) Structural\n(d) Change-related\n\n",
    "If test cases are derived from looking at the code, what type of test design technique is being used?\n(a) Black-box\n(b) White-box\n(c) Specification-based\n(d) Behavior-based\n\n"
]

quiz = [
    Quiz(quiz_questions[0],"b"),
    Quiz(quiz_questions[1],"c"),
    Quiz(quiz_questions[2],"c"),
    Quiz(quiz_questions[3],"b"),
    Quiz(quiz_questions[4],"b")
]

def my_quiz(quiz):
    score = 0
    for item in quiz:
        answer = input(item.question_prompt)
        if answer == item.question_answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(quiz)) + " correct!")
    if int(score) <= 3:
        print("You failed the test! :(")
    else:
        print("You passed the test! :)")

my_quiz(quiz)