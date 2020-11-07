import random
def intersection(arrays):
    """
    YOUR CODE HERE
    #UNDERSTAND
    #find all of the numbers that repeat in each list let return those repeated integers
    #PLAN
    # To do this, we would need to iterate over each list and assign each
    # integer a key so that every time that integer is encountered it is add to that key as a value?
    #EXECUTE
    # [
    #   [0]
    #   [1]
    #   [2]
    # ]
    # If we set a 
    # set a value in a dict with [ ]
        # item = {}
        # item['a'] = 'alpha'
    # dict ={}

    # what would we use as a key?
    """
    # Your code here
    result = {}
    
    
    for list in arrays:
        for element in list:
            if element not in result:
                result[element] = 1
            else:
                result[element] += 1
                
    return result

        
       
    


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
