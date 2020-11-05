import math
import sys

args = sys.argv


def calculate_differential(principal, periods, interest):
    principal = int(principal)
    periods = int(periods)
    interest = float(interest)
    current_month = 1
    overall_payment = 0

    if principal > 0 and periods > 0 and interest > 0:

        nominal_interest_rate = interest / (12 * 100)

        for i in range(periods):
            dm = (principal / periods) + nominal_interest_rate * \
                 (principal - (principal * (current_month - 1) / periods))

            print('Month {}: payment is {}'.format(
                current_month, math.ceil(dm)))
            current_month += 1
            overall_payment = overall_payment + math.ceil(dm)
        overpayment = overall_payment - principal
        print('Overpayment = {}'.format(math.ceil(overpayment)))

    else:
        print('Incorrect parameters.')


def calculate_loan(payment, periods, interest):
    payment = int(payment)
    periods = int(periods)
    interest = float(interest)

    if payment > 0 and periods > 0 and interest > 0:
        # print(payment, periods, interest)

        nominal_interest_rate = interest / (12 * 100)

        principal = int(payment / ((nominal_interest_rate * \
                                    math.pow(1 + nominal_interest_rate, periods)) /
                                   (math.pow(1 + nominal_interest_rate, periods) - 1)))

        print('Your loan principal = {}'.format(principal))
        overpayment = payment * periods - principal
        print('Overpayment = {}'.format(math.ceil(overpayment)))

    else:
        print('Incorrect parameters.')


def calculate_repay(principal, payment, interest):
    principal = int(principal)
    payment = int(payment)
    interest = float(interest)

    if principal > 0 and payment > 0 and interest > 0:

        nominal_interest_rate = interest / (12 * 100)

        number_of_months = math.ceil(math.log(payment /
                                              (payment - nominal_interest_rate * principal), 1 + \
                                              nominal_interest_rate))

        years = int(number_of_months / 12)
        months = number_of_months % 12

        overpayment = number_of_months * payment - principal
        if months > 0:
            print('It will take {} years and {} months to repay this loan!'.format(years, months))

        print('It will take {} years to repay this loan!'.format(years))
        print('Overpayment = {}'.format(overpayment))

    else:
        print('Incorrect parameters.')


def calculate_periods(principal, periods, interest):
    principal = int(principal)
    periods = int(periods)
    interest = float(interest)

    if principal > 0 and periods > 0 and interest > 0:

        nominal_interest_rate = interest / (12 * 100)

        annuity_payment = math.ceil(principal * ((nominal_interest_rate * math.pow(1 + nominal_interest_rate, periods)) /
                               (math.pow(1 + nominal_interest_rate, periods) - 1)))

        print('Your annuity payment = {}!'.format(annuity_payment))
        overpayment = annuity_payment * periods - principal
        print('Overpayment = {}'.format(overpayment))

    else:
        print('Incorrect parameters.')


def menu():
    list_of_args = []

    for i in range(len(args)):
        x = args[i].split('=')
        list_of_args.append(x[0])

    if args[1] == '--type=diff' and len(args) == 5:
        x = args[2].split('=')
        if x[0] == '--principal':
            x2 = args[3].split('=')
        else:
            print('Incorrect parameters.')
            return
        if x2[0] == '--periods':
            x3 = args[4].split('=')
        else:
            print('Incorrect parameters.')
            return
        if x3[0] == '--interest':
            calculate_differential(x[1], x2[1], x3[1])
        else:
            print('Incorrect parameters.')
            return
    elif args[1] == '--type=annuity' and len(args) == 5 and list_of_args[3] == '--payment':
        x = args[2].split('=')
        if x[0] == '--principal':
            x1 = args[3].split('=')
        else:
            print('Incorrect parameters.')
            return
        if x1[0] == '--payment':
            x2 = args[4].split('=')
        else:
            print('Incorrect parameters.')
            return
        if x2[0] == '--interest':
            calculate_repay(x[1], x1[1], x2[1])
        else:
            print('Incorrect parameters.')
            return
    elif args[1] == '--type=annuity' and len(args) == 5 and list_of_args[2] == '--payment':
        x = args[2].split('=')
        if x[0] == '--payment':
            x1 = args[3].split('=')
        else:
            print('Incorrect parameters.')
            return
        if x1[0] == '--periods':
            x2 = args[4].split('=')
        else:
            print('Incorrect parameters.')
            return
        if x2[0] == '--interest':
            calculate_loan(x[1], x1[1], x2[1])
        else:
            print('Incorrect parameters.')
            return
    elif args[1] == '--type=annuity' and len(args) == 5 and list_of_args[3] == '--periods':
        x = args[2].split('=')
        if x[0] == '--principal':
            x1 = args[3].split('=')
        else:
            print('Incorrect parameters.')
            return
        if x1[0] == '--periods':
            x2 = args[4].split('=')
        else:
            print('Incorrect parameters.')
            return
        if x2[0] == '--interest':
            calculate_periods(x[1], x1[1], x2[1])
        else:
            print('Incorrect parameters.')
            return
    else:
        print('Incorrect parameters')


menu()
