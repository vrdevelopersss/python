import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import os
        ### VARIABLES ###

# Diameter of the Nozzle
nozzleD = 0.5
# Set Initial X,Y,Z Possition
initPos = [40, 40, 0.5]
# Feed-rate / Speed
speed = 1000
# Temperature of the Nozzle
nozzleTemp = 220
# Number of layers
layerCount = 39
# Height of the layer
layerHeight = nozzleD
# Initial extrusion
E = 10
# Extrusion Area
Area = (nozzleD / 2) ** 2 * np.pi # PI * square of Radius (Diameter / 2)

    #####################
    #    Open File      #
    #####################

path = str(os.getcwd())
file = path + '\output.gcode'
f = open(file, "w+")

        ### EXAMPLES ###

# write(xCoordOfDot,yCoordOfDot,zCoordOfDot)
# xCrc,yCrc = circle(xCoordOfCenter,yCoordOfCenter)
# xWave,yWave = wave([xPosOfStart,yPosOfStart],amplitude)
# xRotated,yRotated = rotate([x1,x2],[y1,y2],angle)
# xRect,yRect = rect([xPosOfStart,yPosOfStart],length,height)

########################################### functions

        ### PATTERNS & GEOMETRIES ###

def circle(xStart,yStart,radius):
        
    xCoord = np.concatenate((np.linspace(xStart - radius,xStart + radius, 200), np.linspace(xStart + radius,xStart - radius, 200)))
    yCoord = np.concatenate((yStart + np.sqrt(radius ** 2 - (xCoord[:200] - xStart) ** 2),yStart - np.sqrt(radius ** 2 - (xCoord[200:] - xStart) ** 2)))
    plt.plot(xCoord, yCoord)
    plt.axis('equal')
    return xCoord,yCoord

def wave(position,amplitude):
        
    t = np.arange(0.0, 10., 0.01)
    xCoord = t + position[0]
    yCoord = amplitude*np.sin(0.25*np.pi*t) + position[1]
    plt.plot(xCoord,yCoord)
    plt.axis('equal')
    return xCoord,yCoord

def rect(position,length,height):
        
    x0, y0 = position[0], position[1]
    x1, y1 = x0 + length, y0
    x2, y2 = x1, y0 + height
    x3, y3 = x0, y2
    xCoord = [x0,x1,x2,x3,x0]
    yCoord = [y0,y1,y2,y3,y0]
    plt.plot(xCoord,yCoord)
    plt.axis('equal')
    return xCoord,yCoord

def write(xCoord,yCoord,zCoord,f):
        
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

    #################################################################
