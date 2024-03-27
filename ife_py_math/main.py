def power(n:int, x:int)->float:
    """
    Calculates the power of a number

    n:is the base
    x: is the power
    """
    if x >= 0:
        result = 1
        for _ in range(x):
            result *= n
        return result
    else:
        result = 1
        for _ in range(abs(x)):
            result *= n
        return 1 / result


def factorial(x:int)->int:
    """
    calculated the factorial of a number

    x is the value of factorial to be gotten
    """
    f=1
    if x<0:
        raise ValueError("You cannot find the factorial of a negative number")
    else:
        while(x>=1):
            f=f*x
            x=x-1
        return f

def permutation(x:int,y:int)->float:
    """
    calculates the permutation of a number
    x:value at the top
    p:value to be permuted against
    """
    if y>x:
        raise ValueError('y cannot be greater that x')
    else:
        num=factorial(x)
        denominator=factorial(x-y)
        answer=num/denominator
        return answer

def combination(x:int,y:int)->float:
    """
    calculates the combination of a number
    
    x:value at the top
    y:value operation is perfomed against
    """
    if y>x:
        raise ValueError("value of y cannot be greater than that of x")
    else:
        num=factorial(x)
        denominator=factorial(x-y)*factorial(y)
        answer=num/denominator
        return answer