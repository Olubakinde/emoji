from sense_hat import SenseHat
import time

sense = SenseHat()

# Define colors
Y = (255, 255, 0)    # Yellow
B = (0, 0, 0)        # Black
R = (255, 0, 0)      # Red
W = (255, 255, 255)  # White
G = (0, 255, 0)      # Green
Bl = (0, 0, 255)     # Blue
O = (255, 165, 0)    # Orange
P = (128, 0, 128)    # Purple
T = (64, 224, 208)   # Turquoise

# Define emoji patterns
smile = [
    B, B, Y, Y, Y, Y, B, B,
    B, Y, B, B, B, B, Y, B,
    Y, B, Y, B, B, Y, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, Y, B, B, Y, B, Y,
    B, Y, B, Y, Y, B, Y, B,
    B, B, Y, B, B, Y, B, B
]

sad = [
    B, B, Y, Y, Y, Y, B, B,
    B, Y, B, B, B, B, Y, B,
    Y, B, Y, B, B, Y, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, B, Y, Y, B, B, Y,
    B, Y, B, B, B, B, Y, B,
    B, B, Y, Y, Y, Y, B, B
]

heart = [
    B, R, R, B, B, R, R, B,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    B, R, R, R, R, R, R, B,
    B, B, R, R, R, R, B, B,
    B, B, B, R, R, B, B, B,
    B, B, B, B, B, B, B, B
]

surprised = [
    B, B, Y, Y, Y, Y, B, B,
    B, Y, B, B, B, B, Y, B,
    Y, B, Y, B, B, Y, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, B, W, W, B, B, Y,
    Y, B, B, W, W, B, B, Y,
    B, Y, B, B, B, B, Y, B,
    B, B, Y, Y, Y, Y, B, B
]

# Additional emojis
wink = [
    B, B, Y, Y, Y, Y, B, B,
    B, Y, B, B, B, Bl, Y, B,
    Y, B, Y, B, B, Y, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, Y, B, B, Y, B, Y,
    B, Y, B, Y, Y, B, Y, B,
    B, B, Y, B, B, Y, B, B
]

laugh = [
    B, B, Y, Y, Y, Y, B, B,
    B, Y, B, B, B, B, Y, B,
    Y, B, Y, B, B, Y, B, Y,
    Y, B, Y, B, B, Y, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, G, B, B, G, B, Y,
    B, Y, B, G, G, B, Y, B,
    B, B, Y, B, B, Y, B, B
]

angry = [
    B, B, R, R, R, R, B, B,
    B, R, B, B, B, B, R, B,
    R, B, R, B, B, R, B, R,
    R, B, B, B, B, B, B, R,
    R, B, B, B, B, B, B, R,
    R, B, B, R, R, B, B, R,
    B, R, B, B, B, B, R, B,
    B, B, R, R, R, R, B, B
]

cool = [
    B, B, Bl, Bl, Bl, Bl, B, B,
    B, Bl, B, B, B, B, Bl, B,
    Bl, W, Bl, B, B, Bl, W, Bl,
    Bl, W, B, B, B, B, W, Bl,
    Bl, B, B, B, B, B, B, Bl,
    Bl, B, B, B, B, B, B, Bl,
    B, Bl, B, Bl, Bl, B, Bl, B,
    B, B, Bl, B, B, Bl, B, B
]

kiss = [
    B, B, Y, Y, Y, Y, B, B,
    B, Y, B, B, B, B, Y, B,
    Y, B, R, B, B, R, B, Y,
    Y, B, B, R, R, B, B, Y,
    Y, B, B, R, R, B, B, Y,
    Y, B, B, B, B, B, B, Y,
    B, Y, B, R, R, B, Y, B,
    B, B, Y, Y, Y, Y, B, B
]

cry = [
    B, B, Y, Y, Y, Y, B, B,
    B, Y, B, B, B, B, Y, B,
    Y, B, Bl, B, B, Bl, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, B, Y, Y, B, B, Y,
    B, Y, Bl, B, B, Bl, Y, B,
    B, B, Y, Y, Y, Y, B, B
]

confused = [
    B, B, Y, Y, Y, Y, B, B,
    B, Y, B, B, B, B, Y, B,
    Y, B, Bl, B, B, W, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, B, B, B, B, B, Y,
    B, Y, B, Y, Y, B, Y, B,
    B, B, Y, B, B, Y, B, B
]

