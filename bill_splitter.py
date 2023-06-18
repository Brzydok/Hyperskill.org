import random

print("Enter the number of friends joining (including you):")
no_people = int(input())
friends_list = []

if no_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(no_people):
        a = input()
        friends_list.append(a)
    print("Enter the total bill value:")
    bill = int(input())
    bill_per_person = round(float(bill / no_people), 2)
    bill_dict = dict.fromkeys(friends_list, bill_per_person)
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')

    answer = input()
    
    if answer == "Yes":
        lucky_one = random.choice(friends_list)
        print(f"{lucky_one} is the lucky one!")
        bill_per_person = round(float(bill / (no_people - 1)), 2)
        for friend in friends_list:
            if friend != lucky_one:
                bill_dict = dict.fromkeys(friends_list, bill_per_person)    
        bill_dict[lucky_one] = 0
        print(bill_dict)
    else:
        print("No one is going to be lucky")
        bill_per_person = round(float(bill / no_people), 2)
        bill_dict = dict.fromkeys(friends_list, bill_per_person)
        print(bill_dict)
