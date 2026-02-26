import random

def create_bill_For_Restock(products, key, finalPrice, name, date_time, quantity):

    """
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        Creates a bill whenever someone re-stocks in a txt file with the Restock coustomer's name as the file name

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Parameters:

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        products (list): It is a list of dictionaries which contains all the information in the data.txt containing the following keys

            - 'Product Id' (int) - Id of the products
            - 'Product Name' (String) - Name of the product
            - 'Brand' (String) - Brand of the product
            - 'Quantity' (int) - Quantity of the product available
            - 'Price' (int) - Price of the product
            - 'Country' (String) - Country of the product where it is manufactured

        key (int): It is a key entered by the user when asked for the id of the product they want to restock

        finalPrice (int): It is the final price calcualted after the user has completed their transaction

        name (String): It is the name of the user

        date_time (String): It is the date and time when the bill is being created

        quantity (inr): It is the quantity if the products that the user sold

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Returns:
        
            This function doesn't return anything

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    """

    #Writting in the new file
    newFile = open("Restock " + name + " " + str(random.randint(0, 1000000)) + ".txt", "w")
    newFile.write('\n'+ '*'*20 + 'Here is your bill' + '*'*20 + '\n')
    newFile.write('-'*104 + '\n')
    newFile.write('|\tWholeseller Name: ' + name + '\t\t\t\t\t\tDate of transaction: ' + date_time + '\n')
    newFile.write('-'*104 + '\n')

    for product in products:
        if(key == product['Product Id']):
            newFile.write('|\tProduct Name: ' + product['Product Name'] + '\n\n\tBrand: ' +  product['Brand'] + '\n\n|\tQuantity Sold: ' + str(quantity) + '\n')
    newFile.write('\n|\tPrice: ' + str(finalPrice) + '\n')
    newFile.write('-'*104)
    newFile.close()
    
    changing_In_File(products)

def create_final_Bill(products, cart, totalPrice, name, date_time):

    """
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        Creates a bill whenever someone purchase ann item in a txt file with the Purchase coustomer's name as the file name

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Parameters:

        products (list): It is a list of dictionaries which contains all the information in the data.txt containing the following keys

            - 'Product Id' (int) - Id of the products
            - 'Product Name' (String) - Name of the product
            - 'Brand' (String) - Brand of the product
            - 'Quantity' (int) - Quantity of the product available
            - 'Price' (int) - Price of the product
            - 'Country' (String) - Country of the product where it is manufactured
            

        cart (list): It is a list of dictionaries which contains the id and the quantity of the item purchased

            'Product Id' (int): Id of the product purchased
            'Quantity' (int): Quantity if the product that was purchased
            
        
        finalPrice (int): It is the final price calcualted after the user has completed their transaction
        

        name (String): It is the name of the user
        

        date_time (String): It is the date and time when the bill is being created
        

        quantity (inr): It is the quantity if the products that the user bought

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Returns:
        
            This function doesn't return anything

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    """

    #Writig in the new .txt file
    newFile = open("Purchase " + name + " " + str(random.randint(0, 1000000)) + ".txt", "w")
    newFile.write('\n'+ '*'*20 + 'Here is your bill' + '*'*20 + '\n')
    newFile.write('-'*104)
    newFile.write('\n|\tCustomer Name: ' + name + '\t\t\t\tDate of transaction: ' + date_time + '\n')
    newFile.write('-'*104)

    for product in products:
        for item in cart:
            if(item['Product Id'] == product['Product Id']):
                freeQuantity = item['Quantity'] // 3
                newFile.write('\n|\tProduct Name: ' + product['Product Name'] + '\t\t\t\t\t\tBrand: ' + product['Brand'] + '\n\n|\tQuantity Bought: ' + str(item['Quantity']) + '\t\t\t\t\t\tQuantity of free items: ' + str(freeQuantity) + '\n')
    newFile.write('\n|\tPrice: ' + str(totalPrice) + '\n')
    newFile.write('-'*104)
    newFile.close()

    changing_In_File(products)

def changing_In_File(products):

    """
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        Changes the data in the data.txt after a transactio is done and then again starts the process all over again by importing main and calling the need() function 

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

    #Oprening the file for writing
    file = open("data/data.txt", "w")
    
    #Making changes to the file through the new quantity
    for product in products:
        original_price = product['Price'] // 2

        if(product['Quantity'] < 0):
            product['Quantity'] = 0
        line = product['Product Name'] + ", " + product['Brand'] + ", " + str(product['Quantity']) + ", " + str(original_price) + ", " + product['Country'] + "\n"
        file.write(line)

    file.close()

    import main
    main.need()
