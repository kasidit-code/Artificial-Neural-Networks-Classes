"""
P3 Egg
Student name: Kasidit Chomputhong
"""

if __name__ == "__main__":
    filename = input("File: ")
    file = open(filename, "r")
    fileData = file.read().split("\n")
    dataList = []
    seriesType, series = input("Series: ").split()
    for item in fileData:
        if item != "" and item[0] != "#":
            data = item.split() 
            if data[1] == series :
                dataList.append(float(data[3]))
    print(dataList)
