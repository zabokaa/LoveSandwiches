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

def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]      #last row will be saved iin stock_row variable

    surplus_data = []   #create new empty list

    # use zip-method for working with two data work sheets
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales      #change stock list to int 
        surplus_data.append(surplus)

    return surplus_data

def update_surplus_worksheet(data):
    """
    add new row to surplus worksheet with the new calculated surplus variable
    """
    print("Updating surplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("Surplus worksheet updated successfully.\n")


def main():
    """
    call all FUNCS of the program // it is common practise to put them in a seperate main FUNC
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]  #another list comprehension
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    update_surplus_worksheet(new_surplus_data)
    print(new_surplus_data)


print("Happy to see you on Love Sandwiches Data Automation!")
# do not forget to call the main FUNC to call all FUNCS of the programm
main()
