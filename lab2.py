def string_ex():
    word1 = "hello"
    word2 = "Hello"
    print(f"word1: {word1}")
    print(f"word2: {word2}")
    print(word1 == word2)
    print(type(word1))
    print(type(word2))
    word3 = str(123)
    print(f"word3: {word3}")
    i = int('123')
    j = float('123.4')
    print(f"i: {i}, j: {j}")
    print(f"word1_len: {len(word1)}")
    print(f"hello_index_No2: {'hello'[2]}")
    print(f"hello_No4: {word1[4]} hello_No-5: {word1[-5]}")
    digits = "0123456789"
    print(f"digits1-4: {digits[1:4]}")
    print(f"digits0-4: {digits[:4]}")
    print(f"digits5-: {digits[5:]}")
    print(f"digits_3_9_2: {digits[3:9:2]}")
    price = "2,980円"
    print(f"price_before: {price}")
    price = price.replace(",", "")
    print(f"price_after: {price}")

def search():
    if 'lo' in 'hello':
        print("lo in hello")
    else:
        print("lo not in hello")
    
    escaped = "My name is \"トーマス\"." 
    print(f"escaped: {escaped}")
    
    word1 = "hello"
    word1 = word1 * 3
    print(f"word1: {word1}")
    
    print(f"word1_replace: {word1.replace('l', '123')}")

def list_ex():
    abcd = ['a', 'b', 'c', 'd']
    print(f"abcd: {abcd}")
    print(f"abcd[1]: {abcd[1]}")
    print(f"abcd[1:3]: {abcd[1:3]}")
    lns = [[1,2, 3], [4, 5, 6] ,['a', 'b', 'c']]
    print(f"lns[1]: {lns[1]}")
    print(f"lns[1][1]: {lns[1][1]}")
    print(f"len_lns: {len(lns)}")
    print(f"total: {sum([])}")
    
    zero = [0] * 5
    
    print(f"[0] * 5: {zero}")
    
    a1 = 1
    
    print(f"1_in_a1: {a1 in [1, 2, 3]}")
    
    numbers = [50, 90, 80, 10, 5, 70]
    numbers.append(100)
    print(f"numbers.append(100): {numbers}")
    
    numbers.sort()
    print(f"numbers.sort(): {numbers}")
    
    numbers.sort(reverse=True)
    
    print(f"numbers.sort(reverse): {numbers}")
    
    print(f"sorted(numbers): {sorted(numbers)}")
    
    numbers.sort()
    
    print(f"sorted(numbers) == numbers.sort(): {sorted(numbers) == numbers}")
    
    numbers.extend([90, 110, 130, 150])
    
    print(f"numbers.extend([90, 110, 130, 150]): {numbers}")
    
    numbers.insert(0, 40)
    
    print(f"numbers.insert(0, 40): {numbers}")
    
    numbers.remove(40)
    
    print(f"numbers.remove(40): {numbers}")
    
    numbers.pop(1)
    
    print(f"numbers.pop(1): {numbers}")
    
    del numbers[1: 9]
    
    print(f"del numbers[1: 9]: {numbers}")
    
    numbers.reverse()
    
    print(f"numbers.reverse(): {numbers}")
    
    numbers2 = numbers.copy()
    
    print(f"numbers2 = numbers.copy(): {numbers2}")
    
    numbers2.append(50)
    
    print(f"numbers, numbers2.append(50): {numbers, numbers2}")
    
    
    numbers2 = numbers
    
    print(f"numbers2 = numbers: {numbers2}")
    
    numbers.append(50)
    
    print(f"numbers, numbers2.append(50): {numbers, numbers2}")
    
    print(f"list('abc123): {list('abc123')}")
    
    print(f"A and B and C split: {'A and B and C'.split(' and ')}")
    
    print(f"''.join(['a', 'b' , 'c' , '1', '2', '3']): {''.join(['a', 'b' , 'c' , '1', '2', '3'])}") 

    print(f"'n'.join(['ba', 'a', 'a']): {'n'.join(['ba', 'a', 'a'])}")
    
    x  = 10
    y = 20
    
    print(f"x: {x}, y: {y}, point: {(x, y)}, type(point): {type((x, y))}")
    
    ls = [0,1,2]
    
    for value in ls:
        print('For loop:', value)
        
    str1 = 'Apple and pen'
    
    for c in str1:
        print(c.upper())
        
    a = []
    
    b = []
        
    print(f" a == b:{a == b}, a is b: {a is b}")

def main():
    string_ex()
    search()
    list_ex()

main()