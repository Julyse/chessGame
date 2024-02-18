import pygame

from Case import Case
from Case import Player

# Initialize the grid
grid = [[Case(row, col) for col in range(8)] for row in range(8)]
player = Player("player1")
pygame.init()
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
running = True
MARGIN = 50
WHITE = (204, 204, 153)
BLACK = (101, 67, 33)
SQUARE_SIZE = 80
SCREEN_SIZE = (8 * SQUARE_SIZE + 2 * MARGIN, 8 * SQUARE_SIZE + 2 * MARGIN)

screen = pygame.display.set_mode((SCREEN_SIZE))
pygame.display.set_caption("Chess")
previous_square = None

piece_images = {
        "Rook_b": pygame.image.load('chesslogo/Rook_b.png'),
        "Knight_b": pygame.image.load('chesslogo/Knight_b.png'),
        "Bishop_b": pygame.image.load('chesslogo/Bishop_b.png'),
        "Queen_b": pygame.image.load('chesslogo/Queen_w.png'),
        "King_b": pygame.image.load('chesslogo/King_b.png'),
        "Pawn_b": pygame.image.load('chesslogo/Pawn_b.png'),
        "Rook_w": pygame.image.load('chesslogo/Rook_w.png'),
        "Knight_w": pygame.image.load('chesslogo/Knight_w.png'),
        "Bishop_w": pygame.image.load('chesslogo/Bishop_w.png'),
        "Queen_w": pygame.image.load('chesslogo/Queen_b.png'),
        "King_w": pygame.image.load('chesslogo/King_w.png'),
        "Pawn_w": pygame.image.load('chesslogo/Pawn_w.png')
}

def initial_piece(grid):
    grid[0][0].piece = "Rook_b"
    grid[1][0].piece = "Knight_b"
    grid[2][0].piece = "Bishop_b"
    grid[3][0].piece = "Queen_b"
    grid[4][0].piece = "King_b"
    grid[5][0].piece = "Bishop_b"
    grid[6][0].piece = "Knight_b"
    grid[7][0].piece = "Rook_b"
    for i in range(8):
        grid[i][1].piece = "Pawn_b"
        grid[i][6].piece = "Pawn_w"
    grid[0][7].piece = "Rook_w"
    grid[1][7].piece = "Knight_w"
    grid[2][7].piece = "Bishop_w"
    grid[3][7].piece = "Queen_w"
    grid[4][7].piece = "King_w"
    grid[5][7].piece = "Bishop_w"
    grid[6][7].piece = "Knight_w"
    grid[7][7].piece = "Rook_w"


initial_piece(grid)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = (mouse_x - MARGIN) // SQUARE_SIZE
            col = (mouse_y - MARGIN) // SQUARE_SIZE
            if 0 <= row < 8 and 0 <= col < 8:  # Check if the click was inside the board
                if previous_square is not None:
                    grid[previous_square[0]][previous_square[1]].selected = False
                previous_square = (row, col)
                grid[row][col].selected = True

        screen.fill("white")

        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = WHITE
                else:
                    color = BLACK
                # Draw the squares on the board
                pygame.draw.rect(screen, color,
                                 pygame.Rect(MARGIN + row * SQUARE_SIZE, MARGIN + col * SQUARE_SIZE, SQUARE_SIZE,
                                             SQUARE_SIZE))
                piece = grid[row][col].piece
                if piece != "None":
                    screen.blit(piece_images[piece],
                                (MARGIN + row * SQUARE_SIZE + SQUARE_SIZE // 2 - piece_images[piece].get_width() // 2,
                                 MARGIN + col * SQUARE_SIZE + SQUARE_SIZE // 2 - piece_images[piece].get_height() // 2))
                if grid[row][col].selected :
                    if grid[row][col].piece != "None":
                        pygame.draw.rect(screen, (255, 0, 0),
                                         pygame.Rect(MARGIN + row * SQUARE_SIZE, MARGIN + col * SQUARE_SIZE,
                                                     SQUARE_SIZE,
                                                     SQUARE_SIZE), 3)
                    else:
                        pygame.draw.rect(screen, (255, 255, 255),
                                         pygame.Rect(MARGIN + row * SQUARE_SIZE, MARGIN + col * SQUARE_SIZE,
                                                     SQUARE_SIZE,
                                                     SQUARE_SIZE), 3)
                if col == 0:
                    text = font.render(chr(row + 65), True, (0, 0, 0))
                    screen.blit(text, (MARGIN + row * SQUARE_SIZE + 35, MARGIN - 25))
                if row == 0:
                    text = font.render(str(8 - col), True, (0, 0, 0))
                    screen.blit(text, (MARGIN - 35, MARGIN + col * SQUARE_SIZE + 25))
        pygame.display.flip()

    clock.tick(30)

pygame.quit()



