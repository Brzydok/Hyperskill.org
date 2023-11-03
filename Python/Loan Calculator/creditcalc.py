import argparse
from math import log, ceil

parser = argparse.ArgumentParser(description="Calculation of differentiated payments \
To do this, the user can run the program specifying interest, number of monthly payments, and loan principal..")
parser.add_argument("--type", choices=["annuity", "diff"],
                    help="You need to choose only one from the list.")
parser.add_argument("--payment", help="The monthly payment amount")
parser.add_argument("--principal", help="used for calculations of payment")
parser.add_argument("--periods", help="Denotes the number of months needed to repay the loan")
parser.add_argument("--interest", help="specified without a percent sign")

args = parser.parse_args()
alist = []

for arg in vars(args):
   if getattr(args, arg) is not None:
      alist.append(getattr(args, arg))


if args.interest is None or args.type not in ("diff", "annuity") or len(alist) != 4:
   print("Incorrect parameters")

if args.interest == None:
    print("Incorrect parameters")
if args.interest != None:
    interest = float(args.interest)
    i = (interest) / 1200
    if i < 0:
        print("Incorrect parameters")


def number_of_months(p, a, i):
    p = float(args.principal)
    a = float(args.payment)
    if p <= 0:
        print("Incorrect parameters")
    if a <= 0:
        print("Incorrect parameters")
    formula = a / (a - (i * p))
    return log(formula, 1 + i)


def number_of_monthly_payments():
    p = float(args.principal)
    a = float(args.payment)
    if p <= 0:
        print("Incorrect parameters")
    if a <= 0:
        print("Incorrect parameters")
    n = ceil(number_of_months(p, a, i))
    overpayment = ceil(a * n - p)
    if n / 12 > 1:
        if n % 12 == 0:
            print(f'It will take {n // 12} years to repay this loan!')
        else:
            print(f'It will take {n // 12} years and {n % 12} months to repay this loan!')
    else:
        print(f'It will take {n % 12} months to repay this loan!')
    print(f'Overpayment = {int(ceil(overpayment))}')


def annuity_monthly_payment_amount():
    p = float(args.principal)
    n = float(args.periods)
    if p <= 0:
        print("Incorrect parameters")
    if n <= 0:
        print("Incorrect parameters")

    a = p * ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    overpayment = (ceil(a) * n) - p
    print(f'Your annuity payment = {ceil(a)}!')
    print(f'Overpayment = {int(ceil(overpayment))}')


def loan_principal():
    a = float(args.payment)
    n = float(args.periods)
    if a <= 0:
        print("Incorrect parameters")
    if n <= 0:
        print("Incorrect parameters")

    p = a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    overpayment = ceil(a * n - p)

    print(f'Your loan principal = {(p)}!')
    print(f'Overpayment = {int(ceil(overpayment))}')


if args.type == "annuity":
    if args.payment == None:
        if args.interest != None:
            annuity_monthly_payment_amount()
    elif args.principal == None:
        if args.interest != None:
            loan_principal()
    elif args.periods == None:
        if args.interest != None:
            number_of_monthly_payments()


def diff_annuity_monthly_payment_amount():
    p = float(args.principal)
    n = int(args.periods)
    if p <= 0:
        print("Incorrect parameters")
    if n <= 0:
        print("Incorrect parameters")
    m = 1
    counter = 0
    sum_val = 0
    e_list = []
    for e in range(1, n + 1, 1):
        dm = ceil(p / n + i * (p - (p * (m - 1)) / n))
        m += 1
        counter += 1
        sum_val += dm
        e_list += str(dm)
        print(f'Month {counter}: payment is {dm}')
    overpayment = (ceil(sum_val) - p)
    print(f'Overpayment = {int(ceil(overpayment))}')


if args.type == "diff":
    if args.payment == None:
        if args.interest != None:
            diff_annuity_monthly_payment_amount() 
