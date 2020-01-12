def fibonacci(num):
    print("printing fibonacci numbers till ", num)
    v = 1
    v1 = 1
    v2 = v + v1

    print(v)
    print(v1)

    while v2 < num:
        print(v2)
        v = v1
        v1 = v2
        v2 = v + v1

fibonacci(10)
fibonacci(20)
fibonacci(500)
