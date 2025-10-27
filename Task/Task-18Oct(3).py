"""
Question 3 :
Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.
Hint: Use a counter (like wait_time) and break condition.
"""

wait_time = 0
page_loaded = False

while wait_time < 5:
    user_input = input("Has the page loaded? (yes/no): ")

    if user_input.lower() == "yes":
        page_loaded = True
        print("Page loaded successfully!")
        break

    wait_time += 1

if not page_loaded:
    print("Timeout! Page did not load within 5 attempts.")