"""
Calculator Program in Python

Supports operations: addition, subtraction, multiplication, division,
square root, power, factorial, average, percentage calculation.

Includes input validation, calculation history, and option to save history to a file.

"""

import math
from datetime import datetime 

print("BASIC CALCULATOR".center(62,"-"))

operation_names=["Add","Subtract","Multiply","Divide","Square root","Power","Factorial","Average","Percentage","Exit"]

for index,element in enumerate(operation_names):
    print(f"{index+1}. {element}")

# Create a cleaned version of operation names for comparison with user input
empty_list=[operations.strip().lower().replace(" ","") for operations in operation_names ]

# List to store all calculations done in the session
history=[]

# Prompt the user repeatedly until a valid float is entered.

def handling_error(number):
    while True:
        try:
            return float(input(number))
        except ValueError:
            print("Invalid input!!")

 # Prompt the user to input two numbers and return them as floats.
 
def get_two_float():
    num1=handling_error("Enter first number: ")
    num2=handling_error("Enter second number: ")
    return num1,num2

def calculations():
    # Main loop to prompt user for operation choice, perform calculation,
    # store history, and handle continuation or exit.
    while True:
        inputs=input("Please enter the required operation name: ").strip().replace(" ","").lower()
        if inputs in empty_list:
            break
        else:
            print("Please enter a valid operation name:")
            continue

    if inputs=="add":
            number1,number2=get_two_float()
            print(f"{number1} + {number2} = {round(number1+number2,2)}")
            history.append(f"{number1} + {number2} = {round(number1+number2,2)}")
            
    elif inputs=="subtract":
            number1,number2=get_two_float()
            print(f"{number1} - {number2} = {round(number1-number2,2)}")
            history.append(f"{number1} - {number2} = {round(number1-number2,2)}")
            
    elif inputs=="multiply":
            number1,number2=get_two_float()
            print(f"{number1} X {number2} = {round(number1*number2,2)}")
            history.append(f"{number1} X {number2} = {round(number1*number2,2)}")
            
    elif inputs=="divide":
        number1=handling_error("Enter first number: ")
        # Check for division by zero and prompt again if zero is entered
        while True:
           try:
               number2=float(input("Enter second number: "))
               if(number2==0):
                   print("Division is not possible.")
                   continue
               else:
                   break
           except ValueError:
               print("Invalid input!!")
               continue
        
        print(f"{number1} ÷{number2} = {round(number1/number2,2)}")
        history.append(f"{number1} ÷ {number2} = {round(number1/number2,2)}")
           
    elif inputs=="squareroot":
        while True:
            try:
                number1=float(input("Enter a number: "))
                if number1<0:
                   print("Please enter a number greater than 0.")
                   continue
                else:
                   break
            except ValueError:
                print("Invalid input!!\nInput must be a numeric value.")
                continue
                

        print(f"Square root of {number1} = {round(math.sqrt(number1),2)} .")
        history.append(f"Square root of {number1} = {round(math.sqrt(number1),2)} .")

    elif inputs=="power":
            number1,number2=get_two_float()
            print(f"{number1}^{number2} = {round(number1**number2,2)}")
            history.append(f"{number1}^{number2} = {round(number1**number2,2)}")
            
    elif inputs=="factorial":
        while True:
            try:
               number1=int(input("Enter a number: "))
               if number1<0:
                  print("Please enter a number greater than 0.")
               else:
                  break
            except ValueError:
                print("Invalid input!!")
                continue
        
        print(f"Factorial of {number1} is {math.factorial(number1)} .")
        history.append(f"Factorial of {number1} is {math.factorial(number1)} .")
        
    elif inputs=="average":
        while True:
            average_input=int(input("How many numbers do you want to calculate average of?? "))
            if average_input<=0:
                print("Please enter a number greater than 0.")
            else:
                break
        average_empty_list=[]
        for i in range(average_input):
            if (i==0):
                first=handling_error("enter first number: ")
                average_empty_list.append(first)
            else:
                other_numbers=handling_error("Enter next number: ")
                average_empty_list.append(other_numbers)

        print(f"Average of {average_empty_list} is {round(sum(average_empty_list)/len(average_empty_list))}")
        history.append(f"Average of {average_empty_list} is {round(sum(average_empty_list)/len(average_empty_list))}")

    elif inputs=="percentage":
        while True:
            percent_input=int(input("How many numbers do you want to calculate percentage of?? "))
            if percent_input>0:
                break
            else:
                print("Please enter a number greater than 0.")
                continue

        while True:
            denominator=handling_error("Enter the denominator for each value: ")
            if denominator>0:
                break 
            else:
                print("Please enter a number greater than 0.")
                continue

        percent_empty_list=[]

        for i in range(percent_input):
            if (i==0):
                first=handling_error("Enter a number: ")
                percent_empty_list.append(first)
            else:
                other_numbers=handling_error("Enter next number: ")
                percent_empty_list.append(other_numbers)

        print(f"Percentage of {percent_empty_list} is {round((sum(percent_empty_list) / len(percent_empty_list)) / denominator * 100, 2)}%.")
        history.append(f"Percentage of {percent_empty_list} is {round((sum(percent_empty_list) / len(percent_empty_list)) / denominator * 100, 2)}%.")
    
    else:
        print("Thank You!!")
        quit()
    
    repeat=input("Do you want to continue(YES/NO)? ").strip().lower()

    if(repeat=="yes"):
        calculations()
    else:
        show_history=input("Do you want to see history(YES/NO)? ").strip().lower()
        if show_history=="yes":
            for indexes,operations in enumerate(history):
                print(f"{indexes+1}. {operations}")

def main():
    try:
        calculations()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Thank you for using the calculator. Goodbye!")
        quit()

    file_store=input('''Do you want to store your history in a file named "history.txt"(YES/NO)? ''').strip().lower()
    
    if file_store=="yes":
        with open("history.txt","a") as f:
            # Write the session history to "history.txt" file with timestamp
            f.write(f"Session at {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')} \n")
            for entry in history:
              f.write(entry + "\n")
    else:
        print("Thank you for using calculator!!\nGoodbye!!!")
        quit()

if __name__ == "__main__":
    # Program entry point: starts the calculator.
    main()  