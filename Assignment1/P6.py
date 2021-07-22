"""
P6 Base-3 stone code
Student name : Kasidit Chomputhong
"""
if __name__ == "__main__":

    # take input
    stonecode = input("Stones: ")

    # calculate
    d = int(stonecode[0])*9 + int(stonecode[1])*3 + int(stonecode[2])

    # print out
    print ("Lapses=", d)