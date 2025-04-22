class club_membership: #Copied from Simon Yusuf
    counter =10000
    total_registered = 0
    total_approved = 0
    total_pending = 0
    def __init__(self, name):
        self.name = name
        self.mem_id = self.generate_id()
        self.add_on = {}
        self.total = 300
        self.approval = ""
        club_membership.total_registered += 1
    def generate_id(self):
        club_membership.counter += 1
        return club_membership.counter
    def request_add_on(self):
        num = int(input("How many add ons?: "))
        for i in range(num):
            add_on_name = input("Name of add on: ")
            price = float(input("Enter the price: "))
            self.add_on[add_on_name] = price
        self.total = sum(self.add_on.values())
        return self.total
    def add_on_approval(self):
        if self.total<=1000:
            self.approval = "Approved"
            club_membership.total_approved += 1
        else:
            self.approval = "Pending"
            club_membership.total_pending += 1
    def display(self):
        print ("Name: ",self.name)
        print ("ID: ",self.mem_id)
        print("Total: ",self.total)
        print ("Status: ", self.approval)
        for add_on, price in self.add_on.items():
            print(add_on,":", price)
num_mem = int(input("How many members are registering today?: "))
for i in range(num_mem):
    name = input("Enter your name: ")
    mem = club_membership(name)
    mem.request_add_on()
    mem.add_on_approval()
    mem.display()
print("Summary")
print("Total registers: ", club_membership.total_registered)
print ("Total approved: ",club_membership.total_approved)
print("Total pending: ",club_membership.total_pending)
