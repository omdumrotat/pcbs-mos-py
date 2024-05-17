import time
import random
from openai import OpenAI

# Initialize the OpenAI API with your API key
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

total = 1
money = 50

def generate_problem():
    history = [{"role": "user", "content": "Generate a PC problem and its correct response. Example (use this format, do not add anything else.): \n\n**Problem**: my pc is experiencing an issue. \n\n**Options**:\n\nA) Option A\nB) Option B\nC) Option C\n\n**Correct Response:** A)"}]
    response = client.chat.completions.create(
        model="model-identifier",
        messages=history,
        max_tokens=100
    )
    content = response.choices[0].message.content.strip().split("\n")
    
    problem = ""
    options = []
    correct_response = ""
    
    try:
        # Find the problem line
        problem_line = next((line for line in content if line.startswith("**Problem:**")), None)
        if problem_line:
            problem = problem_line.split("**Problem:**")[1].strip()
        
        # Find the options lines
        options_start = content.index("**Options:**") + 1
        for i in range(options_start, len(content)):
            line = content[i].strip()
            if line.startswith(("A)", "B)", "C)")):
                options.append(line.split(" ", 1)[1].strip())
            if line.startswith("**Correct Response:**"):
                break
        
        # Find the correct response line
        correct_response_line = next((line for line in content if line.startswith("**Correct Response:**")), None)
        if correct_response_line:
            correct_response = correct_response_line.split("**Correct Response:**")[1].strip().split()[0].replace(")", "")
        
        # Ensure we have all necessary parts
        if not problem or not options or not correct_response:
            raise ValueError("Incomplete response format.")
        
        
        return problem, options, correct_response
    
    except (IndexError, ValueError) as e:
        print(f"Error parsing response: {e}")
        return "Error generating problem", ["Option A", "Option B", "Option C"], "A"

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
