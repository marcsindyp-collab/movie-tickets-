   
    
# Function to handle ticket purchase
def buy_tickets(remaining_tickets):
    """Prompt the user for tickets and return tickets purchased."""
    while True:
        try:
            tickets_requested = int(input("Enter your desired amount of tickets you want to buy (1-4)? "))
            
            # Check if request is valid
            if tickets_requested < 1 or tickets_requested > 4:
                print("You can only buy between 1 and 4 tickets.")
            elif tickets_requested > remaining_tickets:
                print(f"Only {remaining_tickets} tickets remain. Please enter a smaller number.")
            else:
                return tickets_requested  # valid purchase
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

# Function to run ticket selling application
def sell_tickets():
    total_tickets = 10
    buyers = 0

    while total_tickets > 0:  # loop until sold out
        print(f"\nTickets remaining: {total_tickets}")
        tickets_bought = buy_tickets(total_tickets)
        
        # Process purchase
        total_tickets -= tickets_bought
        buyers += 1  # accumulator for number of buyers
        
        print(f"You bought {tickets_bought} ticket(s). {total_tickets} ticket(s) remain.")

    # After loop finishes
    print("\nAll tickets sold!")
    print(f"Total buyers: {buyers}")

# Run the program
sell_tickets()
