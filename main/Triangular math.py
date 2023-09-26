import math

class TrigCalculator:
    def __init__(self):
        self.angle_deg = None
        self.angle_rad = None
        self.trig_function = None
        self.value = None

    def convert_deg_to_rad(self, angle_deg):
        return math.radians(angle_deg)

    def convert_rad_to_deg(self, angle_rad):
        return math.degrees(angle_rad)

    def calculate_trig_values(self):
        self.angle_rad = self.convert_deg_to_rad(self.angle_deg)
        sin_value = math.sin(self.angle_rad)
        cos_value = math.cos(self.angle_rad)
        tan_value = math.tan(self.angle_rad)
        return sin_value, cos_value, tan_value

    def calculate_inverse_trig(self):
        if self.trig_function == "sin":
            self.angle_rad = math.asin(self.value)
        elif self.trig_function == "cos":
            self.angle_rad = math.acos(self.value)
        elif self.trig_function == "tan":
            self.angle_rad = math.atan(self.value)
        else:
            return "Invalid trig function"
        return self.convert_rad_to_deg(self.angle_rad)

def main():
    calculator = TrigCalculator()
    print("Trigonometry Calculator")
    print("1. Calculate Trigonometric Functions")
    print("2. Calculate Inverse Trigonometric Functions")
    choice = int(input("Choose an option (1/2): "))

    if choice == 1:
        calculator.angle_deg = float(input("Enter angle (degrees): "))
        sin_val, cos_val, tan_val = calculator.calculate_trig_values()
        print(f"Sine({calculator.angle_deg} degrees) = {sin_val}")
        print(f"Cosine({calculator.angle_deg} degrees) = {cos_val}")
        print(f"Tangent({calculator.angle_deg} degrees) = {tan_val}")

    elif choice == 2:
        calculator.trig_function = input("Choose trigonometric function (sin, cos, tan): ")
        calculator.value = float(input(f"Enter a value (-1 to 1): "))
        result = calculator.calculate_inverse_trig()
        if isinstance(result, str):
            print(result)
        else:
            print(f"{calculator.trig_function}^-1({calculator.value}) = {result} degrees")

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
