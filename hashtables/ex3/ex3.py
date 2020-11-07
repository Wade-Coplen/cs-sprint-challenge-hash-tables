def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #UNDERSTAND
    #find all of the numbers that repeat in each list let return those repeated integers
    #PLAN
    # To do this, we would need to iterate over each list and assign each
    # integer a key so that every time that integer is encountered it is add to that key as a value?

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
