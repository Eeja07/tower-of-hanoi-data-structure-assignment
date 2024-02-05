import pygame
import sys

white = (255, 255, 255)
sky_blue = (135, 206, 250)
blue = (0, 0, 255)
black = (0, 0, 0)

input_string = "0"
you_win = False


def window1(screen):
    rectangles = [
        pygame.Rect(370, 200, 60, 25),
        pygame.Rect(350, 225, 100, 25),
        pygame.Rect(330, 250, 140, 25),
        pygame.Rect(310, 275, 180, 25),
        pygame.Rect(290, 300, 220, 25),
        pygame.Rect(270, 325, 260, 25),
    ]

    rect1 = pygame.Rect(395, 150, 10, 200)
    rect2 = pygame.Rect(250, 350, 300, 10)

    playButton = pygame.Rect(250, 380, 145, 35)
    exitButton = pygame.Rect(405, 380, 145, 35)

    pygame.draw.rect(screen, black, playButton)
    pygame.draw.rect(screen, black, exitButton)

    pygame.draw.rect(screen, black, rect1)
    pygame.draw.rect(screen, black, rect2)

    title_font = pygame.font.Font(None, 48)
    title_text = title_font.render("Tower Of Hanoi", True, black)
    title_rect = title_text.get_rect(center=(800 // 2, 100))

    # Render text
    font = pygame.font.Font(None, 24)
    play_text = font.render('PLAY', True, white)
    exit_text = font.render('EXIT', True, white)

    # Get the text rectangle and center it inside the buttons
    play_text_rect = play_text.get_rect(center=playButton.center)
    exit_text_rect = exit_text.get_rect(center=exitButton.center)

    # Blit text onto the screen
    screen.blit(play_text, play_text_rect)
    screen.blit(exit_text, exit_text_rect)
    screen.blit(title_text, title_rect)

    # Draw rectangles with sky blue fill and blue border
    for rect in rectangles:
        pygame.draw.rect(screen, sky_blue, rect)
        pygame.draw.rect(screen, blue, rect, 2)  # Draw border with thickness 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playButton.collidepoint(event.pos):
                return "window2"
            elif exitButton.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    # Update the display
    pygame.display.update()

def window2(screen):
    global input_string

    rectangles = [
        pygame.Rect(370, 200, 60, 25),
        pygame.Rect(350, 225, 100, 25),
        pygame.Rect(330, 250, 140, 25),
        pygame.Rect(310, 275, 180, 25),
        pygame.Rect(290, 300, 220, 25),
        pygame.Rect(270, 325, 260, 25),
    ]

    rect1 = pygame.Rect(395, 150, 10, 200)
    rect2 = pygame.Rect(250, 350, 300, 10)

    pygame.draw.rect(screen, black, rect1)
    pygame.draw.rect(screen, black, rect2)

    title_font = pygame.font.Font(None, 48)
    title_text = title_font.render("GAME MODE", True, black)
    title_rect = title_text.get_rect(center=(800 // 2, 100))

    manualButton = pygame.Rect(250, 415, 145, 35)
    autoButton = pygame.Rect(405, 415, 145, 35)
    upButton = pygame.Rect(250, 370, 70, 35)
    downButton = pygame.Rect(480, 370, 70, 35)
    inputBox = pygame.Rect(330, 370, 140, 35)

    pygame.draw.rect(screen, black, manualButton)
    pygame.draw.rect(screen, black, autoButton)
    pygame.draw.rect(screen, black, upButton)
    pygame.draw.rect(screen, black, downButton)
    pygame.draw.rect(screen, black, inputBox)

    # Render text
    font = pygame.font.Font(None, 24)
    manual_text = font.render('MANUAL', True, white)
    auto_text = font.render('AUTO', True, white)
    up_text = font.render('UP', True, white)
    down_text = font.render('DOWN', True, white)
    input_text = font.render(f'HANOI: {input_string}', True, white)

    # Get the text rectangle and center it inside the buttons
    manual_text_rect = manual_text.get_rect(center=manualButton.center)
    auto_text_rect = auto_text.get_rect(center=autoButton.center)
    up_text_rect = up_text.get_rect(center=upButton.center)
    down_text_rect = down_text.get_rect(center=downButton.center)
    input_text_rect = input_text.get_rect(center=inputBox.center)

    # Blit text onto the screen
    screen.blit(manual_text, manual_text_rect)
    screen.blit(auto_text, auto_text_rect)
    screen.blit(up_text, up_text_rect)
    screen.blit(down_text, down_text_rect)
    screen.blit(input_text, input_text_rect)
    screen.blit(title_text, title_rect)

    # Draw rectangles with sky blue fill and blue border
    for rect in rectangles:
        pygame.draw.rect(screen, sky_blue, rect)
        pygame.draw.rect(screen, blue, rect, 2)  # Draw border with thickness 2


    # Get events once
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_string = input_string[:-1]  # Remove the last character
            elif event.unicode.isdigit():
                input_string += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if manualButton.collidepoint(event.pos):
                return "window3"
            elif autoButton.collidepoint(event.pos):
                return "window4"
            elif upButton.collidepoint(event.pos):
                try:
                    input_string = str(int(input_string) + 1)
                except ValueError:
                    pass  # Handle non-integer input gracefully
            elif downButton.collidepoint(event.pos):
                try:
                    input_string = str(int(input_string) - 1)
                except ValueError:
                    pass  # Handle non-integer input gracefully

    # Update the display
    pygame.display.update()


def window3(screen):
    global input_string, you_win

    # Set posisi dan lebar masing-masing tower
    tower_positions = [(200, 250), (400, 250), (600, 250)]  # Menyimpan pasangan koordinat (x, y)
    tower_width = 10
    disk_height = 15  # Sesuaikan dengan nilai yang diinginkan

    # Mengubah isi dari towers agar koordinat x dimulai dari 185 dan berkurang 10 setiap disk berikutnya
    towers = [[[(195 - i * 10, 485 - (int(input_string) - i) * 15), i] for i in range(int(input_string), 0, -1)], [], []]

    dragging_disk = None
    is_dragging = False
    original_tower = None
    original_position = None
    while True:
        # Remove screen.fill(white) to avoid the error
        screen.fill(white)
        pygame.draw.rect(screen, black, (100, 500, 600, 10))

        # Draw towers
        for i, (pos_x, pos_y) in enumerate(tower_positions):
            pygame.draw.rect(screen, black, (pos_x - tower_width // 2, pos_y, tower_width, 250))

        if is_dragging:
            x, y = pygame.mouse.get_pos()
            disk_rect = pygame.Rect(x - dragging_disk[1] * 30, y - disk_height // 2, dragging_disk[1] * 30, disk_height)
            pygame.draw.rect(screen, sky_blue, disk_rect)
            pygame.draw.rect(screen, blue, disk_rect, 1)

        for i, (pos_x, pos_y) in enumerate(tower_positions):
            for disk in towers[i]:
                # Calculate the x-coordinate for the disk to be symmetrical around the tower
                disk_width = disk[1] * 20  # Assuming each disk's width is 20 times its number
                disk_x = pos_x - disk_width // 2  # Center the disk around the tower

                # Create and draw the disk rectangle
                disk_rect = pygame.Rect(disk_x, disk[0][1], disk_width, disk_height)
                pygame.draw.rect(screen, sky_blue, disk_rect)
                pygame.draw.rect(screen, blue, disk_rect, 1)

                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos

                # Check if the click is on the topmost disk of any tower
                for i, (pos_x, pos_y) in enumerate(tower_positions):
                    if towers[i]:
                        disk = towers[i][-1]
                        disk_rect = pygame.Rect(disk[0][0], disk[0][1], disk[1] * 20, disk_height)
                        if disk_rect.collidepoint(x, y):
                            dragging_disk = towers[i].pop()
                            is_dragging = True
                            original_tower = i
                            original_position = (dragging_disk[0][0], 485 - (int(input_string) - dragging_disk[1]) * 15)
                            break
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if is_dragging:
                    x, y = pygame.mouse.get_pos()
                    target_tower = next((i for i, (pos_x, pos_y) in enumerate(tower_positions) if pos_x - 100 <= x < pos_x + 100), None)


                    if target_tower is not None:
                        # Debug the position before moving
                        original_position = (dragging_disk[0][0], 485 - (int(input_string) - dragging_disk[1]) * 15)
                        print("Before Move - Disk:", dragging_disk[1], "Original Tower:", original_tower, "Position:", original_position)

                        # Check if the move is valid (disk is smaller than the top disk on the target tower)
                        if not towers[target_tower] or dragging_disk[1] < towers[target_tower][-1][1]:
                            # Modifikasi agar disk ditempatkan pada posisi y tertentu
                            new_disk_y = 485 - len(towers[target_tower]) * disk_height
                            new_disk = [(tower_positions[target_tower][0] + (tower_width - dragging_disk[1] * 30) // 2, new_disk_y), dragging_disk[1]]
                            towers[target_tower].append(new_disk)
                            print(f"Mouse Up - Moved to Tower {target_tower + 1} - Disk: {dragging_disk[1]} - Target Tower: {target_tower} - Position: {new_disk[0]}")

                            # Check for win condition
                            if len(towers[2]) == int(input_string) and all(len(tower) == 0 for i, tower in enumerate(towers) if i != 2):
                                you_win = True
                        else:
                            # Move is invalid, return the disk to the original tower
                            towers[original_tower].append(dragging_disk)
                            print(f"Invalid Move - Disk: {dragging_disk[1]} - Target Tower: {target_tower} - Disk too large")
                    else:
                        # If the target tower is None, place the disk at y=485
                        towers[original_tower].append(dragging_disk)
                        print("Mouse Up - Cancelled Move - Disk:", dragging_disk, "Original Tower:", original_tower, "Position:", original_position)
                    
                    dragging_disk = None
                    is_dragging = False
                    original_tower = None
                    # Check if the player wins after each move


        # Display "You Win" message if the player wins
        if you_win:
            # Draw a black background
            pygame.draw.rect(screen, black, (300, 115, 200, 65))
            # Display the "You Win!" text in white
            font = pygame.font.Font(None, 48)
            win_text = font.render("You Win!", True, (255, 255, 255))
            win_rect = win_text.get_rect(center=(800 // 2, 150))
            screen.blit(win_text, win_rect)

        # Display mouse coordinates
        mouse_x, mouse_y = pygame.mouse.get_pos()
        font = pygame.font.Font(None, 36)
        text = font.render(f"Mouse Coordinates: X = {mouse_x}, Y = {mouse_y}", True, black)
        screen.blit(text, (10, 10))

        pygame.display.update()

you_win = False

def window4(screen):
    global you_win, input_string

    white = (255, 255, 255)
    black = (0, 0, 0)
    sky_blue = (135, 206, 235)
    blue = (0, 0, 255)

    tower_positions = [(200, 250), (400, 250), (600, 250)]
    tower_width = 10
    disk_height = 15

    moves = []  # This will store the sequence of moves

    def move_disk(start, end):
        disk = towers[start].pop()
        towers[end].append(disk)
        check_win_condition()
    def solve_hanoi(n, start, end, temp):
        if n == 1:
            moves.append((start, end))
            return
        solve_hanoi(n-1, start, temp, end)
        moves.append((start, end))
        solve_hanoi(n-1, temp, end, start)


    def check_win_condition():
        global you_win
        if len(towers[2]) == int(input_string) and all(len(tower) == 0 for i, tower in enumerate(towers) if i != 2):
            you_win = True

    towers = [[i for i in range(int(input_string), 0, -1)], [], []]
    solve_hanoi(int(input_string), 0, 2, 1)

    clock = pygame.time.Clock()
    move_delay = 500  # Adjust the delay as needed
    last_move_time = pygame.time.get_ticks()

    move_index = 0  # Track the current move

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(white)
        pygame.draw.rect(screen, black, (100, 500, 600, 10))

        for pos_x, pos_y in tower_positions:
            pygame.draw.rect(screen, black, (pos_x - tower_width // 2, pos_y, tower_width, 250))

        for i, (pos_x, pos_y) in enumerate(tower_positions):
            for j, disk in enumerate(towers[i]):
                disk_width = disk * 20
                disk_x = pos_x - disk_width // 2
                disk_y = 485 - j * disk_height
                pygame.draw.rect(screen, sky_blue, (disk_x, disk_y, disk_width, disk_height))
                pygame.draw.rect(screen, blue, (disk_x, disk_y, disk_width, disk_height), 1)

        if not you_win and pygame.time.get_ticks() - last_move_time > move_delay and move_index < len(moves):
            start, end = moves[move_index]
            move_disk(start, end)  # This function should update the visual state of your towers
            move_index += 1
            last_move_time = pygame.time.get_ticks()

        if you_win:
            # Draw a black background
            pygame.draw.rect(screen, black, (300, 115, 200, 65))
            # Display the "You Win!" text in white
            font = pygame.font.Font(None, 48)
            win_text = font.render("You Win!", True, (255, 255, 255))
            win_rect = win_text.get_rect(center=(800 // 2, 150))
            screen.blit(win_text, win_rect)
        
        # Display mouse coordinates
        mouse_x, mouse_y = pygame.mouse.get_pos()
        font = pygame.font.Font(None, 36)
        text = font.render(f"Mouse Coordinates: X = {mouse_x}, Y = {mouse_y}", True, black)
        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(60)
