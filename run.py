import gspread
from google.oauth2.service_account import Credentials

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
            print("tesing 1")
        if initial_input_str == "2":
            print(f"You entered {initial_input_str}")
            print("testing 2")
        print("You must choose between 1 or 2")
        break


def get_user_review():
    """
    Get movie review input from the user.
    """
    while True:
        print("Please enter your movie review")
        print("Your review should be ten numbers, seperated by commas.")
        print("Example: 1,2,3,4,5,6,7,8,9,10\n")

        review_str = input("Enter your data here: ")

        user_review = review_str.split(",")

        if validate_review(user_review):
            print("Data is valid!")
            break
    return user_review


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


def main():
    """
    Main function to run all programs.
    """
    initial_choice()


print("Welcome to Movie Reviews where your opinion is important to us!\n")
main()
