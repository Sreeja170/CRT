# task.py

def get_ticket_price(age):
    if age < 5:
        return 0
    elif age <= 17:
        return 10
    elif age <= 64:
        return 20
    else:
        return 15


age = int(input().strip())
print(get_ticket_price(age))
