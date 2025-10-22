"""
Q2
In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.
expected_title = "Dashboard"
actual_title = "Dashboard "
✅ Test Passed – Title matches
"""
#expected_title = "Dashboard"
#actual_title = "dashboard"
actual_title = input("Enter the actual title:")
expected_title = input("Enter the expected title:")

if expected_title.lower() == actual_title.strip().lower():
    print("Test Passed - The title matches.")
else:
    print("Test Failed - The title does not match.")