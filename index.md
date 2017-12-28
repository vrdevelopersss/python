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
start(f)
...
end(f)
```
use  **PATTERNS & GEOMETRIES** 
> for example

```python
import threeD as td

td.start(f)
for i in range(0,5):
    xCircle,yCircle = td.circle(40,40,30 - i * 5)
td.end(f)
```

> ## functions

initializes your gcode file ( output.gcode )
```python
start(f)
```
end of file
```python
end(f)
```
writes a dot which positions you give
```python
write(xCoordOfDot,yCoordOfDot,zCoordOfDot,f)
```
returnes circle coordinates which center position and radius you give
```python
xCrc,yCrc = circle(xCoordOfCenter,yCoordOfCenter,radius)
```
returnes wave coordinates which start position and amplitude you give
```python
xWave,yWave = wave([xPosOfStart,yPosOfStart],amplitude)
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

