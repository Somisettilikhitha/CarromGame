import random
import math

# Constants
BOARD_SIZE = 8
HOLE_RADIUS = 1
STRIKER_RADIUS = 1
COIN_RADIUS = 0.5

class CarromBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def display(self):
        for row in self.board:
            print(' '.join(row))
        print()

class CarromGame:
    def __init__(self):
        self.board = CarromBoard()
        self.coins = []
        self.striker = None
        self.current_player = 1

    def initialize_coins(self):
        # Add black coins
        for _ in range(9):
            x = random.randint(1, BOARD_SIZE - 2)
            y = random.randint(1, BOARD_SIZE - 2)
            self.coins.append((x, y, "B"))

        # Add white coins
        for _ in range(9):
            x = random.randint(1, BOARD_SIZE - 2)
            y = random.randint(1, BOARD_SIZE - 2)
            self.coins.append((x, y, "W"))

    def initialize_striker(self):
        x = BOARD_SIZE // 2
        y = BOARD_SIZE - 2
        self.striker = (x, y)

    def place_piece(self, x, y, piece):
        self.board.board[x][y] = piece

    def is_valid_position(self, x, y):
        return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

    def is_empty_position(self, x, y):
        return self.board.board[x][y] == ' '

    def is_striker_position(self, x, y):
        return self.striker == (x, y)

    def is_coin_position(self, x, y):
        return (x, y) in self.coins

    def striker_strike(self, angle, force):
        x, y = self.striker
        rad_angle = math.radians(angle)
        new_x = x + int(force * math.cos(rad_angle))
        new_y = y + int(force * math.sin(rad_angle))

        if self.is_valid_position(new_x, new_y):
            if self.is_empty_position(new_x, new_y):
                self.striker = (new_x, new_y)
                return True
            elif self.is_coin_position(new_x, new_y):
                # Handle pocketed coin
                self.coins = [(cx, cy, c) for cx, cy, c in self.coins if (cx, cy) != (new_x, new_y)]
                return True

        return False

    def play(self):
        self.initialize_coins()
        self.initialize_striker()

        while len(self.coins) > 0:
            self.board.display()
            angle = int(input("Enter the angle (0-360): "))
            force = int(input("Enter the force (1-10): "))

            if self.striker_strike(angle, force):
                print("Strike successful.")
            else:
                print("Invalid strike. Try again.")

            # Switch players
            self.current_player = 1 if self.current_player == 2 else 2

        print("Game Over!")

if __name__ == "__main__":
    game = CarromGame()
    game.play()
