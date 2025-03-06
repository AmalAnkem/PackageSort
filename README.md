Package Sorting Automation: 

This project provides a Python function, sort(width, height, length, mass), which determines the appropriate dispatch stack for packages based on their physical dimensions and mass. This function is designed for Thoughtful’s robotic automation factory to help sort packages into the correct stacks.

Overview
Packages are sorted based on the following criteria:

Bulky:
A package is considered bulky if its volume (width × height × length) is at least 1,000,000 cm³,
OR if any of its dimensions (width, height, or length) is greater than or equal to 150 cm.

Heavy:
A package is considered heavy if its mass is greater than or equal to 20 kg.

STANDARD:
Packages that are neither bulky nor heavy.

SPECIAL:
Packages that are either bulky or heavy, but not both.

REJECTED:
Packages that are both bulky and heavy.

Implementation Details
The function sort(width, height, length, mass) checks the package dimensions and mass and returns a string indicating the dispatch stack.


