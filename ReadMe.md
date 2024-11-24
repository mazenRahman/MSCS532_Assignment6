# Assignment 6: Medians and Order Statistics & Elementary Data Structures

## Overview

This repository contains the solution to **Assignment 6**, which is focused on implementing selection algorithms (for order statistics) and elementary data structures. The assignment is divided into two parts:

1. **Selection Algorithms (Medians and Order Statistics)**: 
   - Implementing both deterministic (Median of Medians) and randomized (Randomized Quickselect) algorithms for selecting the k-th smallest element in an array.
   - Performance analysis and empirical comparison of both algorithms.

2. **Elementary Data Structures**: 
   - Implementing basic data structures such as arrays, stacks, queues, and linked lists.
   - Analyzing the time complexity of their operations and discussing their practical applications.

## Part 1: Selection Algorithms

### Algorithms Implemented:
- **Deterministic Selection Algorithm (Median of Medians)**: This algorithm selects the k-th smallest element in worst-case linear time, O(n).
- **Randomized Selection Algorithm (Randomized Quickselect)**: This algorithm selects the k-th smallest element in expected linear time, O(n).

### Performance Analysis:
- Time and space complexity analysis for both algorithms is provided.
- Empirical analysis compares the running time of both algorithms on various input sizes and distributions.

### Files:
- `selection.py`: Contains the implementation of both selection algorithms.
- `selection_report.pdf`: A report detailing the implementation, performance analysis, and empirical results.

## Part 2: Elementary Data Structures

### Data Structures Implemented:
- **Arrays**: Basic operations like insertion, deletion, and access.
- **Stacks and Queues**: Implemented using arrays with basic operations like push, pop, enqueue, and dequeue.
- **Singly Linked Lists**: Implemented with operations like insertion, deletion, and traversal.
- **Optionally Implemented Rooted Trees**: Represented using linked lists for nodes and their relationships.

### Performance Analysis:
- Time complexity analysis for the basic operations of each data structure is included.
- A discussion on trade-offs between arrays and linked lists for stacks and queues.

### Files:
- `data_structures.py`: Contains the implementation of arrays, stacks, queues, linked lists, and optionally rooted trees.
- `data_structures_report.pdf`: A report discussing the performance analysis and practical applications of the data structures.

## How to Run the Code

1. Clone this repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Run the Python scripts for both selection algorithms and data structures:
   - For selection algorithms: `python selection.py`
   - For data structures: `python data_structures.py`

## Report and Analysis

Both detailed reports for Part 1 (Selection Algorithms) and Part 2 (Data Structures) are included in the `selection_report.pdf` and `data_structures_report.pdf` files. The reports include:
- Time complexity analysis
- Empirical results and comparisons
- Practical applications of the data structures

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for reviewing my assignment!
