test_type = int(input("enter the test type you are running, API, UI, Web"))

match  test_type:
    case 1:
        print("You are running api testing")
    case 2:
        print("You are running web testing")
    case 3:
        print("You are running web UI")
    case _:
        print("Invalid input")