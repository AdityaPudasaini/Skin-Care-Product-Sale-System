import read #Importing reed
import write #Importing write
import operations #Impoprting operations

'''
    Creating a function to take input from user on what action they want to perform
'''

def input_from_user(products):

    """
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        Gets input from the user on what action they would like to perform and depending on that input calling a function from the operations and also handles exception
        
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Parameters:

        products (list): It is a list of dictionaries which contains all the information in the data.txt containing the following keys

            'Product Id' (int) - Id of the products
            'Product Name' (String) - Name of the product
            'Brand' (String) - Brand of the product
            'Quantity' (int) - Quantity of the product available
            'Price' (int) - Price of the product
            'Country' (String) - Country of the product where it is manufactured

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Returns:
        
            This function doesn't return anything

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    """

    
    cart = [] #Creating an empty list cart
    done = False

    while(done == False):
        #Using try and except to handle error in value
        try:
            value = int(input("\nWhat action would you like to perform?\n1 - Purchase an item\n2 - Sell an item\n3 - Print the details of products\n4-Exit\n\nEnter: "))

            if(value == 1):
                done = True
                operations.check_Purchase_Item(products, cart)
                
            elif(value == 2):
                done = True
                operations.check_For_Restock_Item(products)

            elif(value == 3):
                operations.printing_All(products)
                
            elif(value == 4):
                exit()

            else:
                print("Invalid input. Please enter a valid number")
                
        except :
            print("Invalid input. Please enter a number")

def need():

    """
        ---------------------------------------------------------------------------------------------------------------------------------------------------
            
        Calls the printing_All(products) function with products as parameters and also calls the fucntion input_from_user(products) with the same parameter

        ---------------------------------------------------------------------------------------------------------------------------------------------------

        Parameters:

            This function doesn't have any parameter

        --------------------------------------------------------------------------------------------------------------------------------------------------

        Returns:
        
            This function doesn't return anything

        --------------------------------------------------------------------------------------------------------------------------------------------------
    """
    
    operations.printing_All(products)
    input_from_user(products)

#Reading data.txt file 
file = open("data/data.txt", "r")
products = read.read(file)
need()
