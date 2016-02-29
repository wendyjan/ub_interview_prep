"""

"""


def dot_product(a, b):
    sum = 0
    if len(a) != len(b):
        return None
    for i in range(len(a)):
        new_term = a[i] * b[i]
        sum += new_term
    return float(sum)  # Returning a float isn't required, but it makes for nice uniform behavior if we accept vectors that may contain floats or ints.


if __name__ == "__main__":
    vector1 = [1, 2, 3]
    vector2 = [4, 1, 2]
    msg = "The dot product of {0} and {1} is {2}" 
    print (msg.format(str(vector1), str(vector2), str(dot_product(vector1, vector2))))
    vector2 = [8, 1, 1] 
    print (msg.format(str(vector1), str(vector2), str(dot_product(vector1, vector2))))
    vector2 = [0, 1, 1] 
    print (msg.format(str(vector1), str(vector2), str(dot_product(vector1, vector2))))
