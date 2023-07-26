userinput = ''
acstatus = 'off'

while userinput != 'quit':
    userinput = (input("Enter on or off or quit : "))
    if userinput == 'off':
        if acstatus == 'off':
            print("ac already off")
        else:
            print("ac is off now")
            acstatus = 'off'

    elif userinput == 'on':
        if acstatus == 'on':
            print("ac is already on")
        else:
            print("ac is now on")
            acstatus = 'on'