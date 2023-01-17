import gspread
from google.oauth2.service_account import Credentials
import pandas as pd


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('movie_reviews')


def initial_choice():
    """
    Allows user to input review or view past reviews
    """
    print("Would you like to input a review or view past reviews")
    print("Press '1' to input review or '2' to review reviews")

    initial_input_str = input("Enter 1 or 2: \n")

    while True:
        if initial_input_str == "1":
            print(
                f"You entered {initial_input_str}"
                )
            get_user_review()
            break
        elif initial_input_str == "2":
            print(f"You entered {initial_input_str}")
            display_user_reviews()
            break
        else:
            print("You must choose between 1 or 2")
            return initial_choice()
        break


def get_user_review():
    """
    Get movie review input from the user.
    """
    while True:
        print("Please enter your movie review")
        print("Your review should be ten numbers, seperated by commas.")
        print("Example: 1,2,3,4,5,6,7,8,9,10\n")

        review_str = input("Enter your data here: \n")

        user_review = review_str.split(",")

        if validate_review(user_review):
            print("Data is valid!")
            reviews_data = [int(num) for num in user_review]
            update_inputs_worksheet(reviews_data)
            break
        return user_review

    print("Thank you for your review\n")
    print("Please run program again to view or review")


def validate_review(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError msg if strings cannot be converted into integers,
    or if there aren't exctaly 10 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 10:
            raise ValueError(
                f"Exactly 10 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data entered: {e}, please try again.\n")
        get_user_review()
        return False

    return True


def update_inputs_worksheet(user_review):
    """
    Updates inputs worksheet, add new row with the users review.
    """
    print("Updating inputs worksheet...\n")
    inputs_worksheet = SHEET.worksheet("inputs")
    inputs_worksheet.append_row(user_review)
    print("Your review has been upoaded sucessfully.\n")


def display_user_reviews():
    """
    Displays past user reviews based on users inputs.
    """
    print("Please enter your desired movie statistic\n")
    print("Enter: 'Highest' to review movie with highest rating\n")
    print("Enter: 'Lowest' to review movie with lowest rating\n")
    print("Enter: 'Lenght' to review movie lenghts\n")
    print("Enter: 'Age' to review movie age limits\n")
    print("Enter: 'Upcoming' to review upcoming movies in 2023\n")

    display_choice_str = input("Enter your desired statistic: \n")
    print("\n")

    if display_choice_str == "Highest":
        highest_rated_movie = SHEET.worksheet("highest")
        highest_table = pd.DataFrame(highest_rated_movie.get_all_records())
        print(highest_table.to_string(index=False))
        print("\n")
    elif display_choice_str == "Lowest":
        print("Lowest rated movie")
    elif display_choice_str == "Age":
        age_ratings = SHEET.worksheet("Age")
        age_table = pd.DataFrame(age_ratings.get_all_records())
        print(age_table)
        print("\n")
    elif display_choice_str == "Lenght":
        lenghts = SHEET.worksheet("Lenght")
        lenghts_table = pd.DataFrame(lenghts.get_all_records())
        print(lenghts_table)
        print("\n")
    elif display_choice_str == "Upcoming":
        upcoming = SHEET.worksheet("upcoming")
        upcoming_table = pd.DataFrame(upcoming.get_all_records())
        print(upcoming_table)
        print("\n")
    else:
        print(f"You entered {display_choice_str}")
        print("Input invalid you must input one of the available options")
        print("'Top' 'Lowest' 'Age' 'Lenght' or 'Upcoming'")
        return display_user_reviews()

    print("Thank you for viewing\n")
    print("Please run program again to view or review")


def main():
    """
    Main function to run all programs.
    """
    initial_choice()


print("Welcome to Movie Reviews where your opinion is important to us!\n")
main()
