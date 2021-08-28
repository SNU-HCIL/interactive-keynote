import json 
import copy
import argparse


parser = argparse.ArgumentParser(description='Converts markdown to jupyter notebook format')

parser.add_argument("-i", "--input-path", help='Reads markdown file designated by the path and converts it to jupyter file')
parser.add_argument("-o", "--output-path", default="", help="Designates output file path")

args  = parser.parse_args()
input_path = args.input_path
output_path = args.output_path

if (output_path == ""):
    output_path = "output_" + input_path
    output_path = output_path.replace(".md", ".ipynb")



with open(input_path) as md_file:
    lines = md_file.readlines()



cell = []
cells = []
current_cell = "markdown"
for line in lines:
    if ((line[:6] == "class:") or (line[:7] == "layout:") or
        (line[:5] == "name:")   or (line[:9] == "template:")):
        continue
    if ((line[:7] == "class :") or (line[:8] == "layout :") or
        (line[:6] == "name :")   or (line[:10] == "template :")):
        continue
    if (line[:4] == ".col") or (line[:4] == ".row"):
        continue
    if (line == "]\n"):
        cell.append("\n")
        continue
    
    if ('```python' in line) or ('```python3' in line):
        if len(cell) > 0:
            cells.append({
                "source": copy.deepcopy(cell),
                "cell_type": current_cell
            })
            cell = []
        current_cell = "code"
        continue
        
    if (current_cell == "code"):
        if ("```" in line and "```python" not in line and "```python3" not in line):
            cells.append({
                "source": copy.deepcopy(cell),
                "cell_type": current_cell
            })
            cell = []
            current_cell = "markdown"
            continue
    
    if ("---" in line):
        cells.append({
            "source": copy.deepcopy(cell),
            "cell_type": current_cell
        })
        cell = []
        continue
        
    cell.append(line)
        

if len(cell) > 0:
    cells.append({
        "source": copy.deepcopy(cell),
        "cell_type": current_cell
    })
    
    
for cell in cells:
    cell["metadata"] = {}
    if cell["cell_type"] == "code":
        cell["output"] = []
        
output_cells = {
    "cells": cells,
    "metadata": {
      "kernelspec": {
       "display_name": "Python 3",
       "language": "python",
       "name": "python3"
      },
      "language_info": {
       "codemirror_mode": {
        "name": "ipython",
        "version": 3
       },
       "file_extension": ".py",
       "mimetype": "text/x-python",
       "name": "python",
       "nbconvert_exporter": "python",
       "pygments_lexer": "ipython3",
       "version": "3.6.9"
      }
     },
    "nbformat": 4,
    "nbformat_minor": 4
}

with open(output_path, "w") as output_file:
    json.dump(output_cells, output_file)
