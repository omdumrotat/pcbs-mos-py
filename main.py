import time
import random
import openai

# Initialize the OpenAI API with your API key
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

total = 1
money = 50

def generate_problem():
    response = client.chat.Completion.create(
      engine="model-identifier",
      prompt="Generate a PC problem and its correct response.",
      max_tokens=50
    )
    problem = response.choices[0].text.strip()
    return problem.split("\n")

print("Welcome to the PC Store! You are the manager of this company, and you need to earn 1000 Money in the shortest time possible.")
time.sleep(1)
print("Hints:\n Long loading = HDD\nSlow processing = CPU\nLow FPS = GPU\nBSOD = Hardware/Software/Virus issue\nAbrupt shutdown = Hardware (likely overheating)")

print("Your current money is " + str(money))
time.sleep(2)

while True:
    profit = random.randint(60, 170)
    loss = random.randint(30, 50)
    current_problem, correct_response = generate_problem()
    customer = random.randint(1, 100)

    if total <= 10:
        if money <= 0:
            print("Your company has gone bankrupt.")
            break
        elif money >= 1000:
            total -= 1
            print("You have succeeded with a total of " + str(total) + " questions.")
            break
        else:
            print("\nDay " + str(total))
            print(f"Customer {customer} encounters a problem with their PC; {current_problem}")

            response = input("Input your response (A, B, or C): ")

            if response.upper() == correct_response.upper():
                money += profit
                print("You have resolved the issue.")
            else:
                money -= loss
                print("You have not resolved the issue.")

            print("Your current money is " + str(money))
            total += 1
            time.sleep(2)
    else:
        print("You have not reached the goal in 10 days, so you must start over; your money has been reset to the initial amount.")
        time.sleep(2)
        money = 50
        total = 1
