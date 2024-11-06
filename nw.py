level_data = {
    1: (5, 100), 2: (1, 30),
    3: (1, 35), 4: (1, 40),
    5: (2, 45), 6: (2, 50),
    7: (2, 55), 8: (3, 60),
    9: (3, 65), 10: (10, 200),
    11: (3, 80), 12: (3, 90),
    13: (4, 100), 14: (4, 110),
    15: (4, 120), 16: (4, 130),
    17: (4, 140), 18: (4, 150),
    19: (5, 160), 20: (15, 350),
    21: (5, 170), 22: (5, 180),
    23: (5, 190), 24: (5, 200),
    25: (5, 210), 26: (6, 220),
    27: (6, 230), 28: (6, 240),
    29: (7, 250), 30: (20, 500),
}
enhance_level_data = {
    1: (4, 75),2: (1, 23), 
    3: (1, 27),
    4: (1, 30), 5: (2, 34),
    6: (2, 38), 7: (2, 42),
    8: (3, 45), 9: (3, 49),
    10: (8, 150), 11: (3, 60),
    12: (3, 68), 13: (3, 75),
    14: (3, 83), 15: (3, 90),
    16: (3, 98), 17: (3, 105),
    18: (3, 113), 19: (4, 120),
    20: (12, 263), 21: (4, 128),
    22: (4, 135), 23: (4, 143),
    24: (4, 150), 25: (4, 158),
    26: (5, 165), 27: (5, 173),
    28: (5, 180), 29: (6, 188),
    30: (15, 375)
}
mastery_level_data = {
    1: (3, 50), 2: (1, 15),
    3: (1, 18), 4: (1, 20),
    5: (1, 23), 6: (1, 25),
    7: (1, 28), 8: (2, 30),
    9: (2, 33), 10: (5, 100),
    11: (2, 40), 12: (2, 45),
    13: (2, 50), 14: (2, 55),
    15: (2, 60), 16: (2, 65),
    17: (2, 70), 18: (2, 75),
    19: (3, 80), 20: (8, 175),
    21: (3, 85), 22: (3, 90),
    23: (3, 95), 24: (3, 100),
    25: (3, 105), 26: (3, 110),
    27: (3, 115), 28: (3, 120),
    29: (4, 125), 30: (10, 250),
}

categories = {
    "Silence": (150, 4500, level_data),
    "Spear": (123, 3383, enhance_level_data),
    "GreaterD": (123, 3383, enhance_level_data),
    "Bite": (123, 3383, enhance_level_data),
    "Rapid": (123, 3383, enhance_level_data),
    "Quintuple": (83, 2252, mastery_level_data),
    "Ravenous": (83, 2252, mastery_level_data),
}

async def calculate_progress(category_name, max_level):
    # Get category-specific data
    total_sol, total_frag, level_data = categories[category_name]
    current_sol = 0
    current_frag = 0

    for level in range(1, max_level + 1):
        if level in level_data:
            sol, frag = level_data[level]
            current_sol += sol
            current_frag += frag

    percentage = (current_frag / total_frag) * 100
    response = (
        f"> **Total Sol Collected:** `{current_sol}/{total_sol}`\n"
        f"> **Total Fragments Collected:** `{current_frag}/{total_frag}`\n"
        f"> **Progression:** `{percentage:.2f}%`\n"
        f"━━━━━━━━━━━━━━━━\n"
    )
    return response, current_frag