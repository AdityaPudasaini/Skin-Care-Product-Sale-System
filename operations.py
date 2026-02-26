import write # Importing write
import datetime #Importing datetime module

def printing_All(products):

    """
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        Prints the details of the product or the data stored in the products in the console

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
    
    print('\n\n' + '*'*50 + '  Products  ' + '*'*50 + '\n\n')
    print('Product Id\t| Product Name\t\t| Brand\t\t\t| Quantity\t\t| Price\t\t| Country')

    print('-'*120)

#Printing details using for each loop and through products
    for product in products: 
        print(product['Product Id'] , "\t\t| " + product['Product Name'] + "\t| " + product['Brand'] + "\t\t| " , product['Quantity'], "\t\t\t| " + str(product['Price']) + "\t\t| " + product['Country'] )



def check_Purchase_Item(products, cart):

    """
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        Checks the id provided by the user during purchase and if it matches calls the purchase_Item function

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Parameters:


        products (list): It is a list of dictionaries which contains all the information in the data.txt containing the following keys

            'Product Id' (int) - Id of the products
            'Product Name' (String) - Name of the product
            'Brand' (String) - Brand of the product
            'Quantity' (int) - Quantity of the product available
            'Price' (int) - Price of the product
            'Country' (String) - Country of the product where it is manufactured


        cart (list): It is a empty list
        
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Returns:
        
            This function doesn't return anything

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    
    while True:
        #Using try and except to handle error in key
        try:
            key = int(input('\nEnter the product id of the product you desire: '))
            for product in products:
                if(key == product['Product Id']):
                    purchase_Item(products, key, cart)
                    '''
                        Calls the function purchase_Item if the given id and existing id matches
                    '''
            print('Incorrect id. Please try again.')
        except :
            print('Invalid input.')


def purchase_Item(products, key, cart):

    """
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        Checks if the quantity provided by the user is valid or not. If valid makes changes to the quantity in products, stores data in cart and asks for a decision
        from the user and based on the decision calls the respective function

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Parameters:


        products (list): It is a list of dictionaries which contains all the information in the data.txt containing the following keys

            'Product Id' (int) - Id of the products
            'Product Name' (String) - Name of the product
            'Brand' (String) - Brand of the product
            'Quantity' (int) - Quantity of the product available
            'Price' (int) - Price of the product
            'Country' (String) - Country of the product where it is manufactured


        cart (list): It is an empty list

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Returns:
        
            This function doesn't return anything

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    
    while True:
        #Using try and except to handle error in quan
        try:
            #Asks user for quan
            quan = int(input("\nEnter the quantity of the product you desire to purchase: "))
            break #Breaks out of the infinite loop
        
        except :
            print('Invalid input. Please enter a number.')

    for product in products:
        if(key == product['Product Id']):

            
            #Checking if the provided quantity is greater than in our stock
            if(quan > (product['Quantity'] - (product['Quantity']//4))):
                print('\nThe quantity of products that you desire excedes our total stock of it.')
                print('We can only buy ', (product['Quantity'] - (product['Quantity']//4)), '.')
                check_Purchase_Item(products, cart)
                return

            #Checking if the provided quantity is in negative
            if(quan < 0):
                print('\nThe quantity of products that you desire is invalid.')
                check_Purchase_Item(products, cart)
                return

            else:
                found = False

                #Making changes in the product
                for product in products:
                    if(product['Product Id'] == key):
                        product['Quantity'] = max(0, product['Quantity'] - quan - (quan // 3))

                #Adding the quantity given by user to cart
                for item in cart:
                    if(item['Product Id'] == key):
                        item['Quantity'] += quan
                        found = True
                        break

                #If found is false, adds that item to the cart
                if(found == False):
                    cart.append({'Product Id': key, 'Quantity': quan})

                totalQuantity = 0

                #Getting total quantity
                for item in cart:
                        totalQuantity += item['Quantity']


                #Infinite loop
                while True:
                    #Asking the user what he wants to do
                    try:
                        decision = int(input('\nEnter 1 if you want to purchase another item, 2 if that is everything, or 3 to see the products: '))


                        '''
                            Asking user for a decision and based on that decision call the respective function
                        '''
                        if decision == 1:
                            check_Purchase_Item(products, cart)
                            break

                        elif decision == 2:
                            make_Bill(products, totalQuantity, cart)
                            break
 
                        elif decision == 3:
                            printing_All(products)
                            continue

                            '''
                                Importing main which reads, prints and asks user for input all over again
                            '''

                        else:
                            print('Enter a valid number.')

                    except :
                        print('Invalid input. Please enter a number.')



def check_For_Restock_Item(products):

    """
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        Checks if the id provided by the user during re-stock is valid or not. If valid calls the function restock_Item(products, key)

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

    #Infinite loop
    while True:

        #Using try and catch to handle errors
        try:
            #Asking user for id
            key = int(input('\nEnter the product id of the product you want to sell: '))
            
            for product in products:
                if(key == product['Product Id']):
                    restock_Item(products, key)

                    '''
                        If the provided id and existing one matches, the function restock_Item is called
                    '''
                    return
                
            print('Incorrect id. Please try again.')
            
        except :
            print('Invalid input.')

