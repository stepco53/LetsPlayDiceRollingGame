# Dice Rolling Game
import random


def roll_dice():
    return random.randint(1, 6)


def main():
    rolls = []
    while True:
        user_input = (
            input("Press 'r' to roll the dice or 'n' to exit: ").strip().lower()
        )
        if user_input == "r":
            roll = roll_dice()
            rolls.append(roll)
            print(f"You rolled a {roll}.")
        elif user_input == "n":
            if rolls:
                total_rolls = len(rolls)
                average_roll = sum(rolls) / total_rolls
                print(
                    f"Total rolls: {total_rolls}, Average roll value: {average_roll:.2f}"
                )

                # Count frequency of each roll
                frequency = {i: rolls.count(i) for i in range(1, 7)}
                sorted_frequency = sorted(
                    frequency.items(), key=lambda x: x[1], reverse=True
                )

                print("Roll frequencies (most to least frequent):")
                for value, count in sorted_frequency:
                    print(f"{value}: {count} times")
            else:
                print("No rolls were made.")
            break
        else:
            print("Invalid input. Please press 'r' to roll or 'n' to exit.")


if __name__ == "__main__":
    main()
