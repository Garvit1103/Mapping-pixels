## Real-Time Pixel Mapping for 2D LED Array Control

### Introduction
This project gets your current mouse position and maps it to a 5x4 grid. This was used to control a 5x4 LED grid with a mouse using Arduino.

### Setup Instructions
1. Clone the repository.
2. You need to install the dependency: `Pyautogui`
3. Run the script.

##Description
In this code, 1920x1080 pixels are being mapped to 5x4 pixels. This code uses the library pyautogui to get the current mouse position and the time library for the delays between printing the array. This code calculates the distance between the current cursor position and some predefined points and uses a linear search algorithm to find the least distance and maps to that point. This code was initially written for controlling a 2d led array.
