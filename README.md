# PYTHON repository for 3D modelling

<script>
document.head.innerHTML += '<link rel="icon" href="favicon.ico" type="image/x-icon" />'
</script>

use online [notebook](https://try.jupyter.org/)
for fast using and testing
## usage

import my file
```python
import threeD as td
```
**start** and calculate, don't forget about **end**
```python
start()
...
end()
```
use  **PATTERNS & GEOMETRIES** 


> ## functions

initializes your gcode file ( output.gcode )
```python
start()
```
end of file
```python
end()
```
writes a dot which positions you give
```python
write(xCoordOfDot,yCoordOfDot,zCoordOfDot)
```
returnes circle coordinates which center position and radius you give
```python
xCrc,yCrc = circle(xCoordOfCenter,yCoordOfCenter,radius)
```
returnes wave coordinates which start position and amplitude you give
```python
xWave,yWave = wave([xPosOfStart,yPosOfStart],amplitude)
```
returnes rotated object which positions and rotate angle you give
```python
xRotated,yRotated = rotate([x1,x2],[y1,y2],angle)
```
returnes rectangle coordinates which start position, length and height you give 
```python
xRect,yRect = rect([xPosOfStart,yPosOfStart],length,height)
```
