def main():
    # Welcome to the game print statement
    print("Welcome to my computer quiz!")

    # User input to check whether he/she wants to play the game or not
    playing = input("Do you want to play? ").strip().lower()

    # Check the user input
    if playing != "yes":
        quit()
    
    play_game()

    
def play_game():
    print("Okay! Let's play the game :)")

    # full forms dictionary
    full_forms = {
        "CPU": "central processing unit",
        "GPU": "graphics processing unit",
        "RAM": "random access memory",
        "PSU": "power supply"
    }

    # correct and incorrect questions variables
    correct = 0
    incorrect = 0

    correct, incorrect = check_user_answer(correct, incorrect, full_forms)
    print(f"Correct questions: {correct}, \nIncorrect Questions: {incorrect}")

def check_user_answer(correct, incorrect, full_forms):
    # Looping through each key and its full form
    for key, val in full_forms.items():
        answer = input(f"What does {key} stand for? ").lower()

        # If answer is correct increase the correct variable value
        if answer == val:
            correct += 1
        # If answer is incorrect increase the incorrect variable value
        else:
            incorrect += 1
    return (correct, incorrect)

if __name__ == "__main__":
    main()