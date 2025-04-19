class RequisitionSystem:
    counter = 1000
    approved = 0
    pending = 0

    def __init__(self, date,staff_id,name,approval_ref):
        self.date = date
        self.staff_id = staff_id
        self.name = name
        self.approval_ref = approval_ref
        self.item = {}
        self.status = ""
        self.total = 0
        self.requisition_id = RequisitionSystem.counter
        RequisitionSystem.counter += 1

    def staff_info(self):
        self.date = input ("Enter Date: ")
        self.staff_id = input ("Enter Staff ID: ")
        self.name = input ("Enter Name: ")
        self.requisition_id += 1

    def requisition_details(self):
        item_amount = int(input("How many different items do you request?: "))
        for i in range (item_amount):
            item_requisition = input("What item do you request?: ")
            price = int(input("Enter the price: $"))
            self.item[item_requisition] = price
        self.total = sum(self.item.values())
        return self.total

    def requisition_approval(self):
        if self.total < 500:
            self.status = "Approved"
            mesh_id = str(self.requisition_id)
            self.approval_ref = self.staff_id + mesh_id[+1:]
            RequisitionSystem.approved += 1
        else:
            self.status = "Pending"
            RequisitionSystem.pending += 1
            self.approval_ref = "Unavailable"

    def display_requisition(self):
       for item, price in self.item.items():
            print (item,": $",price)

    def requisition_statistic(self):
        print("Printing Requisition System:")
        print ("Date: ", self.date)
        print("Requisition ID: ", self.requisition_id)
        print("Staff ID: ", self.staff_id)
        print("Staff Name: ", self.name)
        print("Total: $", self.total)
        print("Status: ", self.status)
        print("Approval Reference Number: ", self.approval_ref)

submit_req = int(input("How many people are submitting requests?: "))
for i in range(submit_req):
    stats = RequisitionSystem("","","","")
    stats.staff_info()
    stats.requisition_details()
    stats.requisition_approval()
    stats.display_requisition()
    stats.requisition_statistic()
print("Total number of approved requisitions: ",RequisitionSystem.approved)
print("Total number of pending requisitions: ",RequisitionSystem.pending)

