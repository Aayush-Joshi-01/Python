import math


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("The value must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")


def calculate_rectangle_area():
    width = get_positive_number("Enter the width of the rectangle: ")
    height = get_positive_number("Enter the height of the rectangle: ")
    return width * height


def calculate_circle_area():
    radius = get_positive_number("Enter the radius of the circle: ")
    return math.pi * radius * radius


def calculate_triangle_area():
    base = get_positive_number("Enter the base of the triangle: ")
    height = get_positive_number("Enter the height of the triangle: ")
    return 0.5 * base * height


def main():
    while True:
        print("Choose a shape to Calculator the area:")
        print("1. Rectangle")
        print("2. Circle")
        print("3. Triangle")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            area = calculate_rectangle_area()
            print(f"The area of the rectangle is {area:.2f}")
        elif choice == '2':
            area = calculate_circle_area()
            print(f"The area of the circle is {area:.2f}")
        elif choice == '3':
            area = calculate_triangle_area()
            print(f"The area of the triangle is {area:.2f}")
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