def restock_Item(products, key):

    """
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        Checks if the quantity provided by the user is valid or not. If valid makes changes to the quantity in products and calls the function
        bill_For_Restock(products, key, quantity)


        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Parameters:


        products (list): It is a list of dictionaries which contains all the information in the data.txt containing the following keys

            'Product Id' (int) - Id of the products
            'Product Name' (String) - Name of the product
            'Brand' (String) - Brand of the product
            'Quantity' (int) - Quantity of the product available
            'Price' (int) - Price of the product
            'Country' (String) - Country of the product where it is manufactured


        key (int): It is a key entered by the user when asked for the id of the product they want to restock

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Returns:
        
            This function doesn't return anything

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    """

    #Infifnite loop
    while True:
        #Using try and except to handle exception
        try:
            #Asking user for quantity
            quantity = int(input('\nEnter the quantity of the item you want to sell: '))

            #Checking if quantity is valid
            if(quantity < 1):
                print('Invalid quantity.')

            else:
                for product in products:
                    if(key == product['Product Id']):
                        product['Quantity'] = product['Quantity'] + quantity
                        #Changing quantity in products
                        
                bill_For_Restock(products, key, quantity)
                #Calling the function bill_For_Restock(products, key, quantity)
                return
                
        except:
            print('Invalid input. Please enter a valid number.')

def bill_For_Restock(products, key, quantity):

    """
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        Checks if the price provided by user is valid or not. If valid asks the user for name, gets date and time and then prints the bill for re-stock in the console
        and then calls the function create_bill_For_Restock(products, key, finalPrice, name, date_time, quantity) from write

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Parameters:

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        products (list): It is a list of dictionaries which contains all the information in the data.txt containing the following keys

            'Product Id' (int) - Id of the products
            'Product Name' (String) - Name of the product
            'Brand' (String) - Brand of the product
            'Quantity' (int) - Quantity of the product available
            'Price' (int) - Price of the product
            'Country' (String) - Country of the product where it is manufactured


        key (int): It is a key entered by the user when asked for the id of the product they want to restock


        quantity (inr): It is the quantity if the products that the user reeocked

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Returns:
        
            This function doesn't return anything

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    """

    #Infinite loop
    while True:
        #Using try and except to handle exception
        try:
            #Asking user for price
            price = int(input('\nEnter the price of the product: '))

            #Checking if price ia valid nnmber
            if(price < 0):
                print('Price cannot be negative.')

            else:
                break

        except:
            print('Invalid input. Enter a number')

    #Calculating final price with VAT
    finalPrice = price * quantity *1.13

    #Asking user for their name
    name = input('\nEnter your name: ')

    #Getting date and time
    date_time = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)

    print('\n', '*'*20, 'Here is your bill','*'*20,'\n')
    print('-'*104)
    print('|\tWholeseller Name: ', name, '\t\t\t\t\t\tDate of transaction: ', date_time)
    print('-'*104)

    #Printing bill
    for product in products:
        if(key == product['Product Id']):
            print('|\tProduct Name: ', product['Product Name'], '\n\n\tBrand: ', product['Brand'] , '\n\n|\tQuantity sold: ', quantity, '\n')
    print('|\tPrice: ', finalPrice)
    print('-'*104)
    write.create_bill_For_Restock(products, key, finalPrice, name, date_time, quantity)

