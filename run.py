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


def get_user_review():
    """
    Get movie review input from the user.
    """
    print("Please enter your movie review")
    print("Your review should be ten numbers, seperated by commas.")
    print("Example: 1,2,3,4,5,6,7,8,9,10\n")

    review_str = input("Enter your data here: ")

    user_review = review_str.split(",")
    validate_review(user_review)


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


