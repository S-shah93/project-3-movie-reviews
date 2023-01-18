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


def interface():
    """
    This function allows the user to navigate through
    the entire program.
    """
    print("\n")
    print("Please see the available options below.\n")
    while True:
        print("\n")
        print("1: Current Rankings")
        print("2: Search for a movie")
        print("3: Add a movie to list")
        print("4: Add movie rating")
        print("5: Leave comment for movie")
        print("6: Top rated movie")
        print("7: Lowest rated movie")
        print("0: End program")

        user_choice = input("Enter your choice: \n")

        if user_choice == "1":
            print(f"You entered {user_choice}")
            current_ratings()
            break
        elif user_choice == "2":
            m_search()
            break
        elif user_choice == "3":
            m_add()
            break
        elif user_choice == "4":
            m_rating()
            break
        elif user_choice == "5":
            m_comment()
            break
        elif user_choice == "6":
            m_top()
            break
        elif user_choice == "7":
            m_lowest()
            break
        elif user_choice == "0":
            print("Heading to the initial interface")
            interface()
            break
        else:
            print(f"'You provided {user_choice}")
            print("Invalid choice made.")
            print("Please choose a number between 0 - 5")
            main()


def current_ratings():
    """
    Function to list all movies
    """
    print("Test 1")
    m_titles = SHEET.worksheet("current")
    title_list = m_titles.get_all_values()
    print(title_list)

    print("Please see options below")
    print("1: Add your rating")
    print("2: Search specific movie")
    print("0: End program")

    c_ratings_choice = input("Enter a number between 0 - 1\n")

    if c_ratings_choice == "1":
        m_add()
    elif c_ratings_choice == "2":
        m_search()
    elif c_ratings_choice == "0":
        print("Thank you for visiting!")
        print("Goodbye")
    else:
        print(f"Invalid choice, you entered {c_ratings_choice}\n")
        print("Please choose a number between 0 - 2")
        current_ratings()



def m_search():
    """
    Function to search for movies
    """
    print("Test 2")


def m_add():
    """
    Function to add a movie to the list
    """
    print("Test 3")


def m_rating():
    """
    Function allows user to rate movie from 1 - 5
    """
    print("Test 4")


def m_comment():
    """
    Function allows user leave a comment for a movie
    """
    print("Test 5")


def m_top():
    """
    Function to search the top rated movie
    """
    print("Test 6")


def m_lowest():
    """
    Function to search for the lowest rated
    """
    print("Test 7")


def main():
    """
    Function to run all functions
    """
    interface()


main()
