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

# This function acts as the main menu
def interface():
    """
    This function allows the user to navigate through
    the entire program.
    """
    print("\n")
    print("Please see the available options below.\n")
    while True:
        # List of available options in the main menu
        print("\n")
        print("1: Current Rankings")
        print("2: Add movie rating to current list")
        print("3: Request a movie to be added to the list")
        print("4: Top rated movie")
        print("5: Lowest rated movie")
        print("0: End program")

        # Users initial input choice
        user_choice = input("Enter your choice: \n")

        # Validates users input for main menu
        if user_choice == "1":
            print(f"You entered {user_choice}\n")
            current_ratings()
            break
        elif user_choice == "2":
            print(f"You entered {user_choice}\n")
            add_rating()
            break
        elif user_choice == "3":
            print(f"You entered {user_choice}\n")
            add_to_list()
            break
        elif user_choice == "4":
            print(f"You entered {user_choice}\n")
            m_top()
            break
        elif user_choice == "5":
            print(f"You entered {user_choice}\n")
            m_lowest()
            break
        elif user_choice == "0":
            print(f"You entered {user_choice}\n")
            print("Ending program now.\n")
            quit()
            break
        else:
            print(f"'You provided {user_choice}")
            print("Invalid input.\n")
            print("Please choose a number between 0 - 5\n")
            main()


# This function displays a list of the current ratings with options
def current_ratings():
    """
    Function to list all movies
    """
    # Displays list of current movie titles and their ratings
    m_titles = SHEET.worksheet("current")
    title_list = pd.DataFrame(m_titles.get_all_records())
    print(title_list.to_string(index=False))

    print("Please see options below")
    print("1: Add your rating")
    print("2: Request movie to be added")
    print("3: See main menu again")
    print("0: End program")

    c_ratings_choice = input("Enter a number between 0 - 1\n")

    if c_ratings_choice == "1":
        add_rating()
    elif c_ratings_choice == "2":
        add_to_list()
    elif c_ratings_choice == "3":
        interface()
    elif c_ratings_choice == "0":
        print("Thank you for visiting!")
        print("Goodbye")
    else:
        print(f"Invalid choice, you entered {c_ratings_choice}\n")
        print("Please choose a number between 0 - 2")
        current_ratings()


def add_rating():
    """
    # Get movie review input from the user.
    """
    while True:
        print("Please enter your movie review")
        print("Your review should be ten numbers, seperated by commas.")
        print("Example: 1,2,3,4,5,6,7,8,9,10\n")
        print("Please input 1 number between 1 - 10 for each title\n")
        print("Seperated by a comma ','\n")
        review_str = input("Enter your data here: \n")

        user_review = review_str.split(",")

        if validate_rating(user_review):
            print("Data is valid!")
            reviews_data = [int(num) for num in user_review]
            update_inputs_worksheet(reviews_data)
            break
        return user_review

    print("Please see options below")
    print("1: Add another rating")
    print("2: See main menu again")
    print("0: End program")
    c_ratings_choice = input("Enter a number between 0 - 1\n")

    if c_ratings_choice == "1":
        add_rating()
    elif c_ratings_choice == "2":
        interface()
    elif c_ratings_choice == "0":
        print("Thank you for visiting!")
        print("Goodbye")
    else:
        print(f"Invalid choice, you entered {c_ratings_choice}\n")
        print("Please choose a number between 0 - 2")
        current_ratings()

    print("Thank you for your review\n")
    print("Please run program again to view or review")


def validate_rating(values):
    """
    # Inside the try, converts all string values into integers.
    # Raises ValueError msg if strings cannot be converted into integers,
    # or if there aren't exctaly 10 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 10:
            raise ValueError(
                f"Exactly 10 values are required, you provided {len(values)}"
                )
        else:
            print(f"You provided {values}")
    except ValueError as er:
        print(f"Invalid data entered: {er}, please try again.\n")
        add_rating()
        return False

    return True


def update_inputs_worksheet(user_review):
    """
    # Updates inputs worksheet, add new row with the users review.
    """
    print("Updating inputs worksheet...\n")
    inputs_worksheet = SHEET.worksheet("inputs")
    inputs_worksheet.append_row(user_review)
    print("Your review has been upoaded sucessfully.\n")


def add_to_list():
    """
    Function to requests a movie to be added to the list.
    """
    while True:
        print("Please enter your request below")
        print("We will update the rankings list in the next update")

        user_request = input("Enter your movie title here: \n")

        print(f"You entered {user_request}")
        if user_request is True:
            print("Data is valid!")
            user_title = [str(value) for value in user_request]
            update_requests_worksheet(user_title)
            break
        else:
            print("invalid data entered")
            return True
        return user_request


def update_requests_worksheet(user_title):
    """
    Updates requests worksheet
    """
    print("Updating requests worksheet...\n")
    requests_worksheet = SHEET.worksheet("requests")
    requests_worksheet.append_row(user_title)
    print("Your review has been upoaded sucessfully.\n")


def validate_title(values):
    """
    # Inside the try, converts all string values into integers.
    # Raises ValueError msg if strings cannot be converted into integers,
    # or if there aren't exctaly 10 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 10:
            raise ValueError(
                f"Exactly 10 values are required, you provided {len(values)}"
                )
        elif range(1, 10):
            raise ValueError(
                f"Choose numbers between 1 - 10, you provided {values}"
                )
        else:
            print(f"You provided {values}")
            print("Please input a number between 1 - 10")
    except ValueError as er:
        print(f"Invalid data entered: {er}, please try again.\n")
        add_rating()
        return False

    return True


def m_top():
    """
    Function to search the top rated movie
    """
    top_movie = SHEET.worksheet("highest")
    top_table = pd.DataFrame(top_movie.get_all_records())
    print(top_table.to_string(index=False))
    print("\n")

    print("1: See lowest rated")
    print("2: See main menu")
    print("0: End program\n")

    m_top_choice = input("Enter a number between 0 - 2\n")

    if m_top_choice == "1":
        m_lowest()
    elif m_top_choice == "2":
        interface()
    elif m_top_choice == "0":
        print("Thank you for visiting!")
        print("Goodbye")
    else:
        print(f"Invalid choice, you entered {m_top_choice}\n")
        print("Please choose a number between 0 - 2")
        m_top()


def m_lowest():
    """
    Function to search for the lowest rated
    """
    lowest_movie = SHEET.worksheet("lowest")
    lowest_table = pd.DataFrame(lowest_movie.get_all_records())
    print(lowest_table.to_string(index=False))
    print("\n")

    print("1: See highest rated")
    print("2: See main menu")
    print("0: End program\n")

    m_lowest_choice = input("Enter a number between 0 - 2\n")

    if m_lowest_choice == "1":
        m_top()
    elif m_lowest_choice == "2":
        interface()
    elif m_lowest_choice == "0":
        print("Thank you for visiting!")
        print("Goodbye")
    else:
        print(f"Invalid choice, you entered {m_lowest_choice}\n")
        print("Please choose a number between 0 - 2")
        m_lowest()


def main():
    """
    Function to run all functions
    """
    interface()


main()
