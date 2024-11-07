import codesters, random
from codesters import StageClass
stage = StageClass()

player = codesters.Sprite("BasketballHoop")
player.set_size(0.1)
player.go_to(0, -200)
stage.disable_floor()

stage.set_background("Court")

gameOver = False
lives = 5

def move_up(sprite):
    sprite.move_up(1.5)

def move_down(sprite):
    sprite.move_down(1.5)

def move_left(sprite):
    sprite.move_left(2.5)

def move_right(sprite):
    sprite.move_right(2.5)

def show(sprite):
    sprite.show()

def turn_left(sprite):
    heading = sprite.heading
    sprite.set_heading(heading + 1)

def turn_right(sprite):
    heading = sprite.heading
    sprite.set_heading(heading - 1)

def forward(sprite):
    sprite.forward(1)

def hide(sprite):
    sprite.hide()

player.event_key("w", move_up)
player.event_key("s", move_down)
player.event_key("a", move_left)
player.event_key("d", move_right)
player.event_key("h", hide)
player.event_key("g", show)
player.event_key("1", forward)
player.event_key("2", turn_right)
player.event_key("3", turn_left)

def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250, 250)
        object = codesters.Sprite("basketballcool", x_position, 250)
        object.set_size(0.1)
        object.set_y_speed(-10)

stage.event_interval(falling_object, 0.5)

def collision(player, object):
    global lives, gameOver
    
    if object.get_image_name() == "basketballcool":
        stage.remove_sprite(object)
        lives -= 1
        
        if lives <= 0:
            gameOver = True
            print("Game Over! You have no more lives.")
            stage.clear()
        else:
            print(f"Lives remaining: {lives}")

player.event_collision(collision)