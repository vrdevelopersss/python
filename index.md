# PYTHON repository for 3D modelling

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
> for example

```python
import threeD as td

td.start()
for i in range(0,5):
    xCircle,yCircle = td.circle(40,40,30 - i * 5)
td.end()
```

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
<br>
<hr>
<br>
<script>
    document.getElementsByClassName('page-header')[0].innerHTML += '<a href="https://raw.githubusercontent.com/vrdevelopersss/python/master/threeD.py" class="btn" download>Download file</a>';
    document.head.innerHTML += '<link rel="icon" href="favicon.ico" type="image/x-icon"; />'
</script>

