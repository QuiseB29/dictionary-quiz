service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_ticket(tickets, ticket_id, customer, issue, status):
    if ticket_id not in tickets:
        tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": status}
        print(f"Ticket '{ticket_id}' added for customer '{customer}'.")
    else:
        print(f"Ticket with ID '{ticket_id}' already exists.")
        
def update_status(tickets, ticket_id, status):
    if ticket_id in tickets:
        tickets[ticket_id]["Status"] = status
        print(f"Ticket ID {ticket_id} status updated to {status}.")
    else:
        print(f"Ticket ID {ticket_id} not found.")
        
def display_ticket(tickets):
    for pid, details in tickets.items():
        print(f"Ticket ID: {pid}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")
        
        
while True:
    print("Service Ticket System")
    print("1: Add Ticket\n2: Update Service Status\n3: Display Service Ticket\n4: Exit")
    choice = input("Enter your choice:")
    
    if choice == "1":
        pid = input("Enter ticket ID:")
        name = input("Enter customer name:")
        issue = input("Enter issue:")
        status = input("Enter status (open/close):")
        add_ticket(service_tickets, pid, name, issue, status)
        
    elif choice == "2":
        pid = input("Enter ticket ID: ")
        status = input("Enter status (open/close):")
        update_status(service_tickets, pid, status)
        
    elif choice == "3":
        display_ticket(service_tickets)
        
    elif choice == "4":
        break
