import os

# Encrypt using ROT3 (shift every character forward by 3)
def rot3_encrypt(text):
    return "".join([chr((ord(char) + 3) % 256) for char in text])

# Decrypt using ROT3 (shift every character backward by 3)
def rot3_decrypt(text):
    return "".join([chr((ord(char) - 3) % 256) for char in text])

# Ensure credentials.txt exists with a header
def ensure_file_exists():
    if not os.path.exists("credentials.txt") or os.path.getsize("credentials.txt") == 0:
        with open("credentials.txt", "w") as file:
            file.write("Website,Username,Password\n")  # Header line

# Save encrypted credentials to file
def save_credentials():
    url = input("Enter website/application URL: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    encrypted_url = rot3_encrypt(url)
    encrypted_username = rot3_encrypt(username)
    encrypted_password = rot3_encrypt(password)

    with open("credentials.txt", "a") as file:
        file.write(f"{encrypted_url},{encrypted_username},{encrypted_password}\n")

    print("Encrypted credentials saved to credentials.txt\n")

# View decrypted credentials from file (in a row format)
def view_credentials():
    if not os.path.exists("credentials.txt"):
        print("No credentials file found.\n")
        return

    with open("credentials.txt", "r") as file:
        lines = file.readlines()

    if len(lines) <= 1:
        print("No saved credentials.\n")
        return

    print("\nSaved Credentials:")
    print("-" * 70)
    print("{:<25} {:<20} {:<20}".format("Website", "Username", "Password"))
    print("-" * 70)

    for line in lines[1:]:  # Skip header
        encrypted_url, encrypted_username, encrypted_password = line.strip().split(",")

        url = rot3_decrypt(encrypted_url)
        username = rot3_decrypt(encrypted_username)
        password = rot3_decrypt(encrypted_password)

        print("{:<25} {:<20} {:<20}".format(url, username, password))

# Main program loop
def main():
    ensure_file_exists()

    while True:
        print("\nChoose an option:")
        print("1. Save login credentials")
        print("2. View saved credentials")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            save_credentials()
        elif choice == "2":
            view_credentials()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()