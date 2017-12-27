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

        ### EXAMPLES ###

# write(xCoordOfDot,yCoordOfDot,zCoordOfDot)
# xCrc,yCrc = circle(xCoordOfCenter,yCoordOfCenter)
# xWave,yWave = wave([xPosOfStart,yPosOfStart],amplitude)
# xRotated,yRotated = rotate([x1,x2],[y1,y2],angle)
# xRect,yRect = rect([xPosOfStart,yPosOfStart],length,height)

########################################### functions

        ### PATTERNS & GEOMETRIES ###

def circle(X0, Y0, R):
    xCoord = np.concatenate((np.linspace(X0 - R, X0 + R, 200), np.linspace(X0 + R, X0 - R, 200)))
    yCoord = np.concatenate((Y0 + np.sqrt(R ** 2 - (X[:200] - X0) ** 2), Y0 - np.sqrt(R ** 2 - (X[200:] - X0) ** 2)))
    plt.plot(xCoord, yCoord)
    plt.axis('equal')
    return xCoord,yCoord

def wave(position, amplitude):
    t = np.arange(0.0, 10., 0.01)
    xCoord = t + position[0]
    yCoord = amplitude*np.sin(0.25*np.pi*t) + position[1]
    plt.plot(xCoord,yCoord)
    plt.axis('equal')
    return xCoord,yCoord

def rotate(xCoords,yCoords,alpha):
    xNew = xCoord * np.cos(np.deg2rad(alpha)) - yCoords * np.sin(np.deg2rad(alpha)) 
    yNew = xCoord * np.sin(np.deg2rad(alpha)) + yCoords * np.cos(np.deg2rad(alpha))
    return xNew,yNew

def rect(position, length, height):
    x0, y0 = position[0], position[1]
    x1, y1 = x0 + length, y0
    x2, y2 = x1, y0 + height
    x3, y3 = x0, y2
    x4, y4 = x0, y0
    xCoord = [x0,x1,x2,x3,x4]
    yCoord = [y0,y1,y2,y3,y4]
    plt.plot(xCoord,yCoord)
    plt.axis('equal')
    return xCoord,yCoord

def write(xCoord,yCoord,zCoord):
    E = 0
    f.writelines("G92 E0 \n")
    f.writelines("G10 \n")
    f.writelines("G0 X%.5f Y%.5f Z%.5f F%.3f \n" % (xCoord[0],yCoord[0],zCoord,speed))
    f.writelines("G11 \n")
    for i in range(0, len(X) - 1):
        Distance = np.sqrt((xCoord[i + 1] - xCoord[i]) ** 2 + (yCoord[i + 1] - yCoord[i]) ** 2)
        E = E + (Distance * Area)
        f.writelines("G1 X%.5f Y%.5f Z%.5f E%.5f \n" % (xCoord[i+1], yCoord[i+1],zCoord,E))

def start():

    #####################
    #    Open File      #
    #####################

    path = str(os.getcwd())
    file = path + '\output.gcode'
    f = open(file, "w+")

    #####################
    #    START CODE     #
    #####################

    f.writelines("M107 ;start with the fan off\n")
    f.writelines("G21 ; set units to millimeters\n")
    f.writelines("G90 ; use absolute coordinates\n")
    f.writelines("M82 ; use absolute distances for extrusion\n")
    f.writelines("G28 ; home all axes\n")
    f.writelines("G1 Z10 F5000 ; lift nozzle \n")
    f.writelines("M109 S%.3f ; set temperature \n" % (Temp_C))
    f.writelines("G92 E0 ; zero the extruded length \n")
    f.writelines("G1 E%.3f ; extrude 10 mm of filament \n " % (E))
    # f.writelines("G4 P10000 ; wait 10 seconds for nozzle length to stabilize\n")
    # f.writelines("G1 Z15 F12000 E5 ; move 15 mm up, fast, while extruding 5mm\n")

def end():

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
