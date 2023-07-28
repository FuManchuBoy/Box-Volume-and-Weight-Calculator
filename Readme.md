# Box Volume and Weight Calculator

## Description

The Box Volume and Weight Calculator is a simple Python program that allows users to calculate the volume and weight of a box based on user-provided dimensions and material. It is designed to be easy to use and supports both the European (cm) and American (inches) metric systems.

## Features

- Supports both European (cm) and American (inches) metric systems.
- Calculates the volume and weight of the box based on user-provided dimensions.
- Provides the option to choose between cardboard and wood as the box material.

## Functions

### get_volume(length, height, width)

Calculate the volume of the box based on its dimensions.

**Parameters:**
- `length` (float): The length of the box in meters.
- `height` (float): The height of the box in meters.
- `width` (float): The width of the box in meters.

**Returns:**
- `volume` (float): The volume of the box in cubic meters.

### get_volumetric_weight(volume, density)

Calculate the volumetric weight of the box based on its volume and material density.

**Parameters:**
- `volume` (float): The volume of the box in cubic meters.
- `density` (float): The density of the box material in kilograms per cubic meter.

**Returns:**
- `volumetric_weight` (float): The volumetric weight of the box in kilograms.

## Requirements

- Python 3.x

## Getting Started

1. Prerequisites:
   - Python 3.x

2. Clone this repository:

   ```bash
   git clone https://github.com/FuManchuBoy/box-volume-weight-calculator.git
   cd box-volume-weight-calculator

3. Create and activate a virtual environment (optional but recommended):
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

4. Run the program:
   python box_calculator.py
   Using the Frontend (Executable)

If you prefer not to run the program through a development environment, you can use the provided executable file to calculate box volume and volumetric weight without installing Python.

5. Download the latest release of the program from the Releases page.

6. Extract the downloaded ZIP file to a location of your choice.

7. Locate and run the frontend executable (or frontend.exe on Windows).

The program will launch, and you can follow the on-screen instructions to choose the metric system, enter the box dimensions, and select the material.

The results will be displayed in a pop-up window.

Note: The executable is specific to the operating system on which it was created. If you need an executable for a different operating system, you will need to create it separately.

License
This project is licensed under the MIT License.

![License](https://img.shields.io/badge/license-MIT-blue.svg)

Contribution
Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or create a pull request.

Credits
This project was created by Serratore Benito Vittorio.