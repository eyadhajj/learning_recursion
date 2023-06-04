
# Function to input values needed for recursion
def initialise_list():
    lst = []
    num_list = int(input("Input number of items in the list: " )) # The amount of numbers wanted to be used in recursion
    for numbers in range(num_list):
        num = int(input("Enter a value: " )) # For the amount of numbers wanted, assign values to each of them
        lst.append(num)

    return lst

def list_add(list): # Add each of the numbers recursively
    # Base case !
    if len(list) == 1:
        return list[0] # Returns falue of recursion function 

    for i in range(len(list)):
        list[0] = list[0] + list[1]
        list.pop(1) 
        return list_add(list)

def list_subtract(list): # Subtract each of the numbers recursively
    # Base case !
    if len(list) == 1:
        return list[0] # Returns value of the recursion function
    
    for i in range(len(list)):
        list[0] = list[0] - list[1]
        list.pop(1)
        return list_subtract(list) 