sleeping = [
    B, B, B, Y, Y, B, B, B,
    B, B, Y, B, B, Y, B, B,
    B, Y, B, Y, Y, B, Y, B,
    Y, B, B, B, B, B, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, B, B, B, B, B, Y,
    B, Y, B, Y, Y, B, Y, B,
    B, B, Y, B, B, Y, B, B
]

surprised2 = [
    B, B, Y, Y, Y, Y, B, B,
    B, Y, B, B, B, B, Y, B,
    Y, B, B, W, W, B, B, Y,
    Y, B, W, W, W, W, B, Y,
    Y, B, W, W, W, W, B, Y,
    Y, B, B, W, W, B, B, Y,
    B, Y, B, B, B, B, Y, B,
    B, B, Y, Y, Y, Y, B, B
]

blushing = [
    B, B, Y, Y, Y, Y, B, B,
    B, Y, B, B, B, B, Y, B,
    Y, Bl, Y, B, B, Y, Bl, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, Y, B, B, Y, B, Y,
    B, Y, B, Y, Y, B, Y, B,
    B, B, Y, B, B, Y, B, B
]

party = [
    B, Y, Y, Y, Y, Y, Y, B,
    Y, B, B, B, B, B, B, Y,
    Y, B, R, B, B, R, B, Y,
    Y, B, B, G, G, B, B, Y,
    Y, B, B, G, G, B, B, Y,
    Y, B, R, B, B, R, B, Y,
    Y, B, B, B, B, B, B, Y,
    B, Y, Y, Y, Y, Y, Y, B
]

devil = [
    R, R, R, R, R, R, R, R,
    R, B, R, R, R, R, B, R,
    R, B, B, R, R, B, B, R,
    R, B, B, B, B, B, B, R,
    R, B, W, B, B, W, B, R,
    R, B, B, B, B, B, B, R,
    R, B, B, B, B, B, B, R,
    R, R, R, R, R, R, R, R
]

alien = [
    B, B, G, G, G, G, B, B,
    B, G, G, G, G, G, G, B,
    G, G, Bl, G, G, Bl, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, B, G, G, G, G, B, G,
    G, B, B, G, G, B, B, G,
    G, B, B, G, G, B, B, G
]

robot = [
    B, B, B, Bl, Bl, B, B, B,
    B, Bl, Bl, Bl, Bl, Bl, Bl, B,
    Bl, B, B, Bl, Bl, B, B, Bl,
    Bl, Bl, Bl, Bl, Bl, Bl, Bl, Bl,
    Bl, Bl, Bl, Bl, Bl, Bl, Bl, Bl,
    Bl, Bl, Bl, Bl, Bl, Bl, Bl, Bl,
    Bl, Bl, Bl, B, B, Bl, Bl, Bl,
    Bl, Bl, Bl, Bl, Bl, Bl, Bl, Bl
]

star = [
    B, B, B, Y, Y, B, B, B,
    B, B, Y, Y, Y, Y, B, B,
    B, Y, Y, Y, Y, Y, Y, B,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    B, Y, Y, Y, Y, Y, Y, B,
    B, B, Y, Y, Y, Y, B, B,
    B, B, B, Y, Y, B, B, B
]

heart2 = [
    B, R, R, B, B, R, R, B,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    B, R, R, R, R, R, R, B,
    B, B, R, R, R, R, B, B,
    B, B, B, R, R, B, B, B,
    B, B, B, B, B, B, B, B
]

# List of emojis
emojis = [
    smile, sad, heart, surprised, wink, laugh, angry, cool, kiss, cry,
    confused, sleeping, surprised2, blushing, party, devil, alien, robot, star, heart2
]
emoji_index = 0

# Display the first emoji
sense.set_pixels(emojis[emoji_index])

# Function to handle joystick events
def handle_joystick(event):
    global emoji_index
    if event.action == "pressed":
        if event.direction == "up":
            emoji_index = (emoji_index + 1) % len(emojis)
        elif event.direction == "down":
            emoji_index = (emoji_index - 1) % len(emojis)
        elif event.direction in ["left", "right"]:
            emoji_index = (emoji_index + 1) % len(emojis)
        sense.set_pixels(emojis[emoji_index])

# Attach the joystick event handler
sense.stick.direction_any = handle_joystick

# Keep the script running to listen for events
while True:
    time.sleep(0.1)
