def get_input(prompt):
    while True:
        response = input(prompt).strip()
        if response:  # ensure not empty
            return response
        else:
            print("Input can't be empty. Please try again.")

def daily_prompts():
    print("=== Daily Prompt Input ===")
    date = get_input("Enter the date (YYYY-MM-DD): ")

    print("\n-- Morning Prompts --")
    morning_word = get_input("1. One word to describe how you want to feel today: ")
    print("2. Three small wins you aim for today:")
    wins = []
    for i in range(1, 4):
        win = get_input(f"   {i}) ")
        wins.append(win)
    avoiding = get_input("3. One thing you've been avoiding that you'll tackle today: ")

    print("\n-- Evening Prompts --")
    proud = get_input("1. What did you do today that you're proud of? ")
    made_better = get_input("2. Who or what made your day better? ")
    let_go = get_input("3. What’s something you'd like to let go of before tomorrow? ")

    # Store or print collected data
    print("\n=== Summary of Your Daily Prompts ===")
    print(f"Date: {date}")
    print(f"Morning - Feel word: {morning_word}")
    print("Morning - Small wins:")
    for idx, w in enumerate(wins, 1):
        print(f"  {idx}. {w}")
    print(f"Morning - Avoiding: {avoiding}")
    print(f"Evening - Proud of: {proud}")
    print(f"Evening - Made better by: {made_better}")
    print(f"Evening - Let go of: {let_go}")

if __name__ == "__main__":
    daily_prompts()
