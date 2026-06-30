# Edge-detection-using-OpenCV-and-Python
Python and OpenCV project demonstrating live Laplacian and Canny edge detection from a webcam feed.

The Laplacian filter detects areas where the image intensity changes rapidly (edges). In the code, the result is first stored as a 64-bit floating-point image to preserve negative and large gradient values, and then converted to an 8-bit integer for display.
The Canny edge detector identifies edges in an image using two threshold values. Lower threshold values detect more edges, while higher threshold values retain only stronger edges, resulting in a cleaner output.
