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
    #Ark
    "Primordial": (150, 4500, level_data),
    "Abyssal": (123, 3383, enhance_level_data),
    "Infinity": (123, 3383, enhance_level_data),
    "Devious": (123, 3383, enhance_level_data),
    "Beast": (123, 3383, enhance_level_data),
    "Awakened": (83, 2252, mastery_level_data),
    "Grievous": (83, 2252, mastery_level_data),
    #Night Walker
    "Silence": (150, 4500, level_data),
    "Spear": (123, 3383, enhance_level_data),
    "GreaterD": (123, 3383, enhance_level_data),
    "Bite": (123, 3383, enhance_level_data),
    "Rapid": (123, 3383, enhance_level_data),
    "Quintuple": (83, 2252, mastery_level_data),
    "Ravenous": (83, 2252, mastery_level_data),
    #Bishop
    "HolyAdv": (150, 4500, level_data),
    "Bene": (123, 3383, enhance_level_data),
    "Angel": (123, 3383, enhance_level_data),
    "PeaceM": (123, 3383, enhance_level_data),
    "Divine": (123, 3383, enhance_level_data),
    "AngRay": (83, 2252, mastery_level_data),
    "BigBang": (83, 2252, mastery_level_data),
    #Night Lord
    "L&D": (150, 4500, level_data),
    "ThrowingS": (123, 3383, enhance_level_data),
    "Shurrikane": (123, 3383, enhance_level_data),
    "DLord": (123, 3383, enhance_level_data),
    "Blasting": (123, 3383, enhance_level_data),
    "QuadStar": (83, 2252, mastery_level_data),
    "Assassin": (83, 2252, mastery_level_data),
    #Adele
    "Maestro": (150, 4500, level_data),
    "Ruin": (123, 3383, enhance_level_data),
    "InfinityBlade": (123, 3383, enhance_level_data),
    "Legacy": (123, 3383, enhance_level_data),
    "Storm": (123, 3383, enhance_level_data),
    "Cleave": (83, 2252, mastery_level_data),
    "Hunting": (83, 2252, mastery_level_data),
    #Shadower
    "HalveCut": (150, 4500, level_data),
    "Assault": (123, 3383, enhance_level_data),
    "TrickBlade": (123, 3383, enhance_level_data),
    "SonicBlow": (123, 3383, enhance_level_data),
    "SlashShad": (123, 3383, enhance_level_data),
    "Assassinate": (83, 2252, mastery_level_data),
    "MesoExplo": (83, 2252, mastery_level_data),
    #Luminous
    "Harmonic": (150, 4500, level_data),
    "GateLight": (123, 3383, enhance_level_data),
    "Aether": (123, 3383, enhance_level_data),
    "Baptism": (123, 3383, enhance_level_data),
    "Liberation": (123, 3383, enhance_level_data),
    "Ender": (83, 2252, mastery_level_data),
    "Reflection": (83, 2252, mastery_level_data),
    #Fire/Poison
    "InfernalVen": (150, 4500, level_data),
    "DoT": (123, 3383, enhance_level_data),
    "PoisionNova": (123, 3383, enhance_level_data),
    "Elemental": (123, 3383, enhance_level_data),
    "PoisonChain": (123, 3383, enhance_level_data),
    "FlameSweep": (83, 2252, mastery_level_data),
    "FlameHaze": (83, 2252, mastery_level_data),
    #DawnWarrior
    "AstralBlitz": (150, 4500, level_data),
    "Cosmos": (123, 3383, enhance_level_data),
    "RiftDamnation": (123, 3383, enhance_level_data),
    "SoulEclipse": (123, 3383, enhance_level_data),
    "FlareSlash": (123, 3383, enhance_level_data),
    "Solar": (83, 2252, mastery_level_data),
    "CosmicShow": (83, 2252, mastery_level_data),
    #Path Finder
    "Forsaken": (150, 4500, level_data),
    "NovaBlast": (123, 3383, enhance_level_data),
    "Raven": (123, 3383, enhance_level_data),
    "Barrier": (123, 3383, enhance_level_data),
    "Relic": (123, 3383, enhance_level_data),
    "CardinalBur": (83, 2252, mastery_level_data),
    "BountifulDel": (83, 2252, mastery_level_data),

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