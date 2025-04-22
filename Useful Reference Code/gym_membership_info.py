counter = 10 #Copied from Simon Yusuf
def gym_member():
    date=input("Enter date: DD/MM/YYYY:")
    name=input("Enter name: ")
    global counter
    counter = counter + 1
    membership_id = counter
    print("Date:",date)
    print("Name:",name)
    print("Membership ID:",membership_id)
    return date,name,membership_id
#for i in range(3):
 #   gym_member()
def membership_total():
    d,n,m = gym_member()
    print("Hello, ",n)
    add_on=int(input("How many add ons??"))
    add_item = {}
    for i in range(add_on):
        add_name=input("Enter the add on: ")
        amount = float(input("How much? "))
        add_item[add_name] = amount
    total = 0
    for k,v in add_item.items():
        total = total + v
    return total,n,m
#membership_total()
#print(membership_total())
def gym_member_approval():
    status = "Pending"
    ref_number = ""
    t,n,m = membership_total()
    if t < 1000:
        status = "Approved"
        count_id = str(m)
        ref_number =n + count_id[3:]
    else:
        status = "Pending"
        ref_number = "Pending"
    return status, ref_number
s,r = gym_member_approval()
print(s)
print(r)
