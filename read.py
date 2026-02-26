'''
    Creating a function to read the txt file
'''
def read(file):

    """
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
            
        Reads the data in the data.txt file and stores the data with also assigning a product id in a list called products

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Parameters:

        file - It is a opened file called data.txt which contains some product data such as product name, brand, qantity, price and country

        ----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Returns:
        
            products (list): It is a list of dictionaries which contains all the information in the data.txt containing the following keys

            'Product Id' (int) - Id of the products
            'Product Name' (String) - Name of the product
            'Brand' (String) - Brand of the product
            'Quantity' (int) - Quantity of the product available
            'Price' (int) - Price of the product
            'Country' (String) - Country of the product where it is manufactured
              
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    
    products = [] #Creating an empty list products
    i = 1
    content = file.read() #Reading the file 
    file.close() #Closing the file
    lines = content.split('\n') #Splitting the content using \n

    for line in lines: #Using for each loop
        if len(line) > 0: #Checking if a line is empty
            fields = line.split(', ') #Splitting line using ,
            product = {'Product Id': i,'Product Name': fields[0], 'Brand': fields[1], 'Quantity': int(fields[2]), 'Price': int(fields[3]) * 2, 'Country': fields[4]} #Storing key and values in the dictionary
            i = i + 1 #Increasing i by 1
            products.append(product) #Appending the dictionary product in products

    return products #Returning the list products
