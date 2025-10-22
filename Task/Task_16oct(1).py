"""
Q - You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not.

I/P response = 404 , O/P ❌ Failed API Request
I/P response = 200 , O/P ✅ Passed API Request
"""

Api_response = int(input("Enter the response code from your test script. "))
if Api_response == 200:
    print("The API response is successful.✅", 200, "Ok")
elif Api_response == 404:
    print("API response is failed ❌.", 404)
else:
    print("Enter a valid response code from your test script.") # this will handle the invalid input