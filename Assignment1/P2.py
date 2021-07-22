"""
P2 Online averaging.
Student name: Kasidit Chomputhong
"""

if __name__ == '__main__':

    valueSum = 0
    newx = 0

    while newx >= 0:

        newx += 1
        roundOflooping = str(newx)
        # get input from user
        numInput = float(input("x" + roundOflooping + ": "))
        valueSum += numInput
        xbar = valueSum/newx
        print("mean={:.4f}".format(xbar))
    # end while
        if numInput < 0:
            break