#def score(**kwargs):
    #total=0
    #for k,v in kwargs.items():
        #total=total+v
    #avg=total/len(kwargs)
    #print (avg)
    #print(total)
    ## The title of this program is missleading. This was previously a copy for the args demonstration. The computer was lagging too much to create a new project and keep up with the lecture
class Ticket:
    ticket_counter = 1 #begin from here
    tickets = []
    
    def __init__(self,date,employee_id,employee_name,issue_desp):
        self.ticket_id = Ticket.ticket_counter
        Ticket.ticket_counter+=1
        self.date = date
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.issue_desp = issue_desp
        self.status = "In Progress"
        self.priority = self.assign_priority()
        self.resolution_message = None
        if "password reset" in self.issue_desp.lower():
            self.auto_password_reset()
        Ticket.tickets.append(self)
    def assign_priority(self):
        issues = ["System Outage","Network Failure"]
        for desp in issues:
            if desp in self.issue_desp:
                return "High"
        return "Low"
    def auto_password_reset(self):
        password = self.employee_id[:2] + self.employee_name[:3]
        self.status = "Resolved"
        self.resolution_message = (f"Password reset completed. Your new password is ",{password})

    @classmethod
    def ticket_statistics(cls):
        total_submitted = len(Ticket.tickets)
        resolved_ticket = 0
        total_in_progress = 0
        total_closed = 0
        for each_ticket in Ticket.tickets:
            if each_ticket.status == "Resolved":
                resolved_ticket +=1
            elif    resolved_ticket.status == "In Progress":
                total_in_progress +=1
            elif each_ticket.status == "Closed":
                total_closed +=1
        print ("---------------Statistics-----------------")
        print ("Total tickets: ", total_submitted)
        print ("Total in progress: ", total_in_progress)
        print ("Total Closed: ", total_closed)
        print ("Total tickets resolved: ",resolved_ticket)
    @classmethod
    def display_tickets(cls):
        for ticket in Ticket.tickets:
            print("Date: ",ticket.date)
            print("Ticket ID:", ticket.ticket_id)
            print("Employee ID",ticket.employee_id)
            print("Name: ", ticket.employee_name)
            print ("Issue: ", ticket.issue_desp)
            print ("Priority: ", ticket.priority)
            print ("Status: ", ticket.status)
            print("Resolution:", ticket.resolution_message)
Ticket("20.02.2025", "2000","Simon", "Password Reset")

Ticket.display_tickets()
Ticket.ticket_statistics()
