import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random
from ark import calculate_progress 

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("The bot is now ready to use!")
    print("----------------------------")

class HelpDropdown(discord.ui.Select):
    def __init__(self):
        # Define options for each command
        options = [
            discord.SelectOption(label="!sen_boi", description="Sen bói Channel"),
            discord.SelectOption(label="Adele", description="!sen_adele"),
            discord.SelectOption(label="Ark", description="!sen_ark"),
            discord.SelectOption(label="Bishop", description="!sen_bs"),
            discord.SelectOption(label="Dawn Warrior", description="!sen_dw"),
            discord.SelectOption(label="Fire Poison", description="!sen_fp"),
            discord.SelectOption(label="Luminous", description="!sen_lumi"),
            discord.SelectOption(label="Night Lord", description="!sen_nl"),
            discord.SelectOption(label="Night Walker", description="!sen_nw"),
            discord.SelectOption(label="Path Finder", description="!sen_pf"),
            discord.SelectOption(label="Shadower", description="!sen_shadower"),

]
        
        
        super().__init__(placeholder="Select a Job command to view details...", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # Respond with details about the selected command
        if self.values[0] == "!sen_boi":
            description = "🎲 **Sen bói Channel**: Use this command to get a random Sen bói response."
        elif self.values[0] == "Ark":
            description = "💡 **!sen_ark Primordial 1 Abyssal 1 Infinity 1 Devious 1 Beast 1 Awakened 1 Grievous 1**\nExample command for Ark."
        elif self.values[0] == "Night Walker":
            description = "💡 **!sen_nw Silence 1 Spear 1 GreaterD 1 Bite 1 Rapid 1 Quintuple 1 Ravenous 1**\nExample command for Night Walker."
        elif self.values[0] == "Bishop":
            description = "💡 **!sen_bs HolyAdv 1 Bene 1 Angel 1 PeaceM 1 Divine 1 AngRay 1 BigBang 1**\nExample command for Bishop."
        elif self.values[0] == "Night Lord":
            description = "💡 **!sen_nl L&D 1 ThrowingS 1 Shurrikane 1 DLord 1 Blasting 1 QuadStar 1 Assassin 1**\nExample command for Night Lord."
        elif self.values[0] == "Adele":
            description = "💡 **!sen_adele Maestro 1 Ruin 1 InfinityBlade 1 Legacy 1 Storm 1 Cleave 1 Hunting 1**\nExample command for Adele."
        elif self.values[0] == "Shadower":
            description = "💡 **!sen_shadower HalveCut 1 Assault 1 TrickBlade 1 SonicBlow 1 SlashShad 1 Assassinate 1 MesoExplo 1**\nExample command for Shadower."
        elif self.values[0] == "Luminous":
            description = "💡 **!sen_lumi Harmonic 1 GateLight 1 Aether 1 Baptism 1 Liberation 1 Ender 1 Reflection 1**\nExample command for Luminous."
        elif self.values[0] == "Fire Poison":
            description = "💡 **!sen_fp InfernalVen 1 DoT 1 PoisionNova 1 Elemental 1 PoisonChain 1 FlameSweep 1 FlameHaze 1**\nExample command for Fire Poison."
        elif self.values[0] == "Dawn Warrior":
            description = "💡 **!sen_dw AstralBlitz 1 Cosmos 1 RiftDamnation 1 SoulEclipse 1 FlareSlash 1 Solar 1 CosmicShow 1**\nExample command for Dawn Warrior."
        elif self.values[0] == "Path Finder":
            description = "💡 **!sen_pf Forsaken 1 NovaBlast 1 Raven 1 Barrier 1 Relic 1 CardinalBur 1 BountifulDel 1**\nExample command for Path Finder "
        # elif self.values[0] == "":
        #     description = "💡 ****\nExample command for."

            
        # Send an ephemeral message with command details
        await interaction.response.send_message(description, ephemeral=True)

class HelpDropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(HelpDropdown())

@client.command()
async def hello(ctx):
    await ctx.send("Ready to use")

def get_random_number():
    return random.randint(1, 40)
@client.command()
async def sen_boi(ctx):
    number = get_random_number()
    await ctx.send(f"🎲 Sen bói Channel **{number}**")

@client.command()
async def sen_help(ctx):
    # Create an embed for the help command
    embed = discord.Embed(
        title="Help - List Job of Commands",
        description="Select a Job",
        color=discord.Color.green()
    )

    # Send the embed with the drop-down view
    await ctx.send(embed=embed, view=HelpDropdownView())

@client.command()
async def sen_ark(ctx, *args):
    # Parse arguments into a dictionary
    args_dict = {}
    for i in range(0, len(args), 2):
        category = args[i]
        level = int(args[i + 1])
        args_dict[category] = level

    # Create the embed for the summary
    embed = discord.Embed(
        title="📊 Sen Coi Progress Summary",
        description="Detailed Progress across all Categories",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1154955903196463154/1303476731885260830/Screenshot_2024-11-05_at_15.49.46.png?ex=672be4ce&is=672a934e&hm=d058f46e3549b1c9865232922f1840c4363ad67ef11952edf5fb07bc968eba5c&")

    # Initialize variables to collect data
    results = []
    total_fragments = 0
    max_frag = 22536  # Example max fragments value

    # Add fields to embed for each category's progress
    for category, max_level in args_dict.items():
        response, frag = await calculate_progress(category, max_level)
        total_fragments += frag
        # Add each category's progress to the embed
        embed.add_field(name=f"{category} Progress", value=response, inline=True)

    # Calculate remaining fragments and progression percentage
    remaining_fragments = max_frag - total_fragments
    progression_percentage = (total_fragments / max_frag) * 100

    # Create a visual progress bar
    progress_bar_length = 10  # Number of segments in the progress bar
    filled_segments = int(progression_percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Add summary fields for total fragments and progression
    embed.add_field(name="Total Fragments Collected", value=f"`{total_fragments}/{max_frag}`", inline=False)
    embed.add_field(name="Fragments Needed to Complete", value=f"`{remaining_fragments}`", inline=False)
    embed.add_field(name="Overall Progression", value=f"`{progression_percentage:.2f}%` {progress_bar}", inline=False)

    # Set a footer for context (optional)
    embed.set_footer(text="Progress data updated just now")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)

@client.command()
async def sen_nw(ctx, *args):
    # Parse arguments into a dictionary
    args_dict = {}
    for i in range(0, len(args), 2):
        category = args[i]
        level = int(args[i + 1])
        args_dict[category] = level

    # Create the embed for the summary
    embed = discord.Embed(
        title="📊 Sen Coi Progress Summary",
        description="Detailed Progress across all Categories",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1154955903196463154/1303489878532558989/Screenshot_2024-11-05_at_16.43.00.png?ex=672bf10c&is=672a9f8c&hm=4e8e54d8df2c6e65a07c720eef7c0a833a31095669ec4e6cf108fe3ac7d9e9fb&")
    # embed.set_thumbnail(url="")
    # Initialize variables to collect data
    results = []
    total_fragments = 0
    max_frag = 22536  # Example max fragments value

    # Add fields to embed for each category's progress
    for category, max_level in args_dict.items():
        response, frag = await calculate_progress(category, max_level)
        total_fragments += frag
        # Add each category's progress to the embed
        embed.add_field(name=f"{category} Progress", value=response, inline=True)

    # Calculate remaining fragments and progression percentage
    remaining_fragments = max_frag - total_fragments
    progression_percentage = (total_fragments / max_frag) * 100

    # Create a visual progress bar
    progress_bar_length = 10  # Number of segments in the progress bar
    filled_segments = int(progression_percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Add summary fields for total fragments and progression
    embed.add_field(name="Total Fragments Collected", value=f"`{total_fragments}/{max_frag}`", inline=False)
    embed.add_field(name="Fragments Needed to Complete", value=f"`{remaining_fragments}`", inline=False)
    embed.add_field(name="Overall Progression", value=f"`{progression_percentage:.2f}%` {progress_bar}", inline=False)

    # Set a footer for context (optional)
    embed.set_footer(text="Progress data updated just now")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)

@client.command()
async def sen_bs(ctx, *args):
    # Parse arguments into a dictionary
    args_dict = {}
    for i in range(0, len(args), 2):
        category = args[i]
        level = int(args[i + 1])
        args_dict[category] = level

    # Create the embed for the summary
    embed = discord.Embed(
        title="📊 Sen Coi Progress Summary",
        description="Detailed Progress across all Categories",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1154955903196463154/1303503422791745587/Screenshot_2024-11-05_at_17.37.07.png?ex=672bfda9&is=672aac29&hm=d209ea78e536b991bec72ad14446ed19f00f208ee774dde002469820e9ba0199&")
    # Initialize variables to collect data
    results = []
    total_fragments = 0
    max_frag = 22536  # Example max fragments value

    # Add fields to embed for each category's progress
    for category, max_level in args_dict.items():
        response, frag = await calculate_progress(category, max_level)
        total_fragments += frag
        # Add each category's progress to the embed
        embed.add_field(name=f"{category} Progress", value=response, inline=True)

    # Calculate remaining fragments and progression percentage
    remaining_fragments = max_frag - total_fragments
    progression_percentage = (total_fragments / max_frag) * 100

    # Create a visual progress bar
    progress_bar_length = 10  # Number of segments in the progress bar
    filled_segments = int(progression_percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Add summary fields for total fragments and progression
    embed.add_field(name="Total Fragments Collected", value=f"`{total_fragments}/{max_frag}`", inline=False)
    embed.add_field(name="Fragments Needed to Complete", value=f"`{remaining_fragments}`", inline=False)
    embed.add_field(name="Overall Progression", value=f"`{progression_percentage:.2f}%` {progress_bar}", inline=False)

    # Set a footer for context (optional)
    embed.set_footer(text="Progress data updated just now")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)

@client.command()
async def sen_nl(ctx, *args):
    # Parse arguments into a dictionary
    args_dict = {}
    for i in range(0, len(args), 2):
        category = args[i]
        level = int(args[i + 1])
        args_dict[category] = level

    # Create the embed for the summary
    embed = discord.Embed(
        title="📊 Sen Coi Progress Summary",
        description="Detailed Progress across all Categories",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1154955903196463154/1303515470003048488/Screenshot_2024-11-05_at_18.24.45.png?ex=672c08e2&is=672ab762&hm=d8a302f61ac542961dfa2c2d27943566be8b2cadf239259eec3491a3aa8ba26d&")
    # embed.set_thumbnail(url="")
    # Initialize variables to collect data
    results = []
    total_fragments = 0
    max_frag = 22536  # Example max fragments value

    # Add fields to embed for each category's progress
    for category, max_level in args_dict.items():
        response, frag = await calculate_progress(category, max_level)
        total_fragments += frag
        # Add each category's progress to the embed
        embed.add_field(name=f"{category} Progress", value=response, inline=True)

    # Calculate remaining fragments and progression percentage
    remaining_fragments = max_frag - total_fragments
    progression_percentage = (total_fragments / max_frag) * 100

    # Create a visual progress bar
    progress_bar_length = 10  # Number of segments in the progress bar
    filled_segments = int(progression_percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Add summary fields for total fragments and progression
    embed.add_field(name="Total Fragments Collected", value=f"`{total_fragments}/{max_frag}`", inline=False)
    embed.add_field(name="Fragments Needed to Complete", value=f"`{remaining_fragments}`", inline=False)
    embed.add_field(name="Overall Progression", value=f"`{progression_percentage:.2f}%` {progress_bar}", inline=False)

    # Set a footer for context (optional)
    embed.set_footer(text="Progress data updated just now")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)

@client.command()
async def sen_adele(ctx, *args):
    # Parse arguments into a dictionary
    args_dict = {}
    for i in range(0, len(args), 2):
        category = args[i]
        level = int(args[i + 1])
        args_dict[category] = level

    # Create the embed for the summary
    embed = discord.Embed(
        title="📊 Sen Coi Progress Summary",
        description="Detailed Progress across all Categories",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1154955903196463154/1303532309479297054/Screenshot_2024-11-05_at_19.31.53.png?ex=672c1891&is=672ac711&hm=62712613ffa1b241e39a5775f3b8e8bf69e3b5e20aef33a2af73a70430be8bb7&")
    # embed.set_thumbnail(url="")
    # Initialize variables to collect data
    results = []
    total_fragments = 0
    max_frag = 22536  # Example max fragments value

    # Add fields to embed for each category's progress
    for category, max_level in args_dict.items():
        response, frag = await calculate_progress(category, max_level)
        total_fragments += frag
        # Add each category's progress to the embed
        embed.add_field(name=f"{category} Progress", value=response, inline=True)

    # Calculate remaining fragments and progression percentage
    remaining_fragments = max_frag - total_fragments
    progression_percentage = (total_fragments / max_frag) * 100

    # Create a visual progress bar
    progress_bar_length = 10  # Number of segments in the progress bar
    filled_segments = int(progression_percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Add summary fields for total fragments and progression
    embed.add_field(name="Total Fragments Collected", value=f"`{total_fragments}/{max_frag}`", inline=False)
    embed.add_field(name="Fragments Needed to Complete", value=f"`{remaining_fragments}`", inline=False)
    embed.add_field(name="Overall Progression", value=f"`{progression_percentage:.2f}%` {progress_bar}", inline=False)

    # Set a footer for context (optional)
    embed.set_footer(text="Progress data updated just now")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)

@client.command()
async def sen_shadower(ctx, *args):
    # Parse arguments into a dictionary
    args_dict = {}
    for i in range(0, len(args), 2):
        category = args[i]
        level = int(args[i + 1])
        args_dict[category] = level

    # Create the embed for the summary
    embed = discord.Embed(
        title="📊 Sen Coi Progress Summary",
        description="Detailed Progress across all Categories",
        color=discord.Color.blue()
    )
    # embed.set_thumbnail(url="")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1154955903196463154/1303751340257705985/Screenshot_2024-11-06_at_10.02.06.png?ex=672ce48e&is=672b930e&hm=e22e6acff2d38a1edfb1213b57a215c2495ab366a1963090d81c1c14609d0130&")
    # Initialize variables to collect data
    results = []
    total_fragments = 0
    max_frag = 22536  # Example max fragments value

    # Add fields to embed for each category's progress
    for category, max_level in args_dict.items():
        response, frag = await calculate_progress(category, max_level)
        total_fragments += frag
        # Add each category's progress to the embed
        embed.add_field(name=f"{category} Progress", value=response, inline=True)

    # Calculate remaining fragments and progression percentage
    remaining_fragments = max_frag - total_fragments
    progression_percentage = (total_fragments / max_frag) * 100

    # Create a visual progress bar
    progress_bar_length = 10  # Number of segments in the progress bar
    filled_segments = int(progression_percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Add summary fields for total fragments and progression
    embed.add_field(name="Total Fragments Collected", value=f"`{total_fragments}/{max_frag}`", inline=False)
    embed.add_field(name="Fragments Needed to Complete", value=f"`{remaining_fragments}`", inline=False)
    embed.add_field(name="Overall Progression", value=f"`{progression_percentage:.2f}%` {progress_bar}", inline=False)

    # Set a footer for context (optional)
    embed.set_footer(text="Progress data updated just now")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)


@client.command()
async def sen_lumi(ctx, *args):
    # Parse arguments into a dictionary
    args_dict = {}
    for i in range(0, len(args), 2):
        category = args[i]
        level = int(args[i + 1])
        args_dict[category] = level

    # Create the embed for the summary
    embed = discord.Embed(
        title="📊 Sen Coi Progress Summary",
        description="Detailed Progress across all Categories",
        color=discord.Color.blue()
    )
    # embed.set_thumbnail(url="")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1154955903196463154/1303753107410255915/Screenshot_2024-11-06_at_10.09.17.png?ex=672ce633&is=672b94b3&hm=c98b10d446e01ad5f204acd2a275c108f25e2908c5bab5024ee932c3a148007e&")
    # Initialize variables to collect data
    results = []
    total_fragments = 0
    max_frag = 22536  # Example max fragments value

    # Add fields to embed for each category's progress
    for category, max_level in args_dict.items():
        response, frag = await calculate_progress(category, max_level)
        total_fragments += frag
        # Add each category's progress to the embed
        embed.add_field(name=f"{category} Progress", value=response, inline=True)

    # Calculate remaining fragments and progression percentage
    remaining_fragments = max_frag - total_fragments
    progression_percentage = (total_fragments / max_frag) * 100

    # Create a visual progress bar
    progress_bar_length = 10  # Number of segments in the progress bar
    filled_segments = int(progression_percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Add summary fields for total fragments and progression
    embed.add_field(name="Total Fragments Collected", value=f"`{total_fragments}/{max_frag}`", inline=False)
    embed.add_field(name="Fragments Needed to Complete", value=f"`{remaining_fragments}`", inline=False)
    embed.add_field(name="Overall Progression", value=f"`{progression_percentage:.2f}%` {progress_bar}", inline=False)

    # Set a footer for context (optional)
    embed.set_footer(text="Progress data updated just now")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)

@client.command()
async def sen_fp(ctx, *args):
    # Parse arguments into a dictionary
    args_dict = {}
    for i in range(0, len(args), 2):
        category = args[i]
        level = int(args[i + 1])
        args_dict[category] = level

    # Create the embed for the summary
    embed = discord.Embed(
        title="📊 Sen Coi Progress Summary",
        description="Detailed Progress across all Categories",
        color=discord.Color.blue()
    )
    # embed.set_thumbnail(url="")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1154955903196463154/1303755270455037952/Screenshot_2024-11-06_at_10.17.54.png?ex=672ce837&is=672b96b7&hm=522a6782b08dc0f3ec50b6a9ab5b80b0fa483da09681ded07ee12794f9251d58&")
    # Initialize variables to collect data
    results = []
    total_fragments = 0
    max_frag = 22536  # Example max fragments value

    # Add fields to embed for each category's progress
    for category, max_level in args_dict.items():
        response, frag = await calculate_progress(category, max_level)
        total_fragments += frag
        # Add each category's progress to the embed
        embed.add_field(name=f"{category} Progress", value=response, inline=True)

    # Calculate remaining fragments and progression percentage
    remaining_fragments = max_frag - total_fragments
    progression_percentage = (total_fragments / max_frag) * 100

    # Create a visual progress bar
    progress_bar_length = 10  # Number of segments in the progress bar
    filled_segments = int(progression_percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Add summary fields for total fragments and progression
    embed.add_field(name="Total Fragments Collected", value=f"`{total_fragments}/{max_frag}`", inline=False)
    embed.add_field(name="Fragments Needed to Complete", value=f"`{remaining_fragments}`", inline=False)
    embed.add_field(name="Overall Progression", value=f"`{progression_percentage:.2f}%` {progress_bar}", inline=False)

    # Set a footer for context (optional)
    embed.set_footer(text="Progress data updated just now")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)

@client.command()
async def sen_dw(ctx, *args):
    # Parse arguments into a dictionary
    args_dict = {}
    for i in range(0, len(args), 2):
        category = args[i]
        level = int(args[i + 1])
        args_dict[category] = level

    # Create the embed for the summary
    embed = discord.Embed(
        title="📊 Sen Coi Progress Summary",
        description="Detailed Progress across all Categories",
        color=discord.Color.blue()
    )
    # embed.set_thumbnail(url="")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1154955903196463154/1303757592341905488/Screenshot_2024-11-06_at_10.27.08.png?ex=672cea60&is=672b98e0&hm=0717a5515f7c97bdcfa94216aea992a08679ff74880e02dcc79f20a2a01b7034&")
    # Initialize variables to collect data
    results = []
    total_fragments = 0
    max_frag = 22536  # Example max fragments value

    # Add fields to embed for each category's progress
    for category, max_level in args_dict.items():
        response, frag = await calculate_progress(category, max_level)
        total_fragments += frag
        # Add each category's progress to the embed
        embed.add_field(name=f"{category} Progress", value=response, inline=True)

    # Calculate remaining fragments and progression percentage
    remaining_fragments = max_frag - total_fragments
    progression_percentage = (total_fragments / max_frag) * 100

    # Create a visual progress bar
    progress_bar_length = 10  # Number of segments in the progress bar
    filled_segments = int(progression_percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Add summary fields for total fragments and progression
    embed.add_field(name="Total Fragments Collected", value=f"`{total_fragments}/{max_frag}`", inline=False)
    embed.add_field(name="Fragments Needed to Complete", value=f"`{remaining_fragments}`", inline=False)
    embed.add_field(name="Overall Progression", value=f"`{progression_percentage:.2f}%` {progress_bar}", inline=False)

    # Set a footer for context (optional)
    embed.set_footer(text="Progress data updated just now")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)
@client.command()
async def sen_pf(ctx, *args):
    # Parse arguments into a dictionary
    args_dict = {}
    for i in range(0, len(args), 2):
        category = args[i]
        level = int(args[i + 1])
        args_dict[category] = level

    # Create the embed for the summary
    embed = discord.Embed(
        title="📊 Sen Coi Progress Summary",
        description="Detailed Progress across all Categories",
        color=discord.Color.blue()
    )
    # embed.set_thumbnail(url="")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1154955903196463154/1303761157504634910/Screenshot_2024-11-06_at_10.41.18.png?ex=672cedb2&is=672b9c32&hm=c01fc79aaaff5fb6ac44d34d9aef49e3cb212db59243aafcc241752e5d5c6bdc&")
    # Initialize variables to collect data
    results = []
    total_fragments = 0
    max_frag = 22536  # Example max fragments value

    # Add fields to embed for each category's progress
    for category, max_level in args_dict.items():
        response, frag = await calculate_progress(category, max_level)
        total_fragments += frag
        # Add each category's progress to the embed
        embed.add_field(name=f"{category} Progress", value=response, inline=True)

    # Calculate remaining fragments and progression percentage
    remaining_fragments = max_frag - total_fragments
    progression_percentage = (total_fragments / max_frag) * 100

    # Create a visual progress bar
    progress_bar_length = 10  # Number of segments in the progress bar
    filled_segments = int(progression_percentage / 10)  # Each segment represents 10%
    empty_segments = progress_bar_length - filled_segments
    progress_bar = "🟩" * filled_segments + "⬜" * empty_segments

    # Add summary fields for total fragments and progression
    embed.add_field(name="Total Fragments Collected", value=f"`{total_fragments}/{max_frag}`", inline=False)
    embed.add_field(name="Fragments Needed to Complete", value=f"`{remaining_fragments}`", inline=False)
    embed.add_field(name="Overall Progression", value=f"`{progression_percentage:.2f}%` {progress_bar}", inline=False)

    # Set a footer for context (optional)
    embed.set_footer(text="Progress data updated just now")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)
client.run(TOKEN)
