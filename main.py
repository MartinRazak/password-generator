from storage import load_data, save_data
from manager import generate_password, check_strength


data = load_data()

while True:
    menu_choice = input('''
Welcome to the password manager: 
    
1. Generate new password
2. Retrieve password
3. Delete a password by service name
4. Update password
5. List all services
6. Exit
    
Please select an option: ''')

    if menu_choice == '1':
        service = input("Enter your service: ")

        if service in data:
            print("You already have a password for this service")
        else:
            data[service] = generate_password(12)
            print("Password generated successfully!")

        save_data(data)

    elif menu_choice == '2':
        service = input("Enter your service: ")

        if service in data:
            password = data[service]
            strength = check_strength(password)

            print(f"Your password for {service}: {password}")
            print(f"Password strength: {strength}")
        else:
            print(f"You do not have any password associated with {service}")

    elif menu_choice == '3':
        service = input("Enter your service: ")

        if service in data:
            confirm = input(f"Are you sure you want to delete your password for {service} (y/n): ").lower()

            if confirm == 'y':
                del data[service]
                save_data(data)
                print("Password successfully deleted!")

            elif confirm == 'n':
                pass

        else:
            print("service not found")

    elif menu_choice == '4':
        service = input("Enter the service you want to update the password from: ")

        if service in data:
            del data[service]
            data[service] = generate_password(12)
            save_data(data)
            print("Password successfully updated!")
        else:
            print("You do not have a password saved for this service")

    elif menu_choice == '5':
        if data:
            print("\nSaved services:")
            for service in data:
                print(f"- {service}")
        else:
            print("No services saved yet.")

    elif menu_choice == '6':
        break

    else:
        print("Please enter a number in the list")
