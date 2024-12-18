from owlready2 import *

# Loading the ontology
ontology_path = r"C:\Users\OLAJIDE\Documents\church pc\JEDU\DISSERTATION\Femi Sems 2 Assessments\protege\femi.owx"
onto = get_ontology(ontology_path).load()

# Function to get the formula description from ontology
def get_formula_description(shape):
    if shape == "triangle":
        formula_individual = onto.search_one(iri="*TriangleFormula")
    elif shape == "square":
        formula_individual = onto.search_one(iri="*SquareFormula")
    elif shape == "rectangle":
        formula_individual = onto.search_one(iri="*RectangleFormula")
    else:
        return None

    return formula_individual.comment[0] if formula_individual and formula_individual.comment else "No formula available."

# Validate numeric input
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Area calculation functions with explanations
def calculate_triangle_area(base, height):
    print(f"Step 1: Multiply the base ({base}) by the height ({height}).")
    intermediate = base * height
    print(f"Result: {intermediate}")
    print("Step 2: Divide the result by 2.")
    area = intermediate / 2
    print(f"The final area is: {area}")
    return area

def calculate_square_area(side):
    print(f"Step 1: Multiply the side length ({side}) by itself.")
    area = side * side
    print(f"The final area is: {area}")
    return area

def calculate_rectangle_area(length, width):
    print(f"Step 1: Multiply the length ({length}) by the width ({width}).")
    area = length * width
    print(f"The final area is: {area}")
    return area

# CLI application
def main():
    print("Welcome to the Area Calculator!")
    while True:
        print("\nAvailable shapes: triangle, square, rectangle")
        shape = input("Enter the shape (or type 'exit' to quit): ").lower()

        if shape == "exit":
            print("Goodbye!")
            break

        formula = get_formula_description(shape)
        if not formula:
            print("Invalid shape selected!")
            continue

        print(f"Formula for {shape.capitalize()}: {formula}")
        try:
            if shape == "triangle":
                base = get_positive_float("Enter the base of the triangle: ")
                height = get_positive_float("Enter the height of the triangle: ")
                area = calculate_triangle_area(base, height)
                print(f"The area of the triangle is: {area}")
            elif shape == "square":
                side = get_positive_float("Enter the side length of the square: ")
                area = calculate_square_area(side)
                print(f"The area of the square is: {area}")
            elif shape == "rectangle":
                length = get_positive_float("Enter the length of the rectangle: ")
                width = get_positive_float("Enter the width of the rectangle: ")
                area = calculate_rectangle_area(length, width)
                print(f"The area of the rectangle is: {area}")
        except ValueError:
            print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
