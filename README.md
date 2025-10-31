[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21184698&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# What's Your RPG About? 
My RPG is about creating fantasy characters like Warriors, Mages, Rogues, and Clerics. Each character has different strengths, magic power, and health based on their class. Players can create a character, view their stats, level them up, and save or load their progress. It’s a type of character-building system like what you’d find in a larger RPG game.

# Design Choices
I chose these formulas so each class feels unique and fits its role.
- Warriors get more strength and health to be strong fighters.
- Mages gain more magic since they focus on spells.
- Rogues have balanced stats for agility and flexibility.
- Clerics have high health and strength for support and defense.
The formulas also scale with level so characters grow stronger as they play.

# Bonus Creative Features
- I added code that sets the default class to a "Monk" so if the player doesn't   input a class, they automatically received the class and stats of a Monk.
  
- When a character levels up, I created it to where the character receives an extra 50 gold.

# AI Usage
- Help fix logic and file handling issues in save_character() and
  load_character() (without using try/except).
 
- Clarify how to handle invalid paths and class validation more efficiently.
  
- Suggest improvements with formatting.
# How To Run
python project1_starter.py
