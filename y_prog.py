def next():
    i=1
    while True:
        yield i*i
        i+=1

for result in next():
    if result > 100:
        break
    print(result)
