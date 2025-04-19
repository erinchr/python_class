from html.parser import endtagfind

counter = 1000
def staff_info():
    date = input("Enter date: ")
    staff_id = input("Enter staff ID: ")
    name = input("Enter staff name: ")
    global counter
    counter = counter + 1
    requisition_id = counter
    print("Date:",date)
    print("Staff ID:",staff_id)
    print("Staff Name:",name)
    print("Requistion ID:",requisition_id)
    return date,staff_id,name,requisition_id
#print(staff_info())

def requisition_total():
    item_amount = int(input("How many different items do you request?: "))
    item = {}
    for i in range(item_amount):
        item_requisition = input("What item do you request?: ")
        price = int(input("Enter the price: $"))
        item[item_requisition] = price
    for item_requisition, price in item.items():
        print(item_requisition, ": $", price)
    total = 0
    for price in item.values():
        total = total + price
    print("Total: $",total)
    return item_amount,item_requisition,price,total
#print (requisition_total())

def requisition_approval():
    d,s,n,r = staff_info()
    a,ir,p,t = requisition_total()
    status = "Status: Pending"
    if t < 500:
        status = "Status: Approved"
        mesh_id = str(r)
        approval_ref = s + mesh_id[+1:]
        #print("Total: $",t)
        print(status)
        print ("Approval Reference Number:",approval_ref)
        return approval_ref,d,r,s,n,t,status
    else:
        print (status)
#print (requisition_approval())

def display_requisitions():
    a,d,r,s,n,t,st = requisition_approval()
    print_req = "Printing Requisitions:"
    print(print_req)
    print("Date: ",d)
    print("Requisition ID: ",r)
    print("Staff ID: ",s)
    print("Staff Name: ",n)
    print ("Total: $",t)
    print(st)
    print("Approval Reference Number: ",a)
    return print_req,a,d,r,s,n,t,st
print (display_requisitions())