import pygame
import random
import time
pygame.init()

class DrawInfo:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [

        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, list):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(list)

    def set_list(self, list):
        self.list = list
        self.min_val = min(list)
        self.max_val = max(list)

        self.block_width = (self.width - self.SIDE_PAD) / len(list)
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2
        self.start_y = self.TOP_PAD // 2


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info):
    list = draw_info.list

    for i, val in enumerate(list):
        x = draw_info.start_x + i * draw_info.block_width
        height = (val - draw_info.min_val) * draw_info.block_height
        y = draw_info.height - height

        color = draw_info.GRADIENTS[i % 3]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, height))


def generate_starting_list(n, min_val, max_val):
    list = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        list.append(val)

    return list

def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    list = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInfo(800, 600, list)

    while run:
        clock.tick(180)

        draw(draw_info)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                list = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(list)
            if event.key == pygame.K_b:
                start_time = time.perf_counter()

                for i in range((len(list) - 1)):
                    for b in range(len(list) - 1 - i):
                        if list[b] > list[b + 1]:
                           list[b], list[b + 1] = list[b + 1], list[b]
                        draw(draw_info)
                        pygame.time.delay(10)
                end_time = time.perf_counter()
                elapsed_time = end_time - start_time
                print(f"Elapsed time: {elapsed_time:.2f} seconds" )


    pygame.quit()

if __name__ == '__main__':
    main()
