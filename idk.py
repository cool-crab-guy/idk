import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    # Text colors
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"

    print(f"{CYAN}✨ Welcome to the Ultimate Guessing Game! ✨{RESET}")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            prompt = f"\n{YELLOW}➔ Enter your guess: {RESET}"
            guess = int(input(prompt))
            attempts += 1

            if guess < secret_number:
                print(f"{RED}📉 Too low! Try again.{RESET}")
            elif guess > secret_number:
                print(f"{RED}📈 Too high! Try again.{RESET}")
            else:
                print(f"\n{GREEN}🎉 BULLSEYE! You found it in {attempts} attempts!{RESET}")
                break
        except ValueError:
            print(f"{RED}❌ Oops! Please enter a valid whole number.{RESET}")

if __name__ == "__main__":
    play_game()
