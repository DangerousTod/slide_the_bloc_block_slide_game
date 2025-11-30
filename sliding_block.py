import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sliding Block Puzzle")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tile dimensions and grid
TILE_SIZE = 150
GRID_SIZE = 4 # For a 4x4 puzzle
tiles = [[(row * GRID_SIZE + col + 1) for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]
tiles[GRID_SIZE - 1][GRID_SIZE - 1] = 0 # Empty space

t_value = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
target_value = 0
shuffled_value = t_value[:]
random.shuffle(shuffled_value)
#print(shuffled_value)

# Find target value (zero)

def find_index(target_value, shuffled_value):
    for i in range(0, len(shuffled_value)):
        if shuffled_value[i] == target_value:
            return i
    return -1
row_index = find_index(target_value, shuffled_value)

EXTENT = len(t_value) // 4

BOTTOM = 0
TOP = 3
START = 0
my_row_index = 0

while START < EXTENT:
    if BOTTOM <= row_index and row_index <= TOP:
        my_row_index = my_row_index
        break
    else:
        START += 1
        BOTTOM += 4
        TOP += 4
        my_row_index += 1


group_size = 4

grouped_list = [shuffled_value[i:i + group_size] for i in range(0, len(shuffled_value), group_size)]
for lists in grouped_list:

    if lists:
        col_index = find_index(target_value, lists)

        if 0 <= col_index <= 3:
            my_col_index = col_index


num_columns = 4

matrix = [shuffled_value[i:i + num_columns] for i in range(0, len(shuffled_value), num_columns)]

#print("Target value",matrix[my_row_index][my_col_index],"found at row:",my_row_index,"column:",my_col_index)


# Game loop
running = True
while running:
############################################
    row_index = find_index(target_value, shuffled_value)

    EXTENT = len(t_value) // 4
    BOTTOM = 0
    TOP = 3
    START = 0
    my_row_index = 0

    while START < EXTENT:
        if BOTTOM <= row_index and row_index <= TOP:
            my_row_index = my_row_index
            break
        else:
            START += 1
            BOTTOM += 4
            TOP += 4
            my_row_index += 1


    group_size = 4

    grouped_list = [shuffled_value[i:i + group_size] for i in range(0, len(shuffled_value), group_size)]
    for lists in grouped_list:

        if lists:
            col_index = find_index(target_value, lists)

            if 0 <= col_index <= 3:
                my_col_index = col_index


    num_columns = 4

    matrix = [shuffled_value[i:i + num_columns] for i in range(0, len(shuffled_value), num_columns)]

#    print("Target value",matrix[my_row_index][my_col_index],"found at row:",my_row_index,"column:",my_col_index)
############################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYUP:  # Check for key release event
            if event.key == pygame.K_UP:  # Check if the released key is the up arrow
#                print("Up arrow key released!")
                matrix = [shuffled_value[i:i + num_columns] for i in range(0, len(shuffled_value), num_columns)]
                find_index(target_value, shuffled_value)
                if my_row_index > 0:
                    matrix[my_row_index][my_col_index], matrix[my_row_index - 1][my_col_index] = matrix[my_row_index - 1][my_col_index], matrix[my_row_index][my_col_index]

                    shuffled_value = sum(matrix, [])
                else:
                    matrix[my_row_index][my_col_index], matrix[3][my_col_index] = matrix[3][my_col_index], matrix[my_row_index][my_col_index]

                    shuffled_value = sum(matrix, [])

            elif event.key == pygame.K_DOWN:
#                print("Down arrow key released!")
                matrix = [shuffled_value[i:i + num_columns] for i in range(0, len(shuffled_value), num_columns)]
                if my_row_index < 3:
                    matrix[my_row_index][my_col_index], matrix[my_row_index + 1][my_col_index] = matrix[my_row_index + 1][my_col_index], matrix[my_row_index][my_col_index]

                    shuffled_value = sum(matrix, [])
                
                else:
                    matrix[my_row_index][my_col_index], matrix[0][my_col_index] = matrix[0][my_col_index], matrix[my_row_index][my_col_index]

                    shuffled_value = sum(matrix, [])

            elif event.key == pygame.K_LEFT:
#                print("Left arrow key released!")
                matrix = [shuffled_value[i:i + num_columns] for i in range(0, len(shuffled_value), num_columns)]
                if my_col_index > 0:
                    matrix[my_row_index][my_col_index], matrix[my_row_index][my_col_index - 1] = matrix[my_row_index][my_col_index - 1], matrix[my_row_index][my_col_index]

                    shuffled_value = sum(matrix, [])
                
                else:
                    matrix[my_row_index][my_col_index], matrix[my_row_index][3] = matrix[my_row_index][3], matrix[my_row_index][my_col_index]

                    shuffled_value = sum(matrix, [])

            elif event.key == pygame.K_RIGHT:
#                print("Right arrow key released!")
                matrix = [shuffled_value[i:i + num_columns] for i in range(0, len(shuffled_value), num_columns)]
                if my_col_index < 3:

                    matrix[my_row_index][my_col_index], matrix[my_row_index][my_col_index + 1] = matrix[my_row_index][my_col_index + 1], matrix[my_row_index][my_col_index]

                    shuffled_value = sum(matrix, [])

                else:
                    matrix[my_row_index][my_col_index], matrix[my_row_index][0] = matrix[my_row_index][0], matrix[my_row_index][my_col_index]

                    shuffled_value = sum(matrix, [])

            if shuffled_value == t_value:
                pygame.display.set_caption("You Win!!!")
                running = False
                time.sleep(2)
                random.shuffle(shuffled_value)
                print(shuffled_value)
                running = True

    # Drawing
    screen.fill(BLACK)
   
    index = 0

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            tiles[row][col] = shuffled_value[index]
            
            tile_value = tiles[row][col]
            index += 1

                # Draw the tile (e.g., a colored rectangle with the number)
            pygame.draw.rect(screen, WHITE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
            font = pygame.font.Font(None, 74)

            text = font.render(str(tile_value), True, WHITE)

            text_rect = text.get_rect(center=(col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2))
            screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
