
# Unit Converter

This is a simple Flask-based web application designed to convert various units of **length**, **weight**, and **temperature**. The goal of this project is to provide an easy-to-use tool for performing conversions between different units in these categories. Whether you need to convert inches to centimeters or Celsius to Fahrenheit, this app makes it easy!

## Features

### Length Converter
- Converts between:
  - Millimeters (mm)
  - Centimeters (cm)
  - Meters (m)
  - Kilometers (km)

### Weight Converter
- Converts between:
  - Grams (g)
  - Kilograms (kg)
  - Milligrams (mg)
  - Pounds (lb)
  - Ounces (oz)

### Temperature Converter
- Converts between:
  - Celsius (°C)
  - Fahrenheit (°F)
  - Kelvin (K)

### Easy-to-Use Interface
- A user-friendly web interface to input values and select units for conversion.
- Dynamic conversion results are displayed immediately after the user enters input and selects units.

## Technologies Used

- **Flask**: The lightweight Python web framework used to build the app.
- **Jinja2**: Template engine for dynamically rendering the HTML pages.
- **CSS**: Basic styling is applied through custom CSS to make the application visually appealing.
- **HTML5**: For structuring the pages and handling user input forms.

## Installation

Follow the steps below to get the application up and running on your local machine:

1. **Clone the repository**:

   ```bash
   git clone <https://github.com/mohamedashrf87/Unit-Converter>
   ```

2. **Navigate to the project directory**:

   ```bash
   cd unit-converter
   ```

3. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install required dependencies**:

   The project uses `Flask`. You can install all the dependencies from `requirements.txt` (if provided):

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` doesn't exist, you can install Flask manually:

   ```bash
   pip install Flask
   ```

## Run the code

To run the application, follow these steps:

1. **Start the Flask development server** by running the following command in the terminal:

   ```bash
   python app.py
   ```

2. **Visit the application**:

   After running the above command, you can access the application in your web browser at:

   ```
   http://127.0.0.1:5000/
   ```

   This will load the home page where you can select the conversion category (Length, Weight, Temperature) and start using the app.

### Supported Units

#### Length Units:
- Millimeter (mm)
- Centimeter (cm)
- Meter (m)
- Kilometer (km)

#### Weight Units:
- Gram (g)
- Kilogram (kg)
- Milligram (mg)
- Pound (lb)
- Ounce (oz)

#### Temperature Units:
- Celsius (°C)
- Fahrenheit (°F)
- Kelvin (K)

### Example Conversions

1. **Length**: 
   - Convert 100 centimeters to meters: `100 cm = 1 m`
   - Convert 1 kilometer to millimeters: `1 km = 1,000,000 mm`

2. **Weight**:
   - Convert 2 kilograms to grams: `2 kg = 2000 g`
   - Convert 500 milligrams to ounces: `500 mg = 0.01764 oz`

3. **Temperature**:
   - Convert 25°C to Fahrenheit: `25°C = 77°F`
   - Convert 300 Kelvin to Celsius: `300 K = 26.85°C`

## File Structure

The project contains the following files and directories:

- **app.py**: The main Flask application file that defines the routes for length, weight, and temperature conversions.
- **templates/**: The directory containing the HTML templates.
  - **layout.html**: A base HTML template that includes the common layout for the pages.
  - **length.html**: The page for converting lengths between different units.
  - **weight.html**: The page for converting weights between different units.
  - **temperature.html**: The page for converting temperatures between Celsius, Fahrenheit, and Kelvin.
- **static/**: Contains static files like CSS for styling.
  - **styles.css**: A custom stylesheet for styling the app's pages and forms.
- **requirements.txt**: A file containing the dependencies for the project (if used).



## About Me

I am Mohamed Ashraf Ramadan, from Egypt. I developed this project as part of my learning journey in web development and Flask. I enjoy solving problems and building useful applications that can help people.