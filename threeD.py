import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import os
import sympy
import time
import math
# Calculating script time
now = time.time()
# Diameter of the Nozzle
nozzleD = 0.5
# Set Initial X,Y,Z Possition
initPos = [40, 40, 0.5]
# Feed-rate / Speed
speed = 1000
# Temperature of the Nozzle
nozzleTemp = 220
# Number of layers
layerCount = 3
# Height of the layer
layerHeight = nozzleD
# Initial extrusion
E = 10
# Extrusion Area
Area = (nozzleD / 2) ** 2 * np.pi # PI * square of Radius (Diameter / 2)
dens = 20

### GEOMETRIES ###

def rotate(x,y,alpha):
    xRotated = np.array(x) * np.cos(np.deg2rad(alpha)) - np.array(y) * np.sin(np.deg2rad(alpha))
    yRotated = np.array(x) * np.sin(np.deg2rad(alpha)) + np.array(y) * np.cos(np.deg2rad(alpha))
    return xRotated,yRotated

def circle(xStart,yStart,radius):
    xCoord = np.concatenate((np.linspace(xStart - radius,xStart + radius, dens), np.linspace(xStart + radius,xStart - radius, dens)))
    yCoord = np.concatenate((yStart + np.sqrt(radius ** 2 - (xCoord[:dens] - xStart) ** 2),yStart - np.sqrt(radius ** 2 - (xCoord[dens:] - xStart) ** 2)))

def halfCircle(xStart,yStart,radius,length):
    xCoord = np.concatenate((np.linspace(xStart - radius,xStart + radius, dens), np.linspace(xStart + radius,xStart - radius, dens)))
    yCoord = np.concatenate((yStart + np.sqrt(radius ** 2 - (xCoord[:dens] - xStart) ** 2),yStart - np.sqrt(radius ** 2 - (xCoord[dens:] - xStart) ** 2)))

    xUp = []
    yUp = []
    xDown = []
    yDown = []
    for i in range(len(xCoord)):
        if yCoord[i] > yStart :
            yUp.append(yCoord[i])
            xUp.append(xCoord[i])
        if yCoord[i] < yStart :
            yDown.append(yCoord[i] - length)
            xDown.append(xCoord[i])
    x = xUp + xDown
    y = yUp + yDown
    x.append(x[0])
    y.append(y[0])
    plt.plot(x, y)
    plt.axis('equal')
    return x,y

def fill(xPoly,yPoly,alpha,d):
    polyArray = []
    x,y = rotate(xPoly,yPoly,alpha)
    for i in range(len(x)):
        polyArray.append((x[i],y[i]))
    poly = sympy.Polygon(*polyArray)
    reverse = False
    real = 0
    printed = 0
    minX = min(x)
    minY = min(y)
    maxX = max(x)
    maxY = max(y)
    count = (maxY - minY)/d
    inter = []
    xFilled = []
    yFilled = []
    while printed < count :
        real += d
        l = sympy.Line((minX,minY + real),(maxY,minY + real))
        inter.append(poly.intersection(l))
        for i in range(len(inter[printed]) - 1) :
            tempL = sympy.Segment(inter[printed][i],inter[printed][i + 1])
            if poly.encloses_point(tempL.midpoint) :
                if reverse :
                    inter[printed] = np.flip(inter[printed], axis=0)
                xFilled.append(inter[printed][i][0])
                xFilled.append(inter[printed][i + 1][0])
                yFilled.append(inter[printed][i][1])
                yFilled.append(inter[printed][i + 1][1])
            reverse = not reverse
        print(printed)
        printed += 1
    xFinal,yFinal = rotate(xFilled,yFilled,-1 * alpha)
    return xFinal,yFinal
def write(xCoord,yCoord,zCoord,f):
    xCoord = np.float64(xCoord)
    yCoord = np.float64(yCoord)
    E = 0
    f.writelines("G92 E0 \n")
    f.writelines("G10 \n")
    f.writelines("G0 X%.5f Y%.5f Z%.5f F%.3f \n" % (xCoord[0],yCoord[0],zCoord,speed))
    f.writelines("G11 \n")
    for i in range(0, len(xCoord) - 1):
        Distance = np.sqrt((xCoord[i + 1] - xCoord[i]) ** 2 + (yCoord[i + 1] - yCoord[i]) ** 2)
        E = E + (Distance * Area)
        f.writelines("G1 X%.5f Y%.5f Z%.5f E%.5f \n" % (xCoord[i+1], yCoord[i+1],zCoord,E))

def start(f):

    #####################
    #    START CODE     #
    #####################

    f.writelines("M107 ;start with the fan off\n")
    f.writelines("G21 ; set units to millimeters\n")
    f.writelines("G90 ; use absolute coordinates\n")
    f.writelines("M82 ; use absolute distances for extrusion\n")
    f.writelines("G28 ; home all axes\n")
    f.writelines("G1 Z10 F5000 ; lift nozzle \n")
    f.writelines("M109 S%.3f ; set temperature \n" % (nozzleTemp))
    f.writelines("G92 E0 ; zero the extruded length \n")
    f.writelines("G1 E%.3f ; extrude 10 mm of filament \n " % (E))
    # f.writelines("G4 P10000 ; wait 10 seconds for nozzle length to stabilize\n")
    # f.writelines("G1 Z15 F12000 E5 ; move 15 mm up, fast, while extruding 5mm\n")

def end(f):

    ###############################
    #     Default End Commands    #
    ###############################

    plt.show()
    f.writelines("M104 S0 ; extruder heater off \n")
    f.writelines("M140 S0 ; heated bed heater off (if you have it) \n")
    f.writelines("G91 ; relative positioning \n")
    f.writelines("G28 X0 S0 \n")
    f.writelines("G1 Y150 F5000 ; move completed part out\n")
    f.writelines("M84 ; steppers off \n")
    f.writelines("G90 ; absolute positioning \n")
    f.close()



### MY CODE ###

path = str(os.getcwd())
file = path + '\circle.gcode'
# file = path + '/circle.gcode' # uncomment for MAC or LINUX
f = open(file, "w+")


start(f)


alpha = 30
xStart,yStart = halfCircle(100,100,24,37)
d = 2
alpha = [0,10,20,30,40,50,60,70,80,90]
xEnd = []
yEnd = []
for k in range(len(alpha)):
    xEnd,yEnd = polyFill(xStart,yStart,alpha[k],d)
    write(xEnd,yEnd,0.5*(k + 1),f)
end(f)

# print the time needed for script executing
print(math.floor(time.time() - now))

