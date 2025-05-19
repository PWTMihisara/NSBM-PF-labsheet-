def integerpower(base,exponant):
    result=1

    for _ in  range(exponant):
        result=result*base
    return result

print(integerpower(3,4))