import turtle

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def write_text(text, x, y, font_size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color("black")
    turtle.write(text, align="center", font=("Arial", font_size, "bold"))

def draw_shohid_minar(x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("gray")
    base_height = height // 5
    column_width = width // 12
    column_gap = column_width * 2
    column_height = height - base_height

    # Base rectangle
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(base_height)
        turtle.left(90)
    turtle.end_fill()

    # Draw columns (2 side + 1 center)
    for offset in [-2 * column_gap, -column_gap, 0, column_gap, 2 * column_gap]:
        turtle.penup()
        turtle.goto(x + width // 2 + offset - column_width // 2, y + base_height)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(column_width)
            turtle.left(90)
            turtle.forward(column_height if offset != 0 else column_height + base_height // 2)
            turtle.left(90)
        turtle.end_fill()

    # Draw arcs for the realistic top
    for offset in [-2 * column_gap, -column_gap, 0, column_gap, 2 * column_gap]:
        turtle.penup()
        turtle.goto(x + width // 2 + offset, y + base_height + column_height)
        turtle.setheading(0)
        turtle.pendown()
        turtle.circle(column_width // 2, 180)

    # Add a small top column at the center
    small_column_width = column_width // 2
    small_column_height = column_height // 3
    turtle.penup()
    turtle.goto(x + width // 2 - small_column_width // 2, y + base_height + column_height)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(small_column_width)
        turtle.left(90)
        turtle.forward(small_column_height)
        turtle.left(90)
    turtle.end_fill()

def draw_art():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Victory Day - Bangladesh")

    # Draw the green background (flag base)
    draw_rectangle("green", -200, -100, 400, 200)

    # Draw the red circle (flag symbol)
    draw_circle("red", 0, 0, 60)

    # Draw Shohid Minar realistically outside the flag with red circle background
    draw_circle("red", 10, 180, 25)  # Red sun background for Shohid Minar
    draw_shohid_minar(-15, 130, 50, 100)

    # Add the Victory Day text
    write_text("\u09AC\u09BF\u099C\u09AF\u09BC \u09A6\u09BF\u09AC\u09B8 ১৬ ডিসেম্বর", 0, -150, 20)
    write_text("Victory Day of Bangladesh", 0, -180, 15)

    # Add 'NUBCC' and 'Developed By Fahim Sharia' at the top corner
    write_text("NUBCC", -200, 160, 12)
    write_text("Developed By Fahim Shariar", -200, 140, 10)

    turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_art()
