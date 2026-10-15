import random
from logic import feedback

# name: (code length, highest symbol, allowed guesses)
DIFFICULTIES = {
    "easy": (3, 4, 12),
    "normal": (4, 6, 10),
    "hard": (5, 8, 8),
}


class Mastermind:
    def __init__(self, difficulty="normal"):
        self.length, self.max_symbol, self.max_turns = DIFFICULTIES[difficulty]
        self.symbols = "".join(str(n) for n in range(1, self.max_symbol + 1))
        self.code = [random.choice(self.symbols) for _ in range(self.length)]
        self.history = []
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
        print(f"Mastermind — enter {self.length} digits from 1 to {self.max_symbol}. Type q to quit.")
        while not self.over:
            raw = input(f"{self.turns_left} turns left > ").strip()
            if raw.lower() == "q":
                self.over = True
                print("You quit. The code was", "".join(self.code))
                return
            if len(raw) != self.length or any(ch not in self.symbols for ch in raw):
                print(f"Enter exactly {self.length} digits from 1 to {self.max_symbol}.")
                continue
            exact, partial = self.guess(raw)
            print("Exact:", exact, " Partial:", partial)
        if self.won:
            print(f"You win! Cracked the code in {len(self.history)} guesses.")
        else:
            print("You lose! Out of guesses. The code was", "".join(self.code))
