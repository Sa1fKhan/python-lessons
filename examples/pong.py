import sys  # Import system-specific parameters and functions
import pygame  # Import Pygame library for game development
from pygame.locals import QUIT  # Import QUIT to handle window close event

# Initialize Pygame
pygame.init()  # Initializes all the Pygame modules
clock = pygame.time.Clock()  # Create a Clock object to manage the frame rate
fps = 60  # Frames per second, the speed at which the game updates

# Timer settings
countdown_time = 10  # countdown from 10 seconds
start_ticks = pygame.time.get_ticks()  # get start ticks

# Define colors using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
GREEN = (50, 255, 50)
BROWN = (255, 98, 0)
PINK = (255, 0, 234)

# Set up the display
screen = pygame.display.set_mode((600, 600))  # Create a window of size 600x600 pixels
pygame.display.set_caption("PONG")  # Set the window title to "PONG"

# Define paddle boundaries
paddle_minYPos = 0  # Minimum Y position for the paddles
paddle_maxYPos = 500  # Maximum Y position for the paddles

# Initialize paddle positions and speeds
paddleL_currYPos = 300  # Initial Y position of the left paddle
paddleL_currSpeed = 0  # Initial speed of the left paddle

paddleR_currYPos = 300  # Initial Y position of the right paddle
paddleR_currSpeed = 0  # Initial speed of the right paddle

# Initialize ball position and speed
ball_x = 300  # Initial X position of the ball
ball_y = 300  # Initial Y position of the ball
ball_speed_x = 5  # Speed of the ball in X direction
ball_speed_y = 5  # Speed of the ball in Y direction

# Initialize scores
scoreL = 0  # Score for the left player
scoreR = 0  # Score for the right player


def handle_events():
    """
    This function handles all the events, like key presses and window closing.
    """
    global paddleR_currSpeed, paddleL_currSpeed
    for event in pygame.event.get():  # Get all the events
        if event.type == QUIT:  # Check if the event is QUIT (close window)
            pygame.quit()  # Uninitialize all Pygame modules
            sys.exit()  # Exit the program

        if event.type == pygame.KEYDOWN:  # Check if a key is pressed down
            print(str(event.key))
            if event.key == pygame.K_UP:  # If the UP arrow key is pressed
                paddleR_currSpeed = -10  # Move the right paddle up
            elif event.key == pygame.K_DOWN:  # If the DOWN arrow key is pressed
                paddleR_currSpeed = 10  # Move the right paddle down
            elif event.key == pygame.K_w:  # If the 'w' key is pressed
                paddleL_currSpeed = -10  # Move the left paddle up
            elif event.key == pygame.K_s:  # If the 's' key is pressed
                paddleL_currSpeed = 10  # Move the left paddle down

        if event.type == pygame.KEYUP:  # Check if a key is released
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddleR_currSpeed = 0  # Stop the right paddle
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddleL_currSpeed = 0  # Stop the left paddle


def update_paddle_position():
    """
    This function updates the positions of the paddles based on their speeds.
    """
    global paddleL_currYPos, paddleL_currSpeed, paddleR_currYPos, paddleR_currSpeed
    # Update the left paddle's position if it's within the boundaries
    if paddleL_currYPos > paddle_minYPos and paddleL_currYPos < paddle_maxYPos:
        paddleL_currYPos += paddleL_currSpeed  # Update the Y position
    elif paddleL_currYPos <= paddle_minYPos:  # If it hits the top boundary
        paddleL_currYPos = paddle_minYPos + 1  # Set it slightly inside the boundary
        paddleL_currSpeed = 0  # Stop the paddle
    elif paddleL_currYPos >= paddle_maxYPos:  # If it hits the bottom boundary
        paddleL_currYPos = paddle_maxYPos - 1  # Set it slightly inside the boundary
        paddleL_currSpeed = 0  # Stop the paddle

    # Update the right paddle's position if it's within the boundaries
    if paddleR_currYPos > paddle_minYPos and paddleR_currYPos < paddle_maxYPos:
        paddleR_currYPos += paddleR_currSpeed  # Update the Y position
    elif paddleR_currYPos <= paddle_minYPos:  # If it hits the top boundary
        paddleR_currYPos = paddle_minYPos + 1  # Set it slightly inside the boundary
        paddleR_currSpeed = 0  # Stop the paddle
    elif paddleR_currYPos >= paddle_maxYPos:  # If it hits the bottom boundary
        paddleR_currYPos = paddle_maxYPos - 1  # Set it slightly inside the boundary
        paddleR_currSpeed = 0  # Stop the paddle


