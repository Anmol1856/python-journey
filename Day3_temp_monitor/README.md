#  Day 3 – Smart Temperature Monitoring System

This project is a simple simulation of a temperature-based control system.
It takes temperature input from the user and decides how the system should respond (fan, heater, alert, etc.)
##  What this project does
-Takes temperature as input
-Analyzes the value
-Decides system behavior:

  -High temperature - Alert / Cooling
  -Low temperature - Heating
  -Normal - Stable system

## How this is different from Day 2

In Day 2, I created similar logic using simple if-else statements in a direct way.

In Day 3, the same idea is implemented in a better structured way:

-Code is divided into multiple files
-Each file has a specific role
-Functions are used for better control

 Even though the output looks similar, the internal design is much cleaner and closer to real-world systems.

## Project Structure
-main.py = Controls the flow of the program
-sensor.py = Takes temperature input
-controller.py = Decides what action to take
-alert.py = Displays the system response

 