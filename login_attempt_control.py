import time
import hashlib

# Login credentials
USERNAME = "admin"
PASSWORD = hashlib.sha256("admin123".encode()).hexdigest()

MAX_ATTEMPTS = 3
LOCK_TIME = 30

attempts = 0

print("===== LOGIN ATTEMPT CONTROL SYSTEM =====")

while True:

    username = input("\nEnter username: ")
    password = input("Enter password: ")

    # Check login credentials
    entered_password = hashlib.sha256(
        password.encode()
    ).hexdigest()

    if username == USERNAME and entered_password == PASSWORD:

        print("\nLogin Successful!")
        print("Welcome,", username)
        break

    else:
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts

        print("\nIncorrect username or password!")

        if attempts < MAX_ATTEMPTS:
            print("Remaining attempts:", remaining)

        # Lock account after 3 failed attempts
        if attempts == MAX_ATTEMPTS:

            print("\nToo many failed attempts!")
            print("Account temporarily locked.")

            print("Please wait", LOCK_TIME, "seconds.")

            time.sleep(LOCK_TIME)

            print("\nLock expired. You can try again.")

            attempts = 0