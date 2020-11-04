import math
import sys


def calculate_repay_n():
    loan_principal = int(input('Enter the loan principal:'))
    monthly_payment = int(input('Enter the monthly payment:'))
    loan_interest = float(input('Enter the loan interest:'))

    nominal_interest_rate = loan_interest / (12 * 100)

    number_of_months = math.ceil(math.log(monthly_payment / (monthly_payment - nominal_interest_rate * loan_principal), 1 + nominal_interest_rate))

    years = int(number_of_months / 12)
    months = number_of_months % 12

    print('It will take {} years and {} months to repay this loan!'.format(years, months))


def calculate_annuity():
    loan_principal = int(input('Enter the loan principal:'))
    number_of_periods = int(input('Enter the number of periods:'))
    loan_interest = float(input('Enter the loan interest:'))

    nominal_interest_rate = loan_interest / (12 * 100)

    annuity_payment = math.ceil(loan_principal * ((nominal_interest_rate* math.pow(1 + nominal_interest_rate, number_of_periods)) /
                               (math.pow(1 + nominal_interest_rate, number_of_periods) - 1)))

    print('Your monthly payment = {}'.format(annuity_payment))


def calculate_principal():
    annuity_payment = float(input('Enter the annuity payment:'))
    number_of_periods = int(input('Enter the number of periods:'))
    loan_interest = float(input('Enter the loan interest:'))

    nominal_interest_rate = loan_interest / (12 * 100)

    principal = math.ceil(annuity_payment / ((nominal_interest_rate * math.pow(1 + nominal_interest_rate, number_of_periods)) /
                                   (math.pow(1 + nominal_interest_rate, number_of_periods) - 1)))

    print('Your loan principal = {}'.format(principal))


def menu():
    print('What do you want to calculate?')
    print('type "n" for number of monthly payments,')
    print('type "a" for annuity monthly payment amount,')
    print('type "p" for loan principal:')

    user_parameter = input()

    if user_parameter == 'n':
        calculate_repay_n()
    elif user_parameter == 'a':
        calculate_annuity()
    elif user_parameter == 'p':
        calculate_principal()


menu()









