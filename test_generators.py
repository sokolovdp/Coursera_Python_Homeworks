def accumulator():
    total = 0
    while True:
        value = yield total
        print("got {}".format(value))
        if not value:
            break
        else:
            total += value


generator = accumulator()
print(next(generator))
print("accumulated: {}".format(generator.send(1)))
print("accumulated: {}".format(generator.send(1)))
print("accumulated: {}".format(generator.send(1)))
print("accumulated: {}".format(generator.send(-1)))
