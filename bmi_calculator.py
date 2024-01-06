import common_functions


UNDERWEIGHT = (0, 18.5)
NORMAL = (18.5, 24.9)
OVERWEIGHT = (25, 29.9)
OBESITY = 30

def get_bmi_category(BMI):
    if BMI >= UNDERWEIGHT[0] and BMI < UNDERWEIGHT[1]:
        return "Underweight"
    elif BMI >= NORMAL[0] and BMI <= NORMAL[1]:
        return "Normal"
    elif BMI >= OVERWEIGHT[0] and BMI <= OVERWEIGHT[1]:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmi(feet, inches, weight):
    height = (feet * 12) + inches
    centimeters = height * 2.54
    kg_weight = weight / 2.2046
    meters = centimeters / 100
    return kg_weight/(meters ** 2)


def main():
    print("BMI Calculator")
    feet = common_functions.get_input("Enter your feet: ")
    inches = common_functions.get_input("Enter your inches: ")
    weight = common_functions.get_input("Enter your weight in (lbs) units: ")
    bmi = calculate_bmi(feet, inches, weight)
    print(f"Your BMI is {bmi:.2f}")
    print(f"You are {get_bmi_category(bmi)}")
    input("Press Enter to exit...")

main()

