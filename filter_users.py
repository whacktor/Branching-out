import json                                                                                                             #import json-data




def filter_users_by_name(name):                                                                                         #function to filter users by their name
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)




def filter_users_by_age(age):                                                                                           #function to filter users by their age
    with open ("users.json", "r") as file:
        users = json.load(file)

    age_filtered_users = [user for user in users if user["age"] == age]

    for user in age_filtered_users:
        print(user)




def filter_users_by_email(email):                                                                                       #function to filter users by their email
    with open("users.json", "r") as file:
        users = json.load(file)

    email_filtered_users = [user for user in users if user["email"] == email]

    for user in email_filtered_users:
        print(user)




if __name__ == "__main__":                                                                                              #main-function to seperate filter_options
    filter_option = input("What would you like to filter by? (Currently, name, age and emails are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: ").strip())
        filter_users_by_age(age_to_search)
    elif filter_option =="email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
