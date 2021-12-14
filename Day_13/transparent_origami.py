import numpy as np

def fold_once(file):
    inputs = np.char.strip(np.array(open(file, 'r').readlines()))
    blank = np.nonzero(inputs == '')[0][0]
    dots = inputs[:blank]
    instructions = inputs[blank + 1:]
    rows = []
    cols = []
    for dot in dots:
        col, row = dot.split(',')
        cols.append(col)
        rows.append(row)
    rows = np.array(rows, dtype = int)
    cols = np.array(cols, dtype = int)
    
    # for input in inputs:

fold_once('test.txt')