def make_Bill(products, totalQuantity, cart):

    """
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        Calculates the total price based on the quantity and products purchased

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Parameters:


        products (list): It is a list of dictionaries which contains all the information in the data.txt containing the following keys

            'Product Id' (int) - Id of the products
            'Product Name' (String) - Name of the product
            'Brand' (String) - Brand of the product
            'Quantity' (int) - Quantity of the product available
            'Price' (int) - Price of the product
            'Country' (String) - Country of the product where it is manufactured

        -----------------------------------------------------------------------------------------------------------------------------------------------------------------

        cart (list): It is a list of dictionaries which contains the id and the quantity of the item purchased

            'Product Id' (int): Id of the product purchased
            'Quantity' (int): Quantity if the product that was purchased

        -----------------------------------------------------------------------------------------------------------------------------------------------------------------

        toatlQuantity (int): It is the quantity if the products that the user purchased

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Returns:
        
            This function doesn't return anything

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    """

    #Calcualting total price for bill creation
    totalPrice = 0
    for product in products:
        for item in cart:
            if(item['Product Id'] == product['Product Id']):
                totalQuantityAfterFree = item['Quantity'] - item['Quantity'] // 3
                totalItemPrice = totalQuantityAfterFree * product['Price']
                totalPrice += totalItemPrice

    final_Bill(products, cart, totalPrice)


def final_Bill(products, cart, totalPrice):

    """
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        Gets the user's name, date and time and then prints the bill in the console. After that calls the function
        create_final_Bill(products, cart, totalPrice, name, date_time) from write

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Parameters:

        products (list): It is a list of dictionaries which contains all the information in the data.txt containing the following keys

            'Product Id' (int) - Id of the products
            'Product Name' (String) - Name of the product
            'Brand' (String) - Brand of the product
            'Quantity' (int) - Quantity of the product available
            'Price' (int) - Price of the product
            'Country' (String) - Country of the product where it is manufactured


        cart (list): It is a list of dictionaries which contains the id and the quantity of the item purchased

            'Product Id' (int): Id of the product purchased
            'Quantity' (int): Quantity if the product that was purchased
            

        toatlQuantity (int): It is the quantity if the products that the user purchased

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Returns:
        
            This function doesn't return anything

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    """

    #Asking user for their name
    name = input('\nEnter your name: ')

    #Getting date and time
    date_time = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)

    print('\n', '*'*20, 'Here is your bill','*'*20,'\n')
    print('-'*104)
    print('|\tCustomer Name: ', name, '\t\t\t\t\t\tDate of transaction: ', date_time)
    print('-'*104)

    #Printing the bill
    for product in products:
        for item in cart:
            if(item['Product Id'] == product['Product Id']):
                freeQuantity = item['Quantity'] // 3
                print('|\tProduct Name: ', product['Product Name'], '\t\t\t\t\t|\tBrand: ', product['Brand'] , '\n\n|\tQuantity Bought: ', item['Quantity'], '\t\t\t\t\t\tQuantity of free items: ', freeQuantity, '\n')
    print('|\tPrice: ', totalPrice)
    print('-'*104)
    write.create_final_Bill(products, cart, totalPrice, name, date_time)
    
