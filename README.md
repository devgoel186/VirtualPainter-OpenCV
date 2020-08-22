# VirtualPainter_OpenCV

Draw on screen in Real-Time by using physical objects of user-chosen colors through webcam live-feed. Implemented using Python OpenCV.

## Required

* OpenCV
* Numpy

### For installing softwares

```python
pip install opencv-python
pip install numpy
```

## Steps to begin

After performing the above steps for a basic setup, run **create_mask.py** using the command in the terminal:

```python
python create_mask.py
```

Adjust Hue, Saturation, and Value (HSV) using the the **TrackBars** window that pops up until your desired color shows up in the **Mask** window.

Use these HSV values in **virtual_paint.py** by adding them to **myColors** array (line 13 in virtual_paint.py). First clear the default values in the array and then add your values in the format : **[Hue Min, Sat Min, Val Min, Hue Max, Sat Max, Val Max]**.

Similarly add the color you want to show up on the screen in **myColorValues** array, corresponding to the colors in **myColors**. To enter the values, use **BGR format**
Example:-
myColorValues = [[0, 255, 0], [0, 0, 255]] (This corresponds to Green and Red)

After performing the above steps for a basic setup, run **virtual_paint.py** using the command in the terminal:

```python
python virtual_paint.py
```