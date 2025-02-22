import tkinter as tk
import random

# Constants
grid_size = 20
cell_size = 20
canvas_size = grid_size * cell_size

def move_snake():
    global snake, direction, food, game_over
    if game_over:
        return
    
    head_x, head_y = snake[-1]
    
    if direction == "Up":
        head_y -= 1
    elif direction == "Down":
        head_y += 1
    elif direction == "Left":
        head_x -= 1
    elif direction == "Right":
        head_x += 1
    
    new_head = (head_x, head_y)
    
    if new_head in snake or head_x < 0 or head_x >= grid_size or head_y < 0 or head_y >= grid_size:
        canvas.create_text(canvas_size//2, canvas_size//2, text="Game Over", font=("Arial", 24), fill="red")
        canvas.create_text(canvas_size//2, canvas_size//2 + 30, text="Press Enter to Restart", font=("Arial", 16), fill="white")
        game_over = True
        return
    
    snake.append(new_head)
    
    if new_head == food:
        food = place_food()
    else:
        snake.pop(0)
    
    draw()
    root.after(200, move_snake)

def place_food():
    while True:
        food_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        if food_position not in snake:
            return food_position

def change_direction(new_direction):
    global direction
    opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
    if new_direction != opposite_directions.get(direction, ""):
        direction = new_direction

def restart_game(event):
    global snake, direction, food, game_over
    snake = [(5, 5), (6, 5), (7, 5)]
    direction = "Right"
    food = place_food()
    game_over = False
    draw()
    move_snake()

def draw():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, canvas_size, canvas_size, fill="black", outline="black")
    
    for x, y in snake:
        canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size, fill="pink", outline="white")
    
    fx, fy = food
    canvas.create_rectangle(fx * cell_size, fy * cell_size, (fx + 1) * cell_size, (fy + 1) * cell_size, fill="yellow")

root = tk.Tk()
root.title("Snake Game")

canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="black")
canvas.pack()

snake = [(5, 5), (6, 5), (7, 5)]
direction = "Right"
food = place_food()
game_over = False

draw()
root.bind("<Up>", lambda e: change_direction("Up"))
root.bind("<Down>", lambda e: change_direction("Down"))
root.bind("<Left>", lambda e: change_direction("Left"))
root.bind("<Right>", lambda e: change_direction("Right"))
root.bind("<Return>", restart_game)

root.after(200, move_snake)
root.mainloop()
