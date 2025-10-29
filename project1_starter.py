"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Kami Strain
Date: 10-20-2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
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
    character_class = character_class.capitalize()
    classes = ["Wizard", "Sorcerer", "Warlock", "Barbarian", "Monk"]

    if character_class not in classes:
        print("Error: Invalid character class: " + character_class)
        return None

    level = 1 # Starting level
    character_stats = calculate_stats(character_class, level)

    # Gold Values
    if character_class == "Wizard":
        char_gold = 100
    elif character_class == "Sorcerer":
        char_gold = 80
    elif character_class == "Warlock":
        char_gold = 75
    elif character_class == "Barbarian":
        char_gold = 60
    elif character_class == "Monk":
        char_gold = 45
    else:
        char_gold = 25

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": character_stats[0],
        "magic": character_stats[1],
        "health": character_stats[2],
        "gold": char_gold
}
    return character

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)

    - Wizards: Medium strength, high magic, medium health
    - Sorcerers: Medium strength, medium magic, low health
    - Warlocks: Low strength, medium magic, medium health
    - Barbarians: High strength, low magic, high health
    - Monks: High strength, low magic, low health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    if character_class == "Wizard":
        strength = 8 + (level * 4)
        magic = 10 + (level * 6)
        health = 75 + (level * 4)
    elif character_class == "Sorcerer":
        strength = 7 + (level * 4)
        magic = 8 + (level * 4)
        health = 45 + (level * 2)
    elif character_class == "Warlock":
        strength = 5 + (level * 2)
        magic = 7 + (level * 4)
        health = 80 + (level * 4)
    elif character_class == "Barbarian":
        strength = 10 + (level * 6)
        magic = 5 + (level * 2)
        health = 90 + (level * 6)
    elif character_class == "Monk":
        strength = 9 + (level * 6)
        magic = 6 + (level * 2)
        health = 50 + (level * 3)
    else:
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
    valid_keys = ["Name", "Class", "Level", "Strength", "Magic", "Health", "Gold"]
    for key in valid_keys:
        if key not in character:
            return False

    with open(filename, "w") as file:
        file.write(f"Character name: {character["name"]}\n")
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
    if os.path.exists(filename) != True:
        print("File not found")
        return None

    with open(filename, "r") as file:
        lines = file.readlines()

    character = {}
    key_map = {
        "Character Name": "name",
        "Class": "class",
        "Level": "level",
        "Strength": "strength",
        "Magic": "magic",
        "Health": "health",
        "Gold": "gold"
    }

    for line in lines:
        line = line.strip()
        if ": " in line:
            key, value = line.split(": ", 1)
            if key in key_map:
                new_key = key_map[key]
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
    character["level"] += 1
    update_stats = calculate_stats(character["class"], character["level"])
    if update_stats is not None:
        character["strength"] = update_stats[0]
        character["magic"] = update_stats[1]
        character["health"] = update_stats[2]
    character["gold"] += 55

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
    char = create_character("Kami", "wizard")
    display_character(char)
    save_character(char, "my_character.txt")
    loaded_char = load_character("my_character.txt")
