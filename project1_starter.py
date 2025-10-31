"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Kami Strain
Date: 10-20-2025

AI Usage: AI (ChatGPT) helped with:
- Fixing errors and logic in functions using files (without using try/except)
- Improving code readability
- Correcting string formatting and key mapping issues in save/load functions
"""

import os

def create_character(name, character_class='Monk'):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    character_class = character_class.capitalize() # Capitalize class name for consistency
    classes = ["Warrior", "Mage", "Rogue", "Cleric"]

    # Check if the class is valid
    if character_class not in classes:
        print("Error: Invalid character class: " + character_class)
        return None

    level = 1 # Starting level for all characters
    character_stats = calculate_stats(character_class, level)

    # Gold values based on class
    if character_class == "Warrior":
        gold = 100
    elif character_class == "Mage":
        gold = 80
    elif character_class == "Rogue":
        gold = 75
    elif character_class == "Cleric":
        gold = 60
    else:
        gold = 25

    # Create the character dictionary
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": character_stats[0],
        "magic": character_stats[1],
        "health": character_stats[2],
        "gold": gold
}
    return character

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)

    - Warriors: Medium strength, high magic, medium health
    - Mage: Medium strength, medium magic, low health
    - Rogues Low strength, medium magic, medium health
    - Clerics: High strength, low magic, high health
    - Default: Low strength, low magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    # Each class has unique stat scaling
    if character_class == "Warrior":
        strength = 8 + (level * 4)
        magic = 10 + (level * 6)
        health = 75 + (level * 4)
    elif character_class == "Mage":
        strength = 7 + (level * 4)
        magic = 8 + (level * 4)
        health = 45 + (level * 2)
    elif character_class == "Rogue":
        strength = 5 + (level * 2)
        magic = 7 + (level * 4)
        health = 80 + (level * 4)
    elif character_class == "Cleric":
        strength = 10 + (level * 6)
        magic = 5 + (level * 2)
        health = 90 + (level * 6)
    else:
        # Default stats for unknown class
        strength = 5 + (level * 2)
        magic = 5 + (level * 2)
        health = 80 + (level * 2)

    return strength, magic, health

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    # Ensure character has all required keys
    for key in required_keys:
        if key not in character:
            return False

    path = os.path.split(filename)[0]
    if path and not os.path.exists(path):
        return False

    # Write character data to file
    with open(filename, "w") as file:
        file.write(f"Character Name: {character["name"]}\n")
        file.write(f"Class: {character["class"]}\n")
        file.write(f"Level: {character["level"]}\n")
        file.write(f"Strength: {character["strength"]}\n")
        file.write(f"Magic: {character["magic"]}\n")
        file.write(f"Health: {character["health"]}\n")
        file.write(f"Gold: {character["gold"]}\n")
    return True

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    # Check if file exists
    if not os.path.exists(filename):
        print("File not found")
        return None

    # Read all lines from file
    with open(filename, "r") as file:
        lines = file.readlines()

    character = {}
    # Mapping between file labels and dictionary keys
    key_map = {
        "Character Name": "name",
        "Class": "class",
        "Level": "level",
        "Strength": "strength",
        "Magic": "magic",
        "Health": "health",
        "Gold": "gold"
    }

    # Parse each line and extract key/value pairs
    for line in lines:
        line = line.strip()
        if ": " in line:
            key, value = line.split(": ", 1)
            if key in key_map:
                new_key = key_map[key]
                # Convert numbers to integers
                if new_key in ["level", "strength", "magic", "health", "gold"]:
                    character[new_key] = int(value)
                else:
                    character[new_key] = value
    return character

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("=======================")

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    # Increase level by 1
    character["level"] += 1
    
    update_stats = calculate_stats(character["class"], character["level"])
    
    if update_stats is not None:
        character["strength"] = update_stats[0]
        character["magic"] = update_stats[1]
        character["health"] = update_stats[2]
    
    # Add bonus gold for leveling up
    character["gold"] += 50

    print(f"{character['name']} Leveled Up! {character['name']}'s New Level Is: {character['level']}")
# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
    char = create_character("Kami", "cleric")
    display_character(char)
    save_character(char, "my_character.txt")
    loaded_char = load_character("my_character.txt")
