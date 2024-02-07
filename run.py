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
    print("Pls enter sales data")
    print("Data should be 6 numbers")
    print("Example: 10,20,30,40,50,60\n")
# data being displayed
    data_str = input("Enter here: ")
    # testing:  and do not forget the f in the print statement!!
    print(f"data provided is {data_str}")
    # remember to call it!
get_sales_data()

