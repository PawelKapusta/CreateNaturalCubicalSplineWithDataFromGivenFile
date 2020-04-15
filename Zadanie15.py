import csv #do odczytu danych z pliku

from numpy import arange
import scipy.interpolate
import matplotlib.pyplot as plt

pointsTab = []
pointsValues = []

with open('daneDoWykresu.txt') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for row in plots:
        pointsTab.append(float(row[1]))#read first column
        pointsValues.append(float(row[2])) #read second column

print("Calculated points:")
for x in pointsTab:
    print(x)

print("Our values are: ")
for x in pointsValues:
    print(x)

splajn = scipy.interpolate.CubicSpline(pointsTab, pointsValues, bc_type='natural')#To create spline

xplot= arange(-1.5, 1.5, 0.0001) #set points


plt.plot(pointsTab, pointsValues, 'rx')
plt.plot(xplot, splajn(xplot), 'g')#draw graph

plt.legend(['Points', 'Line'])
plt.title('Graph of natural cubical spline')
plt.axvline()
plt.axhline()
plt.grid(True)
plt.savefig('Graph.png')
plt.show()