def update_ball_position():
    """
    This function updates the position of the ball and handles collisions.
    """
    global ball_x, ball_y, ball_speed_x, ball_speed_y, scoreL, scoreR

    # Update the ball's position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top or bottom
    if ball_y <= 0 or ball_y >= 600:
        ball_speed_y *= -1  # Reverse the vertical direction

    # Ball collision with left paddle only if it's on the right side of the paddle
    if ball_x <= 100 and ball_x >= 95:
        if paddleL_currYPos <= ball_y <= paddleL_currYPos + 100:
            ball_speed_x *= -1  # Reverse the horizontal direction

    # Ball collision with right paddle only if it's on the left side of the paddle
    if ball_x >= 500 and ball_x <= 505:
        if paddleR_currYPos <= ball_y <= paddleR_currYPos + 100:
            ball_speed_x *= -1  # Reverse the horizontal direction

    # Ball goes out of bounds on the left side
    if ball_x <= 0:
        scoreR += 1  # Increment the right player's score
        reset_ball()  # Reset the ball position

    # Ball goes out of bounds on the right side
    if ball_x >= 600:
        scoreL += 1  # Increment the left player's score
        reset_ball()  # Reset the ball position


def reset_ball():
    """
    This function resets the ball to the center of the screen.
    """
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x, ball_y = 300, 300  # Reset ball to the center
    ball_speed_x *= -1  # Change direction to serve to the other player


def draw_objects():
    """
    This function draws the paddles, ball, and other objects on the screen.
    """
    screen.fill(BLACK)  # Fill the screen with black color to clear it
    # Draw the left paddle
    pygame.draw.rect(screen, PINK, (50, paddleL_currYPos, 50, 100))
    # Draw the right paddle
    pygame.draw.rect(screen, BROWN, (500, paddleR_currYPos, 50, 100))
    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), 10)
    # Draw the scores
    draw_text(str(scoreL), 150, 50)
    draw_text(str(scoreR), 450, 50)

    # Draw the timer
    countdown_text = get_countdown_time()
    draw_text(str(countdown_text), 250, 200)

    pygame.display.update()  # Update the display with the new drawings


def draw_text(text, x, y):
    """
    This function draws text on the screen.
    """
    font = pygame.font.Font(None, 74)  # Set the font and size
    text = font.render(text, True, WHITE)  # Render the text
    screen.blit(text, (x, y))  # Draw the text on the screen


def get_countdown_time():
    # Calculate the elapsed milliseconds since the countdown started
    elapsed_ticks = pygame.time.get_ticks() - start_ticks

    # Convert elapsed milliseconds to seconds
    elapsed_seconds = elapsed_ticks // 1000

    # Calculate the current countdown time in seconds
    current_seconds = countdown_time - elapsed_seconds

    # Check if the countdown is finished
    if current_seconds < 0:
        current_seconds = 0

    return current_seconds


"""
This is the main function that runs the game loop.
"""


def main():
    while True:  # Infinite loop to keep the game running
        handle_events()  # Handle user input and events
        update_paddle_position()  # Update paddle positions based on input
        update_ball_position()  # Update ball position and handle collisions

        draw_objects()  # Draw the updated game objects on the screen

        clock.tick(fps)  # Ensure the game runs at the specified frame rate

        if scoreL >= 10:
            print("L player wins!")
        elif scoreR >= 10:
            print("R player wins!")


if __name__ == "__main__":
    main()  # Call the main function to start the game
