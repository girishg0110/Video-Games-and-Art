import pygame
import random
import math
import os


def color_from_key(keys, color):
    if (keys[pygame.K_1]):  # RED
        return (255, 0, 0)
    if (keys[pygame.K_2]):  # ORANGE
        return (255, 127, 0)
    if (keys[pygame.K_3]):  # YELLOW
        return (255, 255, 0)
    if (keys[pygame.K_4]):  # GREEN
        return (0, 255, 0)
    if (keys[pygame.K_5]):  # BLUE
        return (0, 0, 255)
    if (keys[pygame.K_6]):  # VIOLET
        return (139, 0, 255)
    if (keys[pygame.K_7]):  # PINK
        return (255, 20, 147)
    if (keys[pygame.K_8]):  # BROWN
        return (139, 69, 19)
    if (keys[pygame.K_9]):  # BLACK
        return (0, 0, 0)
    if (keys[pygame.K_0]):  # WHITE
        return (255, 255, 255)
    return color


def color_from_int(integ):
    if (integ == 1):  # RED
        return (255, 0, 0)
    if (integ == 2):  # ORANGE
        return (255, 127, 0)
    if (integ == 3):  # YELLOW
        return (255, 255, 0)
    if (integ == 4):  # GREEN
        return (0, 255, 0)
    if (integ == 5):  # BLUE
        return (0, 0, 255)
    if (integ == 6):  # VIOLET
        return (139, 0, 255)
    if (integ == 7):  # PINK
        return (255, 20, 147)
    if (integ == 8):  # BROWN
        return (139, 69, 19)
    if (integ == 9):  # BLACK
        return (0, 0, 0)
    return (255, 255, 255)  # WHITE


def invert_color(color):
    return (255-color[0], 255-color[1], 255-color[2])


