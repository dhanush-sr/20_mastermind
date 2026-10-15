import random
from logic import feedback


class Mastermind:
    def __init__(self):
        self.code = [str(random.randint(1, 6)) for _ in range(4)]
        self.history = []
        self.max_turns = 10
        self.over = False
        self.won = False

    @property
    def turns_left(self):
        return self.max_turns - len(self.history)

    def guess(self, guess):
        if self.over:
            raise RuntimeError("The game is over; no more guesses are accepted.")
        exact, partial = feedback(self.code, guess)
        self.history.append((guess, exact, partial))
        if exact == len(self.code):
            self.over = self.won = True
        elif self.turns_left == 0:
            self.over = True
        return exact, partial

    def run(self):
        print("Mastermind — enter four digits from 1 to 6. Type q to quit.")
        while not self.over:
            raw = input(f"{self.turns_left} turns left > ").strip()
            if raw.lower() == "q":
                self.over = True
                print("You quit. The code was", "".join(self.code))
                return
            if len(raw) != 4 or any(ch not in "123456" for ch in raw):
                print("Enter exactly four digits from 1 to 6.")
                continue
            exact, partial = self.guess(raw)
            print("Exact:", exact, " Partial:", partial)
        if self.won:
            print(f"You win! Cracked the code in {len(self.history)} guesses.")
        else:
            print("You lose! Out of guesses. The code was", "".join(self.code))
