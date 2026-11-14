import random
# Function to roll a dice
def roll_dice():
    return random.randint(1, 6)
# Number of rolls
n = int(input("Enter the number of dice rolls: "))
# Dictionary to store frequency of each outcome
frequency = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
# Simulating dice rolls
print("\n--- Dice Rolling Results ---")
for i in range(n):
 result = roll_dice()
    print("Roll", i + 1, ":", result)
    frequency[result] += 1
# Displaying frequency
print("\n--- Frequency of Outcomes ---")
for number in range(1, 7):
    print(number, "appeared", frequency[number], "times")
# Calculating probability
print("\n--- Experimental Probability ---")
for number in range(1, 7):
    probability = (frequency[number] / n) * 100
    print(number, ":", round(probability, 2), "%")
