import pygame
import random

# تنظیمات اولیه
pygame.init()

# تنظیمات صفحه
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bioinformatics Puzzle')

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# اندازه‌های بلوک‌ها
block_width, block_height = 200, 50

# داده‌های پازل
categories = {
    "Prerequisites": [
        "Biology Fundamentals",
        "Programming Fundamentals",
        "Mathematics and Statistics",
        "Introduction to Bioinformatics",
        "Interdisciplinary Knowledge",
        "Project Management and Communication Skills",
        "Case Studies and Practical Applications",
        "Emerging Technologies",
        "Ethical and Societal Impact"
    ],
    "Main Sections": [
        "Omics Data Analysis and Interpretation",
        "Modeling and Simulation",
        "Integrated Platforms, Tools, and Technologies"
    ],
    "Specialized Topics": [
        "AI in Bioinformatics Data Analysis & Structural Biology",
        "Clinical Bioinformatics",
        "Agricultural Bioinformatics",
        "Environmental Bioinformatics",
        "Synthetic Biology",
        "Personalized Medicine",
        "Ethics in Bioinformatics",
        "Bioinformatics in Public Health"
    ],
    "Additional Resources": [
        "Online Courses and Certifications",
        "Books and Publications",
        "Conferences, Workshops, and Webinars",
        "Open-Source Projects and Repositories",
        "Scientific Journals and Papers",
        "Career Guidance and Job Opportunities",
        "Networking and Collaboration",
        "Regular Updates"
    ]
}

# مکان‌های بلوک‌ها
blocks = []
for category, items in categories.items():
    for i, item in enumerate(items):
        x = random.randint(0, screen_width - block_width)
        y = random.randint(0, screen_height - block_height)
        blocks.append({"category": category, "item": item, "rect": pygame.Rect(x, y, block_width, block_height)})

# حالت‌های بازی
dragging = False
selected_block = None

# حلقه بازی
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for block in blocks:
                if block["rect"].collidepoint(event.pos):
                    dragging = True
                    selected_block = block
                    offset_x = block["rect"].x - event.pos[0]
                    offset_y = block["rect"].y - event.pos[1]
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            selected_block = None
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                selected_block["rect"].x = event.pos[0] + offset_x
                selected_block["rect"].y = event.pos[1] + offset_y

    # رسم بلوک‌ها
    for block in blocks:
        pygame.draw.rect(screen, BLACK, block["rect"], 2)
        font = pygame.font.SysFont(None, 24)
        text = font.render(block["item"], True, BLACK)
        screen.blit(text, (block["rect"].x + 10, block["rect"].y + 10))

    pygame.display.flip()

pygame.quit()









import pygame
import random

# تنظیمات اولیه
pygame.init()

# تنظیمات صفحه
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bioinformatics Puzzle')

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# اندازه‌های بلوک‌ها
block_width, block_height = 200, 50

# داده‌های پازل
categories = {
    "Prerequisites": [
        "Biology Fundamentals",
        "Programming Fundamentals",
        "Mathematics and Statistics",
        "Introduction to Bioinformatics",
        "Interdisciplinary Knowledge",
        "Project Management and Communication Skills",
        "Case Studies and Practical Applications",
        "Emerging Technologies",
        "Ethical and Societal Impact"
    ],
    "Main Sections": [
        "Omics Data Analysis and Interpretation",
        "Modeling and Simulation",
        "Integrated Platforms, Tools, and Technologies"
    ],
    "Specialized Topics": [
        "AI in Bioinformatics Data Analysis & Structural Biology",
        "Clinical Bioinformatics",
        "Agricultural Bioinformatics",
        "Environmental Bioinformatics",
        "Synthetic Biology",
        "Personalized Medicine",
        "Ethics in Bioinformatics",
        "Bioinformatics in Public Health"
    ],
    "Additional Resources": [
        "Online Courses and Certifications",
        "Books and Publications",
        "Conferences, Workshops, and Webinars",
        "Open-Source Projects and Repositories",
        "Scientific Journals and Papers",
        "Career Guidance and Job Opportunities",
        "Networking and Collaboration",
        "Regular Updates"
    ]
}

# مکان‌های بلوک‌ها
blocks = []
for category, items in categories.items():
    for i, item in enumerate(items):
        x = random.randint(0, screen_width - block_width)
        y = random.randint(0, screen_height - block_height)
        blocks.append({"category": category, "item": item, "rect": pygame.Rect(x, y, block_width, block_height)})

# حالت‌های بازی
dragging = False
selected_block = None

# حلقه بازی
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for block in blocks:
                if block["rect"].collidepoint(event.pos):
                    dragging = True
                    selected_block = block
                    offset_x = block["rect"].x - event.pos[0]
                    offset_y = block["rect"].y - event.pos[1]
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            selected_block = None
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                selected_block["rect"].x = event.pos[0] + offset_x
                selected_block["rect"].y = event.pos[1] + offset_y

    # رسم بلوک‌ها
    for block in blocks:
        pygame.draw.rect(screen, BLACK, block["rect"], 2)
        font = pygame.font.SysFont(None, 24)
        text = font.render(block["item"], True, BLACK)
        screen.blit(text, (block["rect"].x + 10, block["rect"].y + 10))

    pygame.display.flip()

pygame.quit()




