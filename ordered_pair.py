""" 
    @author Arash Alaei <arashalaei22@gmail.com>.
    @since 5/5/2021
"""

def sum(a:tuple, b:tuple):
    return (a[0] + b[0], a[1] + b[1])
    
def manhattan_distance(a:tuple, b:tuple):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))