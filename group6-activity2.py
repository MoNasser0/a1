"""
Group6-activity2.py

Name of group members: Mohammad, Faisal, Khadija

GitHub Links:
https://github.com/Khadeejaakmal/Group6-activity1


Contribution of each member:

Mohammad: AED to British Pounds and British Pounds to AED, comments and docstrings

Faisal: AED to Dollar and Dollar to AED, comments and docstrings

Khadija: AED to Euro and Euro to AED, comments and docstrings

Describtion:
The code displays a interactive Currency Conventor which gives the user a
choice of three currencies to convert them in different orders.
"""

'The main menu is displayed as soon as the code is started'
main_menu="""
         Main Menu
        Welcome to Currency Converter
        ------------------------------
        """
        
# Functions that are used for the currency conversion
def aed_to_britishPound(money):
    'Converts AED to British Pound'
    return money*0.21

def aed_to_dollar(money):
    'Converts AED to Dollar'
    return money*0.27

def aed_to_euro(money):
    'Converts AED to Euro'
    return money*0.25

def dollar_to_aed(amount):
    'Converts Dollar to AED'
    return amount*3.67

def britishPound_to_aed(amount):
    'Converts British Pound to AED'
    return amount*4.66

def eur_to_aed(amount):
    'Converts Euro to AED'
    return amount*3.98
    
 # Initialize user choices for conversion directions and specific conversions

# In the main function the user imput and conversions are handled
def main():
    print(main_menu)
    
    print('Select the conversion direction: ')
    print('1.AED to other currencies.')   
    print('2.Other curriences to AED')
    print('3.Exit')
    answer=int(input('Please select an option(1,2,or 3.): '))

    # second_answer stores the user's choice for converting from AED to another currency.
    # It is initialized as None and set based on user input if they choose to convert from AED.
    second_answer=None

    # third_answer stores the user's choice for converting from another currency to AED.
    # It is initialized as None and set based on user input if they choose to convert to AED.
    third_answer=None

    # If the user choses to convert from AED
    if answer==1:
        
        print('Please specify your conversion: ')
        print('1.AED to Euro.')
        print('2.AED to British Pound.')
        print('3.AED to Dollar.')
        second_answer=int(input('Please enter your specific conversion(1,2 or 3.)'))

    # If user choses to convert from AED to another currency        
    if second_answer==1:
        money=int(input('Please enter the amount you want to convert: '))
        result=aed_to_euro(money)
        print(f'The amount in Euros is {result}.')

    elif second_answer==2:
        money=int(input('Please enter the amount you want to convert: '))
        print(money)
        result=aed_to_britishPound(money)
        print(f'The amount in Pounds is {result}.')

    elif second_answer==3:
        money=int(input('Please enter the amount you want to convert: '))
        print(money)
        result=aed_to_dollar(money)
        print(f'The amount in Dollars is {result}.')
    
    # If user chooses to convert to AED
    if answer==2:
        print('Please specify your conversion: ')
        print('1.Euro to AED.')
        print('2.British Pound to AED.')
        print('3.Dollar to AED.')
        third_answer=int(input('Please select the conversion to want to proceed with(1,2,or 3: )'))
        print(third_answer)
    
    # If user chooses to convert from another currency to AED
    if third_answer==1:
        amount=int(input('Please enter the amount you want to convert: '))
        print(amount)
        result=eur_to_aed(amount)
        print(f'The amount in AED is result {result}.')

    elif third_answer==2:
        amount=int(input('Please enter the amount you want to convert: '))
        print(amount)
        result=britishPound_to_aed(amount)
        print(f'The amount in AED is result {result}.')

    elif third_answer==3:
        amount=int(input('Please enter the amount you want to convert: '))
        print(amount)
        result=dollar_to_aed(amount)
        print(f'The amount in AED is result {result}.')

    # If user wants to exit
    if answer==3:
        print('Program is exit.')

        
if __name__ == "__main__":    
    main()