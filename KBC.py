def kbc_game():
    print("Welcome to Kaun banega crorepati game")
    print("Answer the question correctly to win a prize")
    print("Type 'exit' to quit the game")

    questions = [

        {
            "question": "What is programming language used in this game",
            "options": ["1.Java", "2.C++", "3.Python", "4.Javascript"],
            "answer": 3,
            "50-50": ["3.Python", "2.C++"]
        },
        {
            "question": "Which is national bird of India",
            "options": ["1.Pigeon", "2.Peacock", "3.Parrot", "4.Sparrow"],
            "answer": 2,
            "50-50": ["2.Peacock","1.Pigeon"]

        },
        {
            "question": "Which is national fruit of India",
            "options": ["1.Papaya", "2.Orange", "3.Grapes", "4.Mango"],
            "answer": 4,
            "50-50": ["4.Mango", "2.Orange"]

        }

    ]

    #Prize money
    prize_money = [1000, 2000, 3000]

    lifelines = {"50-50": False, "skip": False}

    for i, question in enumerate(questions):
        print(f"\n Question {i + 1}:{question['question']}")

        for option in question["options"]:
            print(option)

        print("\nLifelines available:")
        for lifeline, used in lifelines.items():
            if not used:
                print(f"- {lifeline}")

        # Get user input
        user_input = input("\nEnter your answer (1-4) or type a lifeline: ").strip().lower()

        # Handle exit
        if user_input == "exit":
            print(f"\nYou chose to exit. Your prize money is Rs. {prize_money[i - 1] if i > 0 else 0}.")
            break

        # Handle 50-50 lifeline
        if user_input == "50-50" and not lifelines["50-50"]:
            lifelines["50-50"] = True
            print("\nOptions after 50-50:")
            for opt in question["50-50"]:
                print(opt)
            user_input = input("\nEnter your answer (1-4): ").strip()

        # Handle skip lifeline
        if user_input == "skip" and not lifelines["skip"]:
            lifelines["skip"] = True
            print("You chose to skip this question. Moving to the next question.")
            continue

        # Validate and check the answer
        if user_input.isdigit() and int(user_input) == question["answer"]:
            print(f"Congrats!! You won Rs. {prize_money[i]}.")
        else:
            print(f"Your answer is wrong! The correct answer is {question['answer']}.")
            print(f"You leave with Rs. {prize_money[i - 1] if i > 0 else 0}.")
            break
    else:
        print(f"\nCongratulations! You have answered all questions correctly and won Rs. {prize_money[-1]}.")

kbc_game()