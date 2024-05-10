import time
import random

total = 1
money = 50

problems = [
    {
        "problem": "PC takes a long time to load content; how will you solve the problem?\n A: Replace CPU brand XYZ model 123\n B: Replace hard drive PFJ\n C: Replace GPU brand QHF\n Input:\n",
        "correct_response": "B",
        "answered": 0,
    },
    {
        "problem": "Their PC is slow in handling basic tasks; how will you solve the problem?\n A: Replace CPU Ontel Celery brand\n B: Replace RAM DDR2 Kingon\n C: Replace PSU QNV\n Input:\n",
        "correct_response": "A",
        "answered": 0,
    },
    {
        "problem": "Their keyboard is not working even though it's newly bought; how will you solve the problem?\n A: Install the latest drivers\n B: CPU is faulty, must replace it!\n C: Add 128MB RAM to increase performance 1000 times\n Input:\n",
        "correct_response": "A",
        "answered": 0,
    },
    {
        "problem": "Their computer monitor displays distorted colors and objects when they run deep graphics applications. How will you solve the problem?\n A: Reinstall GPU driver\n B: Replace PSU\n C: Replace RAM\n Input:\n",
        "correct_response": "A",
        "answered": 0,
    },
    {
        "problem": "Their computer often shows a Blue Screen of Death (BSOD) error. How will you solve the problem?\n A: Disk fragmentation too high\n B: Replace PSU\n C: Reinstall OS\n Input:\n",
        "correct_response": "C",
        "answered": 0,
    },
    {
        "problem": "Their computer is infected with malware encrypting your files and demanding ransom to release them. What type of malware is this?\n A: Trojan Horse\n B: Spyware\n C: Ransomware\n Input:\n",
        "correct_response": "C",
        "answered": 0,
    },
    {
        "problem": "They want to switch OS to Linux but lack experience in installation; how will you solve the problem?\n A: Upgrade to the latest CPU\n B: Install Linux\n C: Replace 20-inch TFT monitor\n Input:\n",
        "correct_response": "B",
        "answered": 0,
    },
    {
        "problem": "They want the highest current PC configuration but lack experience in assembling; how will you solve the problem?\n A: A PC with the highest current configuration\n B: The current PC is still usable\n Input:\n",
        "correct_response": "A",
        "answered": 0,
    },
    {
        "problem": "Their PC shuts down abruptly during heavy tasks; how will you solve the problem?\n A: Replace 120MB RAM\n B: Apply new thermal paste to CPU heatsink\n C: Replace hard drive\n Input:\n",
        "correct_response": "B",
        "answered": 0,
    },
    {
        "problem": "They are undecided between 2 CPUs at the same price (AND Athln 32 and Ontel 586) knowing that the first CPU performs better than the second; how will you solve the problem?\n A: Ontel 586 is the best choice because of the brand\n B: AND Athln 32 will provide the best performance in the price range\n",
        "correct_response": "B",
        "answered": 0,
    },
]

print("Welcome to the PC Store! You are the manager of this company, and you need to earn 1000 Money in the shortest time possible.")
time.sleep(1)
print("Hints:\n Long loading = HDD\nSlow processing = CPU\nLow FPS = GPU\nBSOD = Hardware/Software/Virus issue\nAbrupt shutdown = Hardware (likely overheating)")

print("Your current money is " + str(money))
time.sleep(2)

while True:
    profit = random.randint(60, 170)
    loss = random.randint(30, 50)
    current_problem = random.choice(problems)
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
            response = input("Customer " + str(customer) + " encounters a problem with their PC; " + current_problem["problem"])

            if response.upper() == current_problem["correct_response"]:
                money += profit
                print("You have resolved the issue.")
            else:
                money -= loss
                print("You have not resolved the issue.")

            print("Your current money is " + str(money))
            total += 1
            problems.remove(current_problem)
            time.sleep(2)
    else:
        print("You have not reached the goal in 10 days, so you must start over; your money has been reset to the initial amount.")
        time.sleep(2)
        money = 50
        total = 1
        problems = [
            {
                "problem": "PC takes a long time to load content; how will you solve the problem?\n A: Replace CPU brand XYZ model 123\n B: Replace hard drive PFJ\n C: Replace GPU brand QHF\n Input:\n",
                "correct_response": "B",
                "answered": 0,
            },
            {
                "problem": "Their PC is slow in handling basic tasks; how will you solve the problem?\n A: Replace CPU Ontel Celery brand\n B: Replace RAM DDR2 Kingon\n C: Replace PSU QNV\n Input:\n",
                "correct_response": "A",
                "answered": 0,
            },
            {
                "problem": "Their keyboard is not working even though it's newly bought; how will you solve the problem?\n A: Install the latest drivers\n B: CPU is faulty, must replace it!\n C: Add 128MB RAM to increase performance 1000 times\n Input:\n",
                "correct_response": "A",
                "answered": 0,
            },
            {
                "problem": "Their computer monitor displays distorted colors and objects when they run deep graphics applications. How will you solve the problem?\n A: Reinstall GPU driver\n B: Replace PSU\n C: Replace RAM\n Input:\n",
                "correct_response": "A",
                "answered": 0,
            },
            {
                "problem": "Their computer often shows a Blue Screen of Death (BSOD) error. How will you solve the problem?\n A: Disk fragmentation too high\n B: Replace PSU\n C: Reinstall OS\n Input:\n",
                "correct_response": "C",
                "answered": 0,
            },
            {
                "problem": "Their computer is infected with malware encrypting your files and demanding ransom to release them. What type of malware is this?\n A: Trojan Horse\n B: Spyware\n C: Ransomware\n Input:\n",
                "correct_response": "C",
                "answered": 0,
            },
            {
                "problem": "They want to switch OS to Linux but lack experience in installation; how will you solve the problem?\n A: Upgrade to the latest CPU\n B: Install Linux\n C: Replace 20-inch TFT monitor\n Input:\n",
                "correct_response": "B",
                "answered": 0,
            },
            {
                "problem": "They want the highest current PC configuration but lack experience in assembling; how will you solve the problem?\n A: A PC with the highest current configuration\n B: The current PC is still usable\n Input:\n",
                "correct_response": "A",
                "answered": 0,
            },
            {
                "problem": "Their PC shuts down abruptly during heavy tasks; how will you solve the problem?\n A: Replace 120MB RAM\n B: Apply new thermal paste to CPU heatsink\n C: Replace hard drive\n Input:\n",
                "correct_response": "B",
                "answered": 0,
            },
            {
                "problem": "They are undecided between 2 CPUs at the same price (AND Athln 32 and Ontel 586) knowing that the first CPU performs better than the second; how will you solve the problem?\n A: Ontel 586 is the best choice because of the brand\n B: AND Athln 32 will provide the best performance in the price range\n",
                "correct_response": "B",
                "answered": 0,
            },
        ]
