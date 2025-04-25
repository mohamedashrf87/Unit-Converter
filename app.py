from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/length", methods=['GET', 'POST'])
def length():
    length_conversions = {
        'mm': {
            'mm': 1,
            'cm': 0.1,
            'm': 0.001,
            'km': 0.000001
        },
        'cm': {
            'mm': 10,
            'cm': 1,
            'm': 0.01,
            'km': 0.00001
        },
        'm': {
            'mm': 1000,
            'cm': 100,
            'm': 1,
            'km': 0.001
        },
        'km': {
            'mm': 1_000_000,
            'cm': 100_000,
            'm': 1000,
            'km': 1
        }
    }
    if request.method == 'POST':
        length = request.form.get('length')
        unit_convert_from = request.form.get('unit_convert_from')
        unit_convert_to = request.form.get('unit_convert_to')

        result = float(length) * length_conversions[unit_convert_from][unit_convert_to]

        return render_template("length.html", length=length, unit_convert_from=unit_convert_from, unit_convert_to=unit_convert_to, result=result)

    return render_template("length.html")

@app.route("/weight", methods=['GET', 'POST'])
def weight():
    weight_conversions = {
            'g': {
                'g': 1,
                'kg': 0.001,
                'mg': 1000,
                'lb': 0.00220462,
                'oz': 0.035274
            },
            'kg': {
                'g': 1000,
                'kg': 1,
                'mg': 1_000_000,
                'lb': 2.20462,
                'oz': 35.274
            },
            'mg': {
                'g': 0.001,
                'kg': 0.000001,
                'mg': 1,
                'lb': 2.20462e-6,
                'oz': 3.5274e-5
            },
            'lb': {
                'g': 453.592,
                'kg': 0.453592,
                'mg': 453592,
                'lb': 1,
                'oz': 16
            },
            'oz': {
                'g': 28.3495,
                'kg': 0.0283495,
                'mg': 28349.5,
                'lb': 0.0625,
                'oz': 1
            }
        }
    if request.method == 'POST':
        weight = request.form.get('weight')
        unit_convert_from = request.form.get('unit_convert_from')
        unit_convert_to = request.form.get('unit_convert_to')

        result = float(weight) * weight_conversions[unit_convert_from][unit_convert_to]

        return render_template("weight.html", weight=weight, unit_convert_from=unit_convert_from, unit_convert_to=unit_convert_to, result=result)

    return render_template("weight.html")

@app.route("/temperature", methods=['GET', 'POST'])
def temperature():
    if request.method == 'POST':
        temperature = request.form.get('temperature')
        unit_convert_from = request.form.get('unit_convert_from')
        unit_convert_to = request.form.get('unit_convert_to')

        if unit_convert_to == 'C':
            result = convert_to_celsius(temperature, unit_convert_from)
        elif unit_convert_to == 'F':
            result = convert_to_fahrenheit(temperature, unit_convert_from)
        elif unit_convert_to == 'K':
            result = convert_to_kelvin(temperature, unit_convert_from)

        return render_template("temperature.html", temperature=temperature, unit_convert_from=unit_convert_from, unit_convert_to=unit_convert_to, result=result)

    return render_template("temperature.html")

def convert_to_celsius(temperature, unit_convert_from):
    if unit_convert_from == 'F':
        result = (float(temperature) - 32) * 5/9
    elif unit_convert_from == 'K':
        result = float(temperature) - 273.15

    return result

def convert_to_fahrenheit(temperature, unit_convert_from) :
    if unit_convert_from == 'C':
        result = (float(temperature) * 9/5) + 32
    elif unit_convert_from == 'K':
        result = ((float(temperature) - 273.15) * 9/5) + 32

    return result

def convert_to_kelvin(temperature, unit_convert_from):
    if unit_convert_from == 'F':
        result = ((float(temperature) - 32) * 5/9) + 273.15
    elif unit_convert_from == 'C':
        result = float(temperature) + 273.15

    return result

@app.route("/")
def home():
    return redirect(url_for('length'))

if __name__ == "__main__":
    app.run(debug=True)