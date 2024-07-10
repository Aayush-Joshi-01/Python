import turtle
import time


# Function to initialize the screen and set up the rods
def setup_towers():
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Set up the rods
    rod_a = turtle.Turtle()
    rod_a.speed(0)
    rod_a.color("black")
    rod_a.goto(-200, 0)

    rod_b = turtle.Turtle()
    rod_b.speed(0)
    rod_b.color("black")
    rod_b.goto(0, 0)

    rod_c = turtle.Turtle()
    rod_c.speed(0)
    rod_c.color("black")
    rod_c.goto(200, 0)

    return rod_a, rod_b, rod_c


# Modified Tower of Hanoi function with visualization
def tower_of_hanoi(n, source, destination, auxiliary, count):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return count
    input("Press Enter to continue...")
    # Draw the current state before moving
    draw_state(n, source, auxiliary, destination)
    input("Press Enter to continue...")
    tower_of_hanoi(n - 1, source, auxiliary, destination, count + 1)
    input("Press Enter to continue...")
    print("Move disk", n, "from", source, "to", destination)

    # Update the state after moving
    draw_state(n, auxiliary, destination, source)

    tower_of_hanoi(n - 1, auxiliary, destination, source, count + 1)


# Function to draw the current state of the towers
def draw_state(n, source, auxiliary, destination):
    # Clear previous drawings
    source.clear()
    auxiliary.clear()
    destination.clear()

    # Draw the rods
    source.penup()
    source.goto(-200, 0)
    source.pendown()
    auxiliary.penup()
    auxiliary.goto(0, 0)
    auxiliary.pendown()
    destination.penup()
    destination.goto(200, 0)
    destination.pendown()

    # Draw the disks
    for i in range(n, 0, -1):
        source.circle(i * 10)
        auxiliary.circle((n - i + 1) * 10)
        destination.circle((n - i + 2) * 10)

    # Label the rods
    source.write("Source", align="center", font=("Arial", 16, "normal"))
    auxiliary.write("Auxiliary", align="center", font=("Arial", 16, "normal"))
    destination.write("Destination", align="center", font=("Arial", 16, "normal"))


# Main function to run the animation
def main():
    rod_a, rod_b, rod_c = setup_towers()
    tower_of_hanoi(5, rod_a, rod_b, rod_c, 0)
    turtle.done()


if __name__ == '__main__':
    main()
