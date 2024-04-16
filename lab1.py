import math

def suti():
    x = 100
    y = 50
    z = x * y
    print(f"x: {x}, y: {y}, z:{z}")
    a = [i for i in range(1, 11)]
    print(a)
    sin = math.sin(math.pi/2)
    cos = math.cos(math.pi/2)
    print(f"sin: {sin}, cos: {cos}")

def hensu():
    h = 188.0 
    w = 67.5
    BMI = w / (h/100.0) ** 2
    print(f"BMI: {BMI}")
    w += 10
    w -= 10
    print(f"w: {w}")
    str1 = "50"
    str2 = "50"
    print(f"sum_str: {str1+ str2}")
    print(f"int_str: {int(str1) + int(str2)}")
    
    dict = {"apple": 100, "banana": 200}
    print(f"dict: {dict}")
    print(f"dict[apple]: {dict['apple']}")
    
    lst = [n for n in range(1, 11)]
    print(f"lst_bedore: {lst}")
    lst.append(20)
    print(f"lst_after: {lst}")
    
    
def max_min(a, b):
    if a > b:
        print(f"max: {a}")
    if a < b:
        print(f"max: {b}")
    else:
        print(f"equal")
        
    c = True
    if c != False:
        print("True")
    else:
        print("False")
    
    if 0:
        print("True")
    else:
        print("False")
        
    if -1:
        print("True")
    else:
        print("False")

def f_sum(n):
    if n == 0:
        return 0
    return n + f_sum(n-1)

def debug(x, y):
    z = x**2 + y**2
    assert z < 0
    print(f"z: {z}")
    
def main():
    suti()
    hensu()
    max_min(10, 20)
    print(f"Total: {f_sum(100)}")
    debug(3, 4)
    
main()