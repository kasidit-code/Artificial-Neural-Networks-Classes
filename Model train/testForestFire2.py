"""
Wind speed affecting forest fires
Student name: Kasidit Chomputhong
Student number : 623040208-0

Attribute Information:

For more information, read [Cortez and Morais, 2007].
1. X - x-axis spatial coordinate within the Montesinho park map: 1 to 9
2. Y - y-axis spatial coordinate within the Montesinho park map: 2 to 9
3. month - month of the year: 'jan' to 'dec'
4. day - day of the week: 'mon' to 'sun'
5. FFMC - FFMC index from the FWI system: 18.7 to 96.20
6. DMC - DMC index from the FWI system: 1.1 to 291.3
7. DC - DC index from the FWI system: 7.9 to 860.6
8. ISI - ISI index from the FWI system: 0.0 to 56.10
9. temp - temperature in Celsius degrees: 2.2 to 33.30
10. RH - relative humidity in %: 15.0 to 100
11. wind - wind speed in km/h: 0.40 to 9.40
12. rain - outside rain in mm/m2 : 0.0 to 6.4
13. area - the burned area of the forest (in ha): 0.00 to 1090.84
(this output variable is very skewed towards 0.0, thus it may make
sense to model with the logarithm transform).

"""
import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt

# read data file
data = pd.read_csv(r"Model train\forestfires.csv")
# variables
x, y = data.wind, data.temp


if __name__ == "__main__" :
    gx = np.linspace(0,10,50)
    gy = ((gx-4.9)**2)+1.96
    plt.plot(x, y, 'ob')
    plt.plot(gx, gy, "-")
    plt.title("Wind speed affecting forest fires")
    plt.ylabel("Temperature (Celsius degrees)")
    plt.xlabel("Wind speed (Km/h)")
    plt.plot()
    plt.show()