"""

An API sometimes fails due to network delays.
Write a program to retry the API call 3 times until the response code becomes 200.
If it still fails after 3 tries, print a failure message.
Hint: Use a while loop with a counter.
Expected Output Example:

Attempt 1: Response 500
Attempt 2: Response 200

✅ Test Passed
"""
i=1 
for i in range(1, 4, 1):
    res_code = int(input("Enter response code:"))
    print(f"Attempt {i}: response code {res_code}")
    if res_code == 200:
        print("\n✅ Test Passed")
        break
if res_code!=200:
    print("\n!!Test Failed!!")

