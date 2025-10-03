# Bubble Sort Visualizer

A Python project using **Pygame** to visually demonstrate the **Bubble Sort** algorithm step by step. Users can generate a random list of integers, watch the sorting process in real time, and measure the time taken to sort.

---

## Features

- Generate a random list of numbers.
- Visualize the Bubble Sort algorithm step by step.
- Highlight array elements with a gradient color scheme.
- Reset the list to a new random sequence.
- Display sorting time in seconds.
- Adjustable visualization speed with delays.



---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bubble-sort-visualizer.git
```

2. Navigate to the project folder:
```bash
cd bubble-sort-visualizer
```

3. Install dependencies (Requires Python 3.x):
```bash
pip install pygame
```

## How to use
Run the main script:

```bash
python alg.py
```

## Controls:
- R - Reset the list with new random rectangles (Numbers)
- B - Start the Bubble Sort visualization.
- More Sorting functions to come

## How it works:
- The program generates a list of random integers.
- Each integer is represented as a vertical bar on the screen.
- When B is pressed, the program animates the Bubble Sort:
  - Compares adjacent elements.
  - Swaps elements if necessary.
  - Shows the progress visually with colors.
- A timer measures how long the sorting took (with optional visualization delay).

## Customization
- Adjust the number of elements by modifying the n variable in main().
- Change the min and max values for the list by modifying min_val and max_val.
- Adjust the delay between steps for faster or slower animations.

## Learning Outcomes:
- Implementation of the Bubble Sort algorithm.
- Basic Pygame usage for graphics and animations.
- Real-time visualization of sorting algorithms.
- Measuring execution time for algorithms.

## Author

https://github.com/RaphT197
