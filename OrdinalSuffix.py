#Program that prints the ordinal suffex of a number
while True:
    try:
        intNumber = int(input("Enter an integer that you want the ordinal suffex of: "))
        break
    except ValueError:
        print("My guy thats not a valid integer try again please")


def ordinalSuffix(number):
    strNumber = str(number)
    if strNumber[-2:] in ("11", "12", "13"):
        return f"{strNumber}th"
    if strNumber[-1:] in ("1"):
        return f"{strNumber}st"
    if strNumber[-1:] in "2":
        return f"{strNumber}nd"
    if strNumber[-1:] in "3":
        return f"{strNumber}rd"
    return f"{strNumber}th"

print(f"Your ordinal number is: {ordinalSuffix(intNumber)}")
