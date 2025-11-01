# ⚙️ Smart Unit Converter

A simple Python CLI project that converts units between kilometers ↔ miles, Celsius ↔ Fahrenheit, and kilograms ↔ pounds.  
This project focuses on logic, clean design, and user-friendly input handling.

---

## 🚀 Features
- Convert between:
  - Kilometers ↔ Miles
  - Celsius ↔ Fahrenheit
  - Kilograms ↔ Pounds
- Clean, easy-to-read console interface  
- Uses modular functions for each conversion  

---

## 🧠 Logic
Each conversion uses standard mathematical formulas:

| Conversion | Formula |
|-------------|----------|
| km → miles | km × 0.621371 |
| miles → km | miles ÷ 0.621371 |
| °C → °F | (°C × 9/5) + 32 |
| °F → °C | (°F − 32) × 5/9 |
| kg → pounds | kg × 2.20462 |
| pounds → kg | pounds ÷ 2.20462 |

---

## 🧩 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/unit-converter.git Unit_converter
