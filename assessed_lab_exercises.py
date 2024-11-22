def calculator(num1, num2, operator):

    if operator == "+":
        result = num1 + num2
        print(f"The result is: {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"The result is: {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"The result is: {result}")
    elif operator == "/":
        if num2 == 0: 
            print("Error: Cannot divide by zero.")
            result = None
        else:
            result = num1 / num2
            print(f"The result is: {result}")
    elif operator == "%":
        result = num1 % num2
        print(f"The result is: {result}")
    elif operator == ">":
        result = num1 > num2
        print(f"The result is: {result}")
    elif operator == ">=":
        result = num1 >= num2
        print(f"The result is: {result}")
    elif operator == "<":
        result = num1 < num2
        print(f"The result is: {result}")
    elif operator == "<=":
        result = num1 <= num2
        print(f"The result is: {result}")
    else:
        print("Invalid operator.")
        result = None

    return result

def max_of_three(num1, num2, num3):

    """
    This function takes three integers as input and returns the maximum of the three given numbers.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    num3 (int): The third number.

    Returns:
    int: The maximum of the three numbers.
    """
    # Hint: you are required to make use of maximum variable that is returned by the function below.
    # Complete your code implementation here...
    print("This function takes three numbers and returns the maximum number input.")
    maximum = max(num1,num2,num3)
    print(f"{maximum} : is the maximum")
    return maximum

def winning_numbers(user_list, winning_list):
    """
    This function checks if the user's numbers match the predefined winning numbers.

    Parameters:
    user_list (list): A list of three integers representing the user's chosen numbers.
    winning_list (list): A list of integers representing the winning numbers.

    Returns:
    str: A string indicating the prize won:
        - "First" if all three numbers match the winning numbers.
        - "Second" if two numbers match the winning numbers.
        - "Third" if one number matches the winning numbers.
        - "No" if none of the numbers match the winning numbers.

    Example:
    --------
    winning_list = [5, 14, 17]
    user_list = [3, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since one number, 5, matches the winning numbers)

    user_list = [14, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since two numbers, 14 and 5, match the winning numbers)

    The function also prints a message indicating the prize won.
    """

    # Function implementation here ...
    user_set = set(user_list)
    winning_set = set(winning_list)

    MatchingNumbers = user_set.intersection(winning_set)
    NumOfMatching = len(MatchingNumbers)

    if NumOfMatching == 1:
        prize = "Third"
    elif NumOfMatching == 2:
        prize = "Second"
    elif NumOfMatching == 3:
        prize = "First"
    else:
        prize = "No"


    print(f"Congratulations, you won {prize} prize!")
    return prize

def sum_of_evens(min_value, max_value):
    
    """Find the sum of even numbers between two given numbers (inclusive).

    Args:
        min_value (int): Minimum number
        max_value (int): Maximum number

    Returns:
        total: sum of the even numbers between min_value and max_value

    Example:

    min_value = 10
    max_value = 13
    total = sum_of_evens(min_value, max_value)
    print(total) # total is 22.

    """



    # Function implementation here ...

    total = 0
    valuerange = range(min_value, max_value + 1)
    for x in valuerange:
        if x % 2 == 0:
            total += x
    
    print(total)
    #return total
    return total

def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...
    if sorted(str1.lower()) == sorted(str2.lower()):
        output = True
    else:
        output = False

    print(output)
    return output

def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """


    # Function implementation here ...
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # Found a divisor
            return False
    return True 

def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers using a for loop.

    Parameters:
    ----------
    numbers : list
        A list of numerical values (int or float).

    Returns:
    -------
    float:
        The average of the numbers in the list. If the list is empty, returns None.

    Example:
    --------
    calculate_average([10, 20, 30, 40, 50])  # Output: 30.0
    """
    
    # Function implementation here ...

    total = 0

    for i in numbers:
        total += i

    average = total / len(numbers) if len(numbers) > 0 else 0

    print (average)
    return average

def calculate_weekly_pay(hours_worked):
    """
    Calculate the weekly pay for an employee based on the number of hours worked.
    
    Parameters:
    hours_worked (int): The total number of hours worked by the employee in a week.
    
    Returns:
    float: The total weekly pay.
    """
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay



    # Function implementation here ...
    if hours_worked > standard_hours:
        overtime_pay = (hours_worked - standard_hours) * overtime_rate
        total_pay = overtime_pay + (regular_rate * standard_hours)
    else:
        total_pay = hours_worked * regular_rate
    

    print(f"£{total_pay} per week")
    return total_pay

def celsius_to_fahrenheit(celsius):
   # complete your function implementation... 
   
   fahrenheit = (celsius * 9/5) + 32
   print(f"{fahrenheit} degrees fahrenheit")
   output = fahrenheit
   return output

def annual_net_income(gross_salary):
    # complete your function implementation here...
   
    taxrate = 0

    if gross_salary >= 45000:
        taxrate = 50
    elif 30000 <= gross_salary < 45000:
        taxrate = 30
    elif gross_salary < 30000:
        taxrate = 15

    tax_amount = gross_salary * (taxrate / 100)
    net_salary = gross_salary - tax_amount

    print(net_salary)
    return net_salary
    
def letter_occurrence(input_string):
    # complete function implementation...
    amount = 0

    for character in input_string:
        if character.lower() == "a":
            amount += 1
        
    print(f"The letter A appears {amount} times")
    return amount

def km_to_miles(kilometers):
    # complete function implementation here...
   
    km_to_mile = 0.62
    miles = (kilometers * km_to_mile)
    
    miles =(float(round(miles, 3)))

    return miles
    #return miles

def fuel_cost(distance_miles):

     MPG = 50  # Miles per gallon
     LITERS_PER_GALLON = 4.5
     PRICE_PER_LITER = 1.49  # Price in pounds per liter

     total_cost = (PRICE_PER_LITER * (distance_miles / MPG) * LITERS_PER_GALLON)

     print(total_cost)
     return total_cost

def find_maximum_difference(a, b):
#     # code implementation here...

  min_a, max_a = min(a), max(a)
  min_b, max_b = min(b), max(b)
    
    # Calculate the maximum difference
  maximum = max(max_a - min_b, max_b - min_a)
    
  return maximum

def is_golden_number(n):

#     # function implementation ...

    boolean = False

    for a in range(1,n):
        b = n - a
    
        if (a * b) % 1000 == 0:
            boolean = True
        
    
    print(boolean)
    return boolean

def decrypt_cypher_text(encrypted_text, key):
#     # function implementation here...
    decrypted_text = ""

    for character in encrypted_text:
        ascii_code = ord(character)
        new_code = ascii_code - key
        new_code %= 256
        decrypted_character = chr(new_code)
        decrypted_text += decrypted_character
    
    print(decrypted_text)
    return decrypted_text

