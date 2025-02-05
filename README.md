<<<<<<< HEAD
# Updated_Crane_Problem
=======
# Interview Code Challenge

## Problem Statement

For this challenge you are tasked with creating a Python implementation that models a crane system and performs various calculations.

### Background Materials

* Reference Diagram: See `crane_diagram.pdf`
* Samples: 
  * The PDF includes a sample question taken from an engineering exam along with the solution. This is meant to provide a reference to the methodology that can be used to solve the problem. A guide video is also provided: <https://www.youtube.com/watch?v=nHSgseibXIk>

  * Finding the Tension of a Cable Supporting a Beam <https://www.youtube.com/watch?v=lcikKSFq7c8>

### Challenge Overview

The challenge is divided into three parts:

1. Crane Object Modeling
   * create a main `Crane` class with three sub-components:
     * base crane:
       * fixed position
       * contains connection points
       * class attributes should include position coordinates and connection point locations

     * boom:
       * rotates about the base foot pin
       * class attributes should include length, current angle, and connection point locations

     * main suspension:
       * variable length component
       * class attributes should include currenth length, and connection point locations

   * the main `Crane` class should maintain the relationships between these components and ensure geometric consistency

   * a starting point for implementation can be found in `src/models`

2. Load Displacement Calculation
   * implement a function that takes the following input parameters:
     * a `Crane` object
     * the distance from the building edge to the crane base (labeled as "A" in the diagram)

   * the minimum standoff point as provided in the reference problem and solution is not provided in the diagram, however a helper function is provided that can be used to obtain it using the measurements that are provided

   * returns the calculated maximum distance from the edge of the building that a load can be placed on top of the building without the crane touching the building (labeled as "B" in the diagram)

   * a starting point for implementation can be found in `src/calculations.py` and `src/__main__.py`

3. Bonus Challenge (optional)
   * implement a function that takes the following input parameters:
     * a `Crane` object
     * a hook load weight

   * returns the calculated tension on the main suspension

## Prerequisites

* Python 3.x
* [uv](https://docs.astral.sh/uv) for dependency management <https://docs.astral.sh/uv/getting-started/installation>
  * this is only a recommendation and is optional

## Getting Started

Using `uv`, you can install dependencies and activate the virtual environment:

```bash
uv sync
source .venv/bin/activate
```

## Expectations

* Code should be well commented, especially in explaining your approach
* Code should follow PEP 8 style guidelines (we use ruff)
* Including unit tests is optional, but recommended
>>>>>>> dd58112 (Inital commit and adding all project files.)
