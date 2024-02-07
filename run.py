import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# functions
def get_sales_data():
    """
    Get sales data
    """
    # while loop so the print messages will be displayed until the input format is valid
    while True:
        print("Pls enter sales data")
        print("Data should be 6 numbers")
        print("Example: 10,20,30,40,50,60\n")

    # data being displayed
        data_str = input("Enter here: ")
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("input data is correct")
            break    #stopping the loop

    return sales_data

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]    #list comprehension, all input data in py are string, so have to convert to int
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True
    # remember to call it!
date = get_sales_data()

