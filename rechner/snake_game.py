import tkinter
import random
import time
import csv

# standart game settings

game_width = 700
game_heigth = 600
speed = 250
space_size = 50
body_parts = 3
snake_color = "blue"
food_color = "red" 
background_color = "black" 


##########################################################################################

class Snake:
    
    def __init__(self):

        self.body_size = body_parts
        self.coordinates = []
        self.squares = []

        for i in range(0, body_parts):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color, tag="SNAKE")
            self.squares.append(square)
        
class Food:
    
    def __init__(self):

        while True:
        
            x = random.randint(0, (game_width / space_size)-1) * space_size
            y = random.randint(0, (game_heigth / space_size)-1) * space_size

            self.coordinates = [x, y]

            global snake

            if not self.check_food_collision(snake):
                break

        self.the_food = canvas.create_oval(x, y, x + space_size, y + space_size, fill=food_color, tag="food")

    def check_food_collision(self, snake):

        x, y = self.coordinates

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True
        return False

def next_turn(snake, food):
    
    x, y =  snake.coordinates[0]

    if direction == "up":
        y -= space_size
    elif direction == "down":
        y += space_size
    elif direction == "left":
        x -= space_size
    elif direction == "right":
        x += space_size

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score
        score += 1
        global label
        label.config(text="Score:{} Highscore:{}".format(score, get_highscore()))

        canvas.delete(food.the_food)
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(speed, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    if new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    if new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    
    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    
    x, y = snake.coordinates[0]

    if x < 0 or x >= game_width:
        return True
    elif y < 0 or y >= game_heigth:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    
    return False

def game_over():
    
    new_highscore = False
    game_over_text = "GAME OVER"

    if get_highscore() == None or score > int(get_highscore()):
        set_highscore(score)
        new_highscore = True

    canvas.destroy()
    
    score_and_highscore_label = tkinter.Label(window, text="Score:{} Highscore:{}".format(score, get_highscore()), font=("consolas", 40))
    score_and_highscore_label.place(relx=0, rely=0, relwidth=1, relheight=0.1)

    if new_highscore:
        game_over_label = tkinter.Label(window, font=("consolas", 70), text=game_over_text, background="red")
        game_over_label.place(relx=0, rely=0.1, relwidth=1, relheight=0.4)
        new_highscore_label = tkinter.Label(window, font=("consolas", 35), text=f"BUT with a \nNEW highscore of {score}!", background="red")
        new_highscore_label.place(relx=0, rely=0.4, relwidth=1, relheight=0.5)

    else:
        game_over_label = tkinter.Label(window, font=("consolas", 70), text=game_over_text, background="red")
        game_over_label.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)

    #window.resizable(True, True) width= window.winfo_height() height= window.winfo_height()
    
    
    new_game_button = tkinter.Button(window, text="New Game", font=("consolas", 20), command=new_game )
    new_game_button.place(relx=0, rely=0.9, relwidth=0.5, relheight=0.1)

    to_the_menu_button = tkinter.Button(window, text="To the Menu", font=("consolas", 20), command=return_to_menu)
    to_the_menu_button.place(relx=0.5, rely=0.9, relwidth=0.5, relheight=0.1)
    
def centered_window(window):

    
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def bind_keys(window):
    
    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))

def get_highscore():
    
    with open("highscores.csv", newline='') as highscore_file:

        highscore = csv.reader(highscore_file)
        for row in highscore:
            return "".join(row)      

def set_highscore(new_highscore):
    
    with open("highscores.csv", 'w', newline='') as highscore_file:

        highscore_writer = csv.writer(highscore_file)
        highscore_writer.writerow([new_highscore])

def default_settings():
    global game_width, game_heigth, speed, space_size, body_parts, snake_color, food_color, background_color
    game_width = 700
    game_heigth = 700
    speed = 250
    space_size = 50
    body_parts = 3
    snake_color = "blue"
    food_color = "red" 
    background_color = "black"

# functions for buttons

def new_game():

    
    
    global window
    window.destroy()
    window = tkinter.Tk()
    window.title("Snake game")
    window.resizable(False, False)

    global score
    score = 0 

    global direction
    direction = "down"

    global label
    label = tkinter.Label(window, text="Score:{} Highscore:{}".format(score, get_highscore()), font=("consolas", 40))
    label.pack()
    

    global canvas
    canvas = tkinter.Canvas(window, bg=background_color, height=game_heigth, width=game_width)
    canvas.pack()

    window.update()

    centered_window(window)

    bind_keys(window)

    global snake
    snake = Snake()
    food = Food()

    next_turn(snake, food)



    window.mainloop()

def change_background_color(new_color):
    global background_color 
    background_color = new_color

def change_snake_color(new_color):
    global snake_color
    snake_color = new_color

def change_food_color(new_color):
    global food_color
    food_color = new_color

def change_snake_speed(new_speed):
    global speed
    speed = new_speed

def change_space_size(new_size):
    global space_size
    space_size = new_size

def change_field_size(new_size):
    game_heigth

def change_snake_length():
    pass

def customize():
    
    global window
    window.destroy()
    window = tkinter.Tk()
    window.title("Snake game")
    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

    customize_label = tkinter.Label(window, background="orange", text="Customization of the Snake Game", font=("consolas", 100))

def return_to_menu():
    
    global window
    window.destroy()
    window = tkinter.Tk()
    window.title("Snake game")

    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

    #centered_window(window)

    snake_game_label = tkinter.Label(window, font=("consolas", 70), background="red", text="Snake game")
    snake_game_label.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    background_color_label = tkinter.Label(window, background="orange")
    background_color_label.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

    customize_button = tkinter.Button(window, font=("consolas", 20), text="Customize", command=customize)
    customize_button.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.2)
    customize_label = tkinter.Label(window, background="orange", font=("consolas", 10), text="The customization of the game settings leads to\nthe not intention of the score as highscore!")
    customize_label.place(relx=0.4, rely=0.5, relheight=0.05, relwidth=0.2)

    new_game_button = tkinter.Button(window, font=("consolas", 20), text="New Game", command=new_game)
    new_game_button.place(relx=0.4, rely=0.55, relheight=0.1, relwidth=0.2)

    exit_button = tkinter.Button(window, font=("consolas", 20), text="Close Game", command=window.destroy)
    exit_button.place(relx=0.4, rely=0.65, relheight=0.1, relwidth=0.2)

    your_highscore = tkinter.Label(window, font=("consolas", 20), background="orange", text=f"Your Highscore:{get_highscore()}")
    your_highscore.place(relx=0.4, rely=0.75, relheight=0.05, relwidth=0.2)



##########################################################################################

def main():

    global window
    window = tkinter.Tk()
    window.title("Snake game")
    window.resizable(False, False)

    global score
    score = 0 

    global direction
    direction = "down"

    global label
    label = tkinter.Label(window, text="Score:{} Highscore:{}".format(score, get_highscore()), font=("consolas", 40))
    label.pack()
    

    global canvas
    canvas = tkinter.Canvas(window, bg=background_color, height=game_heigth, width=game_width)
    canvas.pack()

    window.update()

    centered_window(window)

    bind_keys(window)

    global snake
    snake = Snake()
    food = Food()

    next_turn(snake, food)



    window.mainloop()

##########################################################################################

if __name__ == "__main__":
    main()