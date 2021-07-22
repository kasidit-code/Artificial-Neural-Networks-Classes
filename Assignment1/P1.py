"""
P1 Orientation
Student name : Kasidit Chomputhong
"""

if __name__ == "__main__":

    #take input
    starDirection = input("observe: ")

    # if else statement
    if starDirection.lower() == "u":
        print("facing east")
    elif starDirection.lower() == "d":
        print("facing west")
    elif starDirection.lower() == "l":
        print("facing north")
    elif starDirection.lower() == "r":
        print("facing south")
    elif starDirection.lower() == "ul":
        print("facing north-east")
    elif starDirection.lower() == "ur":
        print("facing south-east")
    elif starDirection.lower() == "dl":
        print("facing north-west")
    elif starDirection.lower() == "dr":
        print("facing south-west")