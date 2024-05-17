import time
import random
from openai import OpenAI

# Initialize the OpenAI API with your API key
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

total = 1
money = 50

def generate_problem():
    history = [{"role": "user", "content": "Generate a PC problem and its correct response. Example (A is the right answer): my pc is experiencing an issue. A. Option A B. Option B C. Option C A"}]
    response = client.chat.completions.create(
      model="model-identifier",
      messages=history,
      max_tokens=100
    )
    content = response.choices[0].message.content.strip().split("\n")
    problem = content[0]
    options = [option.strip() for option in content[1:] if option.strip()]
    correct_response = options[-1].split()[-1]  # Extract the correct response (last word after splitting by space)
    return problem, options, correct_response


print("Welcome to the PC Store! You are the manager of this company, and you need to earn 1000 Money in the shortest time possible.")
time.sleep(1)
print("Hints:\n Long loading = HDD\nSlow processing = CPU\nLow FPS = GPU\nBSOD = Hardware/Software/Virus issue\nAbrupt shutdown = Hardware (likely overheating)")

print("Your current money is " + str(money))
time.sleep(2)

while True:
    profit = random.randint(60, 170)
    loss = random.randint(30, 50)
    current_problem, options, correct_response = generate_problem()
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
            print("Options:")
            for i, option in enumerate(options):
                print(f"{chr(65 + i)}. {option}")

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
