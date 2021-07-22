"""
P4 Climate model
Student name: Kasidit Chomputhong
"""

if __name__ == "__main__":

    #take input
    solarHeat = float(input("S: "))
    albedo = float(input("a: "))
    emissivity = float(input("e: "))

    # calculate
    temparature = (((1 - albedo) * solarHeat) / (emissivity * 5.67 * (10 ** -8))) ** (1/4)

    # print out
    print("T= {:.2f}".format(temparature))