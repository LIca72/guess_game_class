import random

class GuessGame:
    def __init__(self):
        self.secret_number = random.randint(1, 10)
        self.attempts = 0
        self.max_attempts = 3
        self.status = "playing"

    def guess(self, number):
        self.attempts += 1
        if number == self.secret_number:
            self.status = "won"
            return True
        return False

    def run(self):
        while self.attempts < self.max_attempts:
            try:
                guess = int(input("🎯 Guess a number between 1 and 10: "))
                if self.guess(guess):
                    print("🎉 You guessed it!")
                    break
                else:
                    print("❌ Wrong guess. Try again.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        if self.status != "won":
            print(f"😢 No more attempts. The correct number was {self.secret_number}.")
