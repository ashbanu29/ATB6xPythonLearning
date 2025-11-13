"""🧩 1️⃣ Write a Function to Check Test Case Status
Problem:
Write a function check_status(status_code) that returns:
"PASS" if status_code = 200
"FAIL" if status_code = 400 or 500
"UNKNOWN" otherwise
Example Input & Output:
print(check_status(200))   # PASS

print(check_status(500))   # FAIL

print(check_status(302))   # UNKNOWN
"""

def Check_Status(status_code):
    match status_code:
        case 200:
            print("PASS")
        case 400:
            print("FAIL")
        case 500:
            print("Fail")
        case _:
            print("UNKNOWN")

code = int(input("Enter response code:"))
Check_Status(code)




