def has_negatives(a):
    """
    YOUR CODE HERE
    input is an array of integers
    output is an array of integers
    """
    # Your code here
    cache = {}
    result = []
    
    for element in a:
        if element not in cache:
            cache[element] = 1
            cache[-element] = 2
        if cache[element] == cache[-element]:
            result.append(element)
            print(result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
 