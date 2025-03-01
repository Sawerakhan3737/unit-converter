import streamlit as st

st.title("💼 Professional Unit Converter 🚀")
st.write("""
Welcome to the **Professional Unit Converter** app. 
Here, you can convert various units of measurement like length, weight, temperature, and more.
Choose the category of units, select the units you want to convert, and get the result. Let's convert with confidence! 💪
""")

categories = ['Length', 'Weight', 'Temperature', 'Currency']
category = st.selectbox("Select the category of units to convert 🧰", categories)

if category == 'Length':
    st.header("📏 Length Conversion")
    length_units = ['Meters', 'Kilometers', 'Centimeters', 'Millimeters', 'Inches', 'Feet', 'Yards']
    from_unit = st.selectbox("From Unit 📐", length_units)
    to_unit = st.selectbox("To Unit 📏", length_units)
    value = st.number_input(f"Enter value in {from_unit} 🖋️", min_value=0.0)
    if st.button('Convert 🚀'):
        if value > 0:
            # Conversion Logic
            conversion_factors = {
                'Meters': 1,
                'Kilometers': 1000,
                'Centimeters': 0.01,
                'Millimeters': 0.001,
                'Inches': 0.0254,
                'Feet': 0.3048,
                'Yards': 0.9144
            }
            value_in_meters = value * conversion_factors[from_unit]
            converted_value = value_in_meters / conversion_factors[to_unit]
            st.write(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit} 🎯")

elif category == 'Weight':
    st.header("⚖️ Weight Conversion")
    weight_units = ['Kilograms', 'Grams', 'Milligrams', 'Pounds', 'Ounces']
    from_unit = st.selectbox("From Unit ⚖️", weight_units)
    to_unit = st.selectbox("To Unit ⚖️", weight_units)
    value = st.number_input(f"Enter value in {from_unit} 🖋️", min_value=0.0)


    if st.button('Convert 🚀'):
        if value > 0:
            # Conversion Logic
            conversion_factors = {
                'Kilograms': 1,
                'Grams': 0.001,
                'Milligrams': 1e-6,
                'Pounds': 0.453592,
                'Ounces': 0.0283495
            }
            value_in_kg = value * conversion_factors[from_unit]
            converted_value = value_in_kg / conversion_factors[to_unit]
            st.write(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit} 🏋️‍♂️")

elif category == 'Temperature':
    st.header("🌡️ Temperature Conversion")
    temp_units = ['Celsius', 'Fahrenheit', 'Kelvin']
    from_unit = st.selectbox("From Unit 🌡️", temp_units)
    to_unit = st.selectbox("To Unit 🌡️", temp_units)
    value = st.number_input(f"Enter value in {from_unit} 🖋️", min_value=-273.15)

    if st.button('Convert 🚀'):
        if value > -273.15:  # Preventing values below absolute zero
            if from_unit == 'Celsius':
                if to_unit == 'Fahrenheit':
                    converted_value = (value * 9/5) + 32
                elif to_unit == 'Kelvin':
                    converted_value = value + 273.15
                else:
                    converted_value = value
            elif from_unit == 'Fahrenheit':
                if to_unit == 'Celsius':
                    converted_value = (value - 32) * 5/9
                elif to_unit == 'Kelvin':
                    converted_value = (value - 32) * 5/9 + 273.15
                else:
                    converted_value = value
            elif from_unit == 'Kelvin':
                if to_unit == 'Celsius':
                    converted_value = value - 273.15
                elif to_unit == 'Fahrenheit':
                    converted_value = (value - 273.15) * 9/5 + 32
                else:
                    converted_value = value
            st.write(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit} 🌍")

elif category == 'Currency':
    st.header("💵 Currency Conversion")
    st.write("Currently, we have a basic currency conversion feature. You can add more currencies and rates.")
    currencies = ['USD', 'EUR', 'GBP', 'INR', 'JPY']
    from_currency = st.selectbox("From Currency 💸", currencies)
    to_currency = st.selectbox("To Currency 💸", currencies)
    value = st.number_input(f"Enter value in {from_currency} 💰", min_value=0.0)

    if st.button('Convert 🚀'):
        if value > 0:
            # Hardcoded conversion rates for simplicity
            rates = {
                'USD': 1,
                'EUR': 0.92,
                'GBP': 0.83,
                'INR': 82.75,
                'JPY': 134.72
            }
            converted_value = value * rates[to_currency] / rates[from_currency]
            st.write(f"{value} {from_currency} is equal to {converted_value:.2f} {to_currency} 💵")
