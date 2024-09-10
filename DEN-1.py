# This is the first task of the internship at Digital Empowerment Pakistan
# I have made a Red-Blue nim game, that works with two players (but I have implemented Player vs Computer)
# I have used MinMax and Alpha Beta Pruning to choose the best move for the computer.
# All of the work is done in the class "NimGame", with its instance created in main.


class NimGame:
    def __init__(self, red, blue, version="standard", first_player="human"):
        self.red = red  
        self.blue = blue  
        self.version = version  
        self.current_player = first_player 

    def is_game_over(self):
        return self.red == 0 and self.blue == 0

    def display_state(self):
        print(f"Red marbles: {self.red}, Blue marbles: {self.blue}")

    def human_move(self):
        while True:
            choice = input("Choose pile (red/blue): ").lower()
            if choice == "red" and self.red > 0:
                amount = int(input(f"How many red marbles to remove (1-{self.red})? "))
                if 1 <= amount <= self.red:
                    self.red -= amount
                    break
            elif choice == "blue" and self.blue > 0:
                amount = int(input(f"How many blue marbles to remove (1-{self.blue})? "))
                if 1 <= amount <= self.blue:
                    self.blue -= amount
                    break
            print("Invalid move. Try again.")

    def computer_move(self):
        _, move = self.minmax(self.red, self.blue, True, float("-inf"), float("inf"))
        pile, amount = move
        if pile == "red":
            print(f"Computer removes {amount} red marbles.")
            self.red -= amount
        else:
            print(f"Computer removes {amount} blue marbles.")
            self.blue -= amount

    def minmax(self, red, blue, is_computer, alpha, beta):
        if red == 0 and blue == 0:
            if self.version == "standard":
                return (-1 if is_computer else 1), None  # Lose for current player
            else:
                return (1 if is_computer else -1), None  # Win for current player

        best_move = None
        if is_computer:
            max_eval = float("-inf")
            for move in self.get_valid_moves(red, blue):
                new_red, new_blue = self.apply_move(red, blue, move)
                eval, _ = self.minmax(new_red, new_blue, False, alpha, beta)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float("inf")
            for move in self.get_valid_moves(red, blue):
                new_red, new_blue = self.apply_move(red, blue, move)
                eval, _ = self.minmax(new_red, new_blue, True, alpha, beta)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def get_valid_moves(self, red, blue):
        moves = []
        for i in range(1, red + 1):
            moves.append(("red", i))
        for i in range(1, blue + 1):
            moves.append(("blue", i))
        return moves

    def apply_move(self, red, blue, move):
        pile, amount = move
        if pile == "red":
            return red - amount, blue
        else:
            return red, blue - amount

    def play_game(self):
        while not self.is_game_over():
            self.display_state()
            if self.current_player == "human":
                self.human_move()
                self.current_player = "computer"
            else:
                self.computer_move()
                self.current_player = "human"

        self.display_state()
        print("Game Over!")
        if self.is_game_over():
            if self.version == "standard":
                if self.current_player == "human":
                    print("Computer wins!")
                else:
                    print("Human wins!")
            else:
                if self.current_player == "human":
                    print("Human wins!")
                else:
                    print("Computer wins!")

def mode(ver):
    return "standard" if ver == 1 else "misere"

while True:
    print("Welcome! Which game do you want to play? (Press 1 or 2)\n1. Standard\n2. Misere")
    style = int(input())
    game = NimGame(red=5, blue=4, version=mode(style), first_player="human")
    game.play_game()
    print("Want to play more? (y or n)")
    again = input()
    if again.lower() == 'n':
        break
