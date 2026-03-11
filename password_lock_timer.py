import time

password = "python123"
attempts = 3

while attempts > 0:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Access granted")
        break
    else:
        attempts -= 1
        print("Wrong password")

        if attempts > 0:
            print("Try again in 5 seconds...")
            time.sleep(5)

if attempts == 0:
    print("Access denied. System locked.")
