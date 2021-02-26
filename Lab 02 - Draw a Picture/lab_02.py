import arcade

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Happy Face Example"

# Open the window. Set the window title and dimensions
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.LIGHT_BLUE)

# Clear screen and start render process
arcade.start_render()

# --- Drawing Commands Will Go Here ---

# Draw the face
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

# Draw the right eye
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the left eye
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the smile
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK,
                        start_angle, end_angle, 10)
# Example
x = 500
y = 500
radius = 40
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

x = 515
y = 515
radius = 4
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 485
y = 515
radius = 4
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

arcade.draw_rectangle_filled(500, 500, 15, 2, arcade.color.BLACK)

# Example 2
x = 100
y = 500
radius = 40
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

x = 115
y = 515
radius = 4
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 85
y = 515
radius = 4
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 100
y = 490
radius = 8
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()