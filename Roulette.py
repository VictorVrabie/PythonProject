
def AboveMinimum (bet, minbet):
    output = []
    for item in bet :
        if item > minbet:
            output.append("TRUE")
        else :
            output.append("FALSE")
    print(output)
