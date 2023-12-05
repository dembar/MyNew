import datetime
customer=[]
bill = []
dateDue = datetime.datetime(2023, 10, 1)
def customer_data(customer):
    f = open('test.txt', 'a')
    cust_id = int(input("Write customer ID: "))
    text = str(cust_id)+', '
    f.write(text)
    cust_name = str(input("Write customer name: "))
    text = str(cust_name)+', '
    f.write(text)
    cust_bill_Date = input("Write the bill date(MM/DD/YYYY): ")
    text = str(cust_bill_Date)+', '
    f.write(text)
    f.close()
    return customer

def casher(bill, amount):
    f = open('test.txt', 'a')
    while True:
        item_price = int(input("Write item price: "))
        text = str(item_price)+', '
        f.write(text)
        item_quantity = int(input("Write item quantity: "))
        text = str(item_quantity)+', '
        f.write(text)
        a = item_price * item_quantity
        amount = amount + a
        cont = input("Do you want to add another item? Y/N: ")
        if cont.lower() == 'n':
            break
    b = str(amount)+'\n'
    f.write(b)
    f.close()
    return bill, amount

#This is to fill the txt file
#customer_data(customer)
#casher(bill, 0)

#This is to read the document and print the info
f = open('test.txt','r')
NewList=[]
for i in f.readlines():
    NewList.append(i.split(sep=','))
f.close()
user = []
other = []
c = 0
for i in NewList:
    user = []
    for j in range(0,3,2):
        user.insert(j,i[j])
    user.insert(2,i[len(i) - 1])
    other.insert(c,user)
    c +=1
for i in other:
    userId = i[0]
    date_bill = i[1].split(sep='/')
    date_bill = datetime.datetime(int(date_bill[2]), int(date_bill[1]), int(date_bill[0]))
    amount = int(i[2])
    if amount > 999 and date_bill > dateDue:
        print('The amount for this user is high', userId, 'Amount: ', amount)
