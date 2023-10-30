for p_i in range(1,101):
    if p_i % 3 == 0:
        if p_i % 5 == 0:
            print("FizzBuzz")
        else:
             print("Fizz")
    elif p_i % 5 == 0:
        print("Buzz")
    else:
        print(p_i)