def draw_menu(canvas, menu_color, menu_width, menu_font, dims):
    fill_background(canvas, invert_color(menu_color),
                    (0, 0, menu_width, dims[1]))
    pygame.draw.line(canvas, menu_color, (0, 0), (0, dims[1]), 5)
    pygame.draw.line(canvas, menu_color, (menu_width, 0),
                     (menu_width, dims[1]), 5)
    for i in range(11):
        pygame.draw.line(canvas, menu_color,
                         (0, menu_width*i), (menu_width, menu_width*i), 5)
    for i in range(10):
        menu_square = (menu_width//10, menu_width * i +
                       menu_width//10, menu_width*8//10, menu_width*8//10)
        pygame.draw.rect(canvas, color_from_int(i), menu_square)
        text_surface = menu_font.render(str(i), True, (menu_color if color_from_int(i) != menu_color
                                                       else (255-menu_color[0], 255-menu_color[1], 255-menu_color[2])))
        canvas.blit(text_surface, menu_square)


def fill_background(canvas, background_color, rect):
    pygame.draw.rect(canvas, background_color, rect)


def line_data_extract(line_str):
    color_list = line_str[1:line_str.index(')')].split(', ')
    line_str = line_str[line_str.index(')') + 1:]
    point_1_list = line_str[1:line_str.index(')')].split(', ')
    line_str = line_str[line_str.index(')') + 1:]
    point_2_list = line_str[1:line_str.index(')')].split(', ')
    line_str = line_str[line_str.index(')') + 1:]
    thickness = int(line_str)

    for i in range(3):
        color_list[i] = int(color_list[i])
    for i in range(2):
        point_1_list[i] = int(point_1_list[i])
    for i in range(2):
        point_2_list[i] = int(point_2_list[i])

    return (color_list, point_1_list, point_2_list, thickness)


def main():
    # Intro
    print("\n\nWelcome to PyPaint!")
    print("Here, you can make and save original compositions.")

    print("\n\nClick on the boxes along the left-hand side to select brush color.")
    print("This can also be done using the numbers as indicated.")
    print("\nTo change the thickness of the brush, use the up and down arrow keys.")
    print("An indicator in the upper right-hand corner of the window will reflect these changes.")
    print('\nHit the "space" key to reset the canvas to its original color.')
    print("Pressing 'F' and selecting a color will change the background color of the canvas.")
    print("\nPressing 'R' after placing the first point of a line will reset that point.")
    print("\nPressing 'A' will create a RANDOM composition of how many ever lines you specify.")
    print("\nFinally, pressing 'S' will prompt you to enter a file name for your composition under which to save it.")

    input("\n\n\nAll set? Hit the enter key when you're ready to get started!")

    pygame.init()
    pygame.display.set_caption("PyPaint")

    # Canvas Setup
    dims = (800, 800)
    canvas = pygame.display.set_mode(dims)
    background_color = (0, 0, 0)

    # Initial Brush Settings
    thickness = 2
    color = (255, 255, 255)
    first_pair = ()

    # COLOR MENU
    menu_color = (0, 0, 0) if background_color != (
        0, 0, 0) else (255, 255, 255)
    menu_width = dims[0]//10
    menu_font = pygame.font.SysFont("impact", menu_width//3)
    menu_rect = (0, 0, menu_width, dims[1])  # full menu
    canvas_rect = (menu_width, 0, dims[0] - menu_width, dims[1])

    fill_background(canvas, background_color, canvas_rect)
    draw_menu(canvas, menu_color, menu_width, menu_font, dims)
    pygame.display.flip()

    root = os.getcwd()
    # each line is (COLOR)(POINT1)(POINT2)(THICKNESS)
    instructions = str(background_color) + str(dims)

    filling_mode = False
    running = True
    while running:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Why is this inside the event loop?
            #       Mouse clicks are continuous, so this controls the input somewhat
            if (pygame.mouse.get_pressed()[0]):
                if (pygame.mouse.get_pos()[0] > menu_width):
                    if (len(first_pair) == 0):
                        first_pair = pygame.mouse.get_pos()
                    else:
                        second_pair = pygame.mouse.get_pos()
                        pygame.draw.line(
                            canvas, color, first_pair, second_pair, thickness)
                        instructions = instructions + "\n" + \
                            str(color) + str(first_pair) + \
                            str(second_pair) + str(thickness)
                        first_pair = ()
                else:
                    if (filling_mode):
                        background_color = color_from_int(
                            pygame.mouse.get_pos()[1]//menu_width)
                        pygame.draw.rect(canvas, background_color, canvas_rect)
                        filling_mode = False
                        instructions = str(background_color)

                    color = color_from_int(
                        pygame.mouse.get_pos()[1]//menu_width)

        # Hotkeys
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP]):
            thickness = thickness + \
                1 if thickness < (min(dims)-50)//2 else thickness
        if (keys[pygame.K_DOWN]):
            thickness = thickness - 1 if thickness > 1 else thickness
        if (keys[pygame.K_SPACE]):
            fill_background(canvas, background_color, canvas_rect)
            draw_menu(canvas, menu_color, menu_width, menu_font, dims)
            pygame.display.flip()
            instructions = str(background_color)
            first_pair = ()
        if (keys[pygame.K_s]):
            # Images
            thickness = 2
            save_choice = input(
                "\nWould you like to save a JPG image of your canvas(y/n)? ")
            image_name = ""
            if (save_choice != 'n'):
                while True:
                    image_name = input("\tEnter name of composition: ")
                    full_path = root + r"\Compositions" + r"\\" + image_name + ".jpg"
                    if (not os.path.exists(full_path)):
                        break
                    else:
                        print("A file with this name already exists.")

                pygame.image.save(canvas.subsurface(canvas_rect), full_path)

                print(full_path)
            # Instructions
            instruct_choice = input(
                "\nWould you like to save the instructions (y/n)? ")
            instruct_name = image_name
            if (instruct_choice != 'n'):
                if (len(instruct_name) == 0):
                    instruct_name = input("\tEnter name of composition: ")

                full_path = root + r"\Instructions" + \
                    r"\Instructions - " + instruct_name + ".txt"
                f = open(full_path, "w")
                f.write(instructions)
                print(instructions)

                print(full_path)
                f.close()
        if (keys[pygame.K_d]):  # decode a text file
            # array of line objects
            print(os.listdir("./Instructions/"))
            file_name = input("\nWhat file are you reading? ")
            full_path = root + r"\Instructions" + "\Instructions - " + file_name + ".txt"
            if (os.path.exists(full_path)):
                f = open(full_path, "r")
                background_color_arr = f.readline().split(', ')
                background_color = (int(background_color_arr[0][1:]), int(
                    background_color_arr[1]), int(background_color_arr[2][:-2]))
                pygame.draw.rect(canvas, background_color, canvas_rect)

                line_info_arr = f.readlines()[1:]
                for line in line_info_arr:
                    parsed_line = line_data_extract(line)
                    color = (parsed_line[0][0],
                             parsed_line[0][1], parsed_line[0][2])
                    pygame.draw.line(canvas, color, (parsed_line[1][0], parsed_line[1][1]),
                                     (parsed_line[2][0], parsed_line[2][1]), parsed_line[3])
                firstPair = ()
                draw_menu(canvas, menu_color, menu_width, menu_font, dims)
                f.close()
            else:
                print("File not found!")
        if (keys[pygame.K_a]):  # random sequence of n lines
            rand_choice = input(
                "\nWould you like to create a random composition(y/n)? ")
            if (rand_choice == 'y'):
                rand_line_total = int(
                    input("\nNumber of randomly generated lines: "))
                pygame.draw.rect(canvas, background_color, canvas_rect)
                for i in range(rand_line_total):
                    color = color_from_int(random.randint(0, 9))
                    # thickness goes (1,(min(dims)-50)//2)
                    thickness = random.randint(1, (min(dims)-50)//2)
                    first_pair = (random.randint(menu_width, dims[0]), random.randint(
                        0, dims[1]))  # X goes (menuWidth, dims[0])
                    second_pair = (random.randint(menu_width, dims[0]), random.randint(
                        0, dims[1]))  # Y goes (0, dims[1])

                    pygame.draw.line(canvas, color, first_pair,
                                     second_pair, thickness)
                    instructions = instructions + "\n" + \
                        str(color) + str(first_pair) + \
                        str(second_pair) + str(thickness)

                thickness = 2
                first_pair = ()
                second_pair = ()
        if (keys[pygame.K_r]):
            first_pair = ()
        if (keys[pygame.K_f]):
            filling_mode = True

        color = color_from_key(keys, color)
        # Information about Brush
        pygame.draw.rect(canvas, color, (dims[0] - 10, 0, 10, thickness))
        pygame.draw.rect(canvas, background_color,
                         (dims[0] - 10, thickness, 10, dims[1] - thickness))

        pygame.display.update(canvas_rect)


if __name__ == "__main__":
    main()
