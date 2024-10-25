#!/usr/bin/env python3
from random import random

def inverse_kinematics_dummy(X,Y,Z):
    # TODO: Use Inverse Kinematics Engine (e.g., MoveIt!) to calculate the actual value!
    A1 = random()
    A2 = random()
    A3 = random()
    A4 = random()
    A5 = random()
    A6 = random()
    return [A1, A2, A3, A4, A5, A6]

def write_to_KVP_memory_dummy(A1,A2,A3,A4,A5,A6):
    pass

filename = 'test.gcode'
fin = open(filename)
X = 0
Y = 0
Z = 0
for line in fin.readlines():
    line = line.strip()
    if line.startswith('G1'):
        if 'X' in line:
            X = line.split('X')[1].split(' ')[0]
            print('X:'+str(X)+' ',end='')
        if 'Y' in line:
            Y = line.split('Y')[1].split(' ')[0]
            print('Y:'+str(Y)+' ',end='')
        if 'Z' in line:
            Z = line.split('Z')[1].split(' ')[0]
            print('Z:'+str(Z)+ ' ',end='')
        if 'X' not in line and 'Y' not in line and 'Z' not in line:
            continue
        print()

        [X,Y,Z] = [float(X),float(Y),float(Z)]
        [A1,A2,A3,A4,A5,A6] = inverse_kinematics_dummy(X,Y,Z)
        write_to_KVP_memory_dummy(A1,A2,A3,A4,A5,A6)


fin.close()