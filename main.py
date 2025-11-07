from js import document
from pyscript import display

def safe_float(value):
    try:
        return float(value)
    except:
        return 0.0

def calculate_gwa(e=None):
    # get name
    fname = document.getElementById("fname").value.strip()
    lname = document.getElementById("lname").value.strip()

    # get grades
    english = safe_float(document.getElementById("English").value)
    filipino = safe_float(document.getElementById("Filipino").value)
    math = safe_float(document.getElementById("Math").value)
    science = safe_float(document.getElementById("Science").value)
    social = safe_float(document.getElementById("Social_Studies").value)
    pe = safe_float(document.getElementById("PE").value)

    # list and tuple
    subjects = ["English", "Filipino", "Math", "Science", "Social Studies", "PE"]
    units = (3, 3, 3, 3, 2, 2)

    grades = [english, filipino, math, science, social, pe]

    # compute GWA (weighted average)
    total_units = sum(units)
    weighted_sum = sum(g * u for g, u in zip(grades, units))
    gwa = weighted_sum / total_units if total_units else 0

    # create short sentence summary
    result = f"{fname} {lname} got a general weighted average (GWA) of {gwa:.2f}."

    # show it nicely
    document.getElementById("output").innerHTML = result

def refresh_fields(e=None):
    ids = ["fname","lname","English","Filipino","Math","Science","Social_Studies","PE"]
    for i in ids:
        document.getElementById(i).value = ""
    document.getElementById("output").innerHTML = ""