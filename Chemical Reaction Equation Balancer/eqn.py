from random import randint
from math import gcd
from functools import reduce

class Equation:
    """
    class of reaction equation
    """
    def __init__(self, equation):
        """
        initialize equation
        """
        self.left = list()
        self.right = list()
        self.balanced = list()

        integers = "0123456789"
        split = equation.split(" = ")
        left_side = split[0]
        right_side = split[1]

        left_components = left_side.split(" + ")
        right_components = right_side.split(" + ")

        total_left = dict()
        total_right = dict()
        
        for component in left_components:
            left_count = dict()
            for i in range(0,len(component)):
                if component[i] == ")":
                    if component[i-2] == "(":
                        element = component[i-1:i]
                    elif component[i-3] == "(":
                        element = component[i-2:i]
                    
                    try:
                        if component[i+3] in integers:
                            number = int(component[i+1:i+4])
                        elif component[i+2] in integers:
                            number = int(component[i+1:i+3])
                        else:
                            number = int(component[i+1])
                    
                    except IndexError:
                        try:
                            if component[i + 2] in integers:
                                number = int(component[i+1:i+3])
                            else:
                                number = int(component[i+1])

                        except IndexError:
                            try:
                                number = int(component[i+1])

                    if element in left_components:
                        left_count[element] += number
                    else:
                        left_count[element] = number

                    if element in total_left:
                        total_left[element] += number
                    else:
                        total_left[element] = number
            
            self.left.append(left_count)


        
        for component in right_components:
            right_count = dict()
            for i in range(0,len(component)):
                if component[i] == ")":
                    if component[i-2] == "(":
                        element = component[i-1:i]
                    elif component[i-3] == "(":
                        element = component[i-2:i]
                    
                    try:
                        if component[i+3] in integers:
                            number = int(component[i+1:i+4])
                        elif component[i+2] in integers:
                            number = int(component[i+1:i+3])
                        else:
                            number = int(component[i+1])
                    
                    except IndexError:
                        try:
                            if component[i + 2] in integers:
                                number = int(component[i+1:i+3])
                            else:
                                number = int(component[i+1])

                        except IndexError:
                            try:
                                number = int(component[i+1])

                    if element in right_components:
                        right_count[element] += number
                    else:
                        right_count[element] = number

                    if element in total_left:
                        total_left[element] += number
                    else:
                        total_left[element] = number
            
            self.right.append(left_count)

        for key in total_left:
            if total_left[key] != total_right[key]:
                self.balanced = False
            else:
                continue