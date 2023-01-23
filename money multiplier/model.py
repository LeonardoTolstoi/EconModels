currency = 0
rate = 0.1
deposits = [100]
reserves = 10
money_supply = currency + sum(deposits)
monetary_base = currency + reserves

def withdraw(c):
    global currency, rate, deposits, reserves, money_supply, monetary_base
    withdrawal = deposits[c]
    deposits[c] = 0
    if withdrawal > reserves:
        print("The bank is dead :/")
        return -1
    else:
        reserves -= withdrawal
        currency += withdrawal
    money_supply = currency + sum(deposits)
    monetary_base = currency + reserves

def put_deposit(depo):
    global currency, rate, deposits, reserves, money_supply, monetary_base
    deposits.append(depo)
    reserves += depo * rate
    money_supply = currency + sum(deposits)
    monetary_base = currency + reserves

def change_str(a, b):
    if a > b:
        return "🔼" + str(a - b)
    elif a == b:
        return "no diff yet"
    else:
        return "🔽" + str(a - b) # at this point in the development this line is useless as money's not spent

last_mb, last_ms = monetary_base, money_supply
while True:
    ms_change, mb_change = change_str(money_supply, last_ms), change_str(monetary_base, last_mb)
    print(f"Monetary base = {monetary_base} ({mb_change}), money supply = {money_supply} ({ms_change}), reserves are {reserves}")
    last_mb = monetary_base
    last_ms = money_supply
    print("Run simulation, withdraw or deposit? r/w/d")
    choice = input()
    if choice == "r":
        print("For how many steps?")
        i = input()
        if i == "b":
            continue
        x = int(i)
        for i in range(x):
            deposit = deposits[-1]
            reserves += deposit * rate
            deposits.append(deposit * (1 - rate))
            money_supply = currency + sum(deposits)
            monetary_base = currency + reserves
    elif choice == "w":
        print("Who withdraws?")
        for i in range(len(deposits)):
            print(i + 1, ": ", deposits[i], sep='')
        inp = input()
        if inp == "b":
            continue
        x = int(inp)
        if withdraw(x - 1) == -1:
            break
    elif choice == "d":
        print("How much to put?")
        i = input()
        if i == "b":
            continue
        put_deposit(int(i))
    else:
        print("You made a typo")