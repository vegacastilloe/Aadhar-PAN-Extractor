# Aadhar & PAN Extractor
![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Last Updated](https://img.shields.io/github/last-commit/vegacastilloe/Aadhar-PAN-Extractor)
![Language](https://img.shields.io/badge/language-español-darkred)

#
---
- 🌟 --- CAN YOU SOLVE THIS - EXCEL CHALLENGE 806 ---
- 🌟 **Author**: Excel (Vijay A. Verma) BI

    - Extract Aadhar and PAN numbers from given strings. The pattern followed by Aadhar and PAN:
      - Aadhar: 12 digits: Ex. 487210986345
      - PAN : format is AAAAA9999A where A = English Letter and 9 = Digit : Ex. POIUY6543X
    - In case of multi answer, extract the first occurrence.

 🔰 Este script en Python permite extraer y validar identificadores personales desde cadenas de texto. Utiliza expresiones regulares para detectar: **Aadhar**: `12 dígitos consecutivos` - **PAN**: Formato `AAAAA9999A`.

 🔗 Link to Excel file:
 👉 https://lnkd.in/dNb5yph4

> **My code in Python** 🐍 **for this challenge**
> 
>  🔗 https://github.com/vegacastilloe/Aadhar-PAN-Extractor/blob/main/aadhar_and_pan_extract.py

---
---

## 🆔 Aadhar & PAN Extractor

Este script en Python permite extraer y validar identificadores personales desde cadenas de texto. Utiliza expresiones regulares para detectar:

- **Aadhar**: 12 dígitos consecutivos (ej. `487210986345`)
- **PAN**: Formato `AAAAA9999A` (ej. `POIUY6543X`)

## 📦 Requisitos

- Python 3.7+
- pandas
- re
- tabulate
- Archivo Excel con al menos cuatro columnas:
  - `Names`: nombre de la persona
  - `Strings`: cadena que puede contener Aadhar y/o PAN

---

## 🚀 Cómo funciona

1. Carga el archivo Excel y valida su estructura.
2. Extrae Aadhar y PAN usando expresiones regulares.
3. Compara los valores extraídos con los esperados.
4. Muestra el resultado en formato tabular con indicadores de coincidencia.

---

## 📤 Salida

El script imprime un DataFrame con:

- `Names`, `Strings`, `Aadhar`, `PAN`
- Columnas esperadas desde el Excel
- Columnas `Match1` y `Match2` con valores `True` o `False`

---
## ✨ Output:

| Names  | Strings              | Aadhar        | PAN         | Aadhar Given | PAN Given | Match1 | Match2 |
|-|-|-|-|-|-|-|-|
| Aarav  | A652381472095B3K...  | 652381472095  | ABCDE1234F  | 652381472095 | ABCDE1234F| True   | True   |
| Sanya  | 1239038938PQWRT...   |               | PQWRT9087K  |              | PQWRT9087K| True   | True   |

---

## 🛠️ Personalización

Puedes adaptar el script para:

- Extraer múltiples coincidencias
- Validar otros formatos
- Exportar el resultado a Excel o CSV

## 🚀 Ejecución
```bash
pip install pandas openpyxl
```
```python
aadhar_and_pan_extract.py
```

## 📄 Licencia

Este proyecto está bajo ![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg). Puedes usarlo, modificarlo y distribuirlo libremente.
