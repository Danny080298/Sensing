import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("The bot is now ready to use!")
    print("----------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Ready to use")
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

# Define the command
# @client.command()
async def origin(max_level: int):
    total_sol = 150
    total_frag = 4500
    current_sol = 0
    current_frag = 0

    for level in range(1, max_level + 1):
        if level in level_data:
            sol, frag = level_data[level]
            current_sol += sol
            current_frag += frag


    percentage = (current_frag / total_frag) * 100

    progress_bar_length = 7  # Number of segments in the progress bar
    filled_segments = int(percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Create the response with the progress bar
    response = (
        f"> **Total Sol Collected:** `{current_sol}/{total_sol}`\n"
        f"> **Total Fragments Collected:** `{current_frag}/{total_frag}`\n"
        f"> **Progression:** `{percentage:.2f}%` {progress_bar}\n"
    )
    return response, current_frag


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

# Define the command
# @client.command()
async def enhance1(max_level: int):
    total_sol = 123
    total_frag = 3383
    current_sol = 0
    current_frag = 0

    for level in range(1, max_level + 1):
        if level in enhance_level_data:
            sol, frag = enhance_level_data[level]
            current_sol += sol
            current_frag += frag


    percentage = (current_frag / total_frag) * 100

    progress_bar_length = 7  # Number of segments in the progress bar
    filled_segments = int(percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Create the response with the progress bar
    response = (
        f"> **Total Sol Collected:** `{current_sol}/{total_sol}`\n"
        f"> **Total Fragments Collected:** `{current_frag}/{total_frag}`\n"
        f"> **Progression:** `{percentage:.2f}%` {progress_bar}\n"
    )
    return response, current_frag


# @client.command()
async def enhance2(max_level: int):
    total_sol = 123
    total_frag = 3383
    current_sol = 0
    current_frag = 0

    for level in range(1, max_level + 1):
        if level in enhance_level_data:
            sol, frag = enhance_level_data[level]
            current_sol += sol
            current_frag += frag

    percentage = (current_frag / total_frag) * 100

    progress_bar_length = 7  # Number of segments in the progress bar
    filled_segments = int(percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Create the response with the progress bar
    response = (
        f"> **Total Sol Collected:** `{current_sol}/{total_sol}`\n"
        f"> **Total Fragments Collected:** `{current_frag}/{total_frag}`\n"
        f"> **Progression:** `{percentage:.2f}%` {progress_bar}\n"
    )
    return response, current_frag
# @client.command()
async def enhance3(max_level: int):
    total_sol = 123
    total_frag = 3383
    current_sol = 0
    current_frag = 0

    for level in range(1, max_level + 1):
        if level in enhance_level_data:
            sol, frag = enhance_level_data[level]
            current_sol += sol
            current_frag += frag

    
    percentage = (current_frag / total_frag) * 100

    progress_bar_length = 7  # Number of segments in the progress bar
    filled_segments = int(percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Create the response with the progress bar
    response = (
        f"> **Total Sol Collected:** `{current_sol}/{total_sol}`\n"
        f"> **Total Fragments Collected:** `{current_frag}/{total_frag}`\n"
        f"> **Progression:** `{percentage:.2f}%` {progress_bar}\n"
    )
    return response, current_frag


# @client.command()
async def enhance4(max_level: int):
    total_sol = 123
    total_frag = 3383
    current_sol = 0
    current_frag = 0

    for level in range(1, max_level + 1):
        if level in enhance_level_data:
            sol, frag = enhance_level_data[level]
            current_sol += sol
            current_frag += frag

    percentage = (current_frag / total_frag) * 100

    progress_bar_length = 7  # Number of segments in the progress bar
    filled_segments = int(percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Create the response with the progress bar
    response = (
        f"> **Total Sol Collected:** `{current_sol}/{total_sol}`\n"
        f"> **Total Fragments Collected:** `{current_frag}/{total_frag}`\n"
        f"> **Progression:** `{percentage:.2f}%` {progress_bar}\n"
    )
    return response, current_frag



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

# Define the command
# @client.command()
async def mastery1(max_level: int):
    total_sol = 83
    total_frag = 2252
    current_sol = 0
    current_frag = 0

    # Calculate cumulative Sol and Fragments for all levels from 1 to max_level
    for level in range(1, max_level + 1):
        if level in mastery_level_data:
            sol, frag = mastery_level_data[level]
            current_sol += sol
            current_frag += frag

    percentage = (current_frag / total_frag) * 100

    progress_bar_length = 7  # Number of segments in the progress bar
    filled_segments = int(percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Create the response with the progress bar
    response = (
        f"> **Total Sol Collected:** `{current_sol}/{total_sol}`\n"
        f"> **Total Fragments Collected:** `{current_frag}/{total_frag}`\n"
        f"> **Progression:** `{percentage:.2f}%` {progress_bar}\n"
    )
    return response, current_frag


# @client.command()
async def mastery2(max_level: int):
    total_sol = 83
    total_frag = 2252
    current_sol = 0
    current_frag = 0

    # Calculate cumulative Sol and Fragments for all levels from 1 to max_level
    for level in range(1, max_level + 1):
        if level in mastery_level_data:
            sol, frag = mastery_level_data[level]
            current_sol += sol
            current_frag += frag

    # Calculate the percentage of progression
    percentage = (current_frag / total_frag) * 100

    # Create the progress bar
    progress_bar_length = 7  # Number of segments in the progress bar
    filled_segments = int(percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Create the response with the progress bar
    response = (
        f"> **Total Sol Collected:** `{current_sol}/{total_sol}`\n"
        f"> **Total Fragments Collected:** `{current_frag}/{total_frag}`\n"
        f"> **Progression:** `{percentage:.2f}%` {progress_bar}\n"
    )
    return response, current_frag


@client.command()
async def sen_coi(ctx, *args):
    # Parse arguments into a dictionary
    args_dict = {}
    for i in range(0, len(args), 2):
        category = args[i]
        level = int(args[i+1])
        args_dict[category] = level

    # Collect results for each category
    total_fragments = 0
    max_frag = 22536
    embed = discord.Embed(
        title="📊 Sen coi Progress Summary",
        description="Detailed Progress across all Categories",
        color=discord.Color.blue()
    )

    # Function calls for each category with data accumulation
    if 'origin' in args_dict:
        response, frag = await origin(args_dict['origin'])
        total_fragments += frag
        embed.add_field(name="🧭 Origin Progress", value=response, inline=False)

    if 'enhance1' in args_dict:
        response, frag = await enhance1(args_dict['enhance1'])
        total_fragments += frag
        embed.add_field(name="🔧 Enhance 1 Progress", value=response, inline=True)

    if 'enhance2' in args_dict:
        response, frag = await enhance2(args_dict['enhance2'])
        total_fragments += frag
        embed.add_field(name="🔧 Enhance 2 Progress", value=response, inline=True)

    if 'enhance3' in args_dict:
        response, frag = await enhance3(args_dict['enhance3'])
        total_fragments += frag
        embed.add_field(name="🔧 Enhance 3 Progress", value=response, inline=True)

    if 'enhance4' in args_dict:
        response, frag = await enhance4(args_dict['enhance4'])
        total_fragments += frag
        embed.add_field(name="🔧 Enhance 4 Progress", value=response, inline=True)

    if 'mastery1' in args_dict:
        response, frag = await mastery1(args_dict['mastery1'])
        total_fragments += frag
        embed.add_field(name="🎓 Mastery 1 Progress", value=response, inline=True)

    if 'mastery2' in args_dict:
        response, frag = await mastery2(args_dict['mastery2'])
        total_fragments += frag
        embed.add_field(name="🎓 Mastery 2 Progress", value=response, inline=True)

    # Calculate remaining fragments and progression percentage
    remaining_fragments = max_frag - total_fragments
    progression_percentage = (total_fragments / max_frag) * 100

    # Create the progress bar
    progress_bar_length = 7  # Number of segments in the progress bar
    filled_segments = int(progression_percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Add summary fields for total fragments and progression
    embed.add_field(name="Total Fragments Collected", value=f"`{total_fragments}/{max_frag}`", inline=True)
    embed.add_field(name="Fragments Needed to Complete", value=f"`{remaining_fragments}`", inline=True)
    embed.add_field(name="Overall Progression", value=f"`{progression_percentage:.2f}%` {progress_bar}", inline=False)

    # Set footer for context (optional)
    embed.set_footer(text="Progress data updated just now")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)

def get_random_number():
    return random.randint(1, 40)
@client.command()
async def sen_boi(ctx):
    number = get_random_number()
    await ctx.send(f"🎲 Sen bói Channel **{number}**")

@client.command()
async def sen_help(ctx):
    # Create an embed for the help message
    embed = discord.Embed(
        title="Help - List of Commands",
        description="Here are the commands you can use with this bot:",
        color=discord.Color.green()
    )

    embed.add_field(name="!sen_boi", value="🎲 Sen bói Channel ", inline=False)
    embed.add_field(name="!sen_coi origin 1 enhance1 1 enhance2 1 enhance3 1 enhance4 1 mastery1 1 mastery2 1", value="Bấm theo cái sen làm mẫu đẻ hiển thị cái bản nha ", inline=False)

    await ctx.send(embed=embed)
client.run(TOKEN)