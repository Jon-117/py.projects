TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining>0:
    print("There are {} tickets left at $10 each".format(tickets_remaining))
    Name=input("What's your name?  ")
    print("Hello, {}.".format(Name))
    #make sure only numbers are allowed to be entered in teh next input
    #--------------------------------------------------------------------
    tickets_desired=input("How many tickets do you want to buy?  ")
    try:
        tickets_desired=int(tickets_desired)
    except ValueError:
        print("Please enter a number less than or equal to",tickets_remaining)
    else:
        if tickets_desired <= tickets_remaining >= 1:
            try:
                proceed=input("Would you like to proceed? Y/N"  ).upper()
                if proceed == "Y":
                    print('Sold! We can barely wait to see you there, {}!'.format(Name))
                    print("You've purchased {} tickets!".format(tickets_desired))
                    print((tickets_remaining - tickets_desired),"tickets are left")
                    tickets_remaining -= tickets_desired
                elif proceed == "N":
                    print("You're really going to miss out, but no worries! Have fun with your other plans, {}.".format(Name))
                    tickets_remaining
            except:
                if proceed != "Y" or "N":
                    print("The input is invalid, {}, please enter Y or N.".format(Name))
        elif tickets_desired > tickets_remaining:
            print("I'm sorry, {}! There aren't enough for that.".format(Name))
        while tickets_remaining < 1:
            print("I'm sorry! No tickets are left!")

        subtotal = TICKET_PRICE*tickets_desired
        print("The price you'll pay is... ${}".format(subtotal))
