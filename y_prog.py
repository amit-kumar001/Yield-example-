# First we define next() function 
def next():
    i=1           # declare the value of i=1
    while True:   # while True is for infinte loop 
        yield i*i #  yield use for iteration over the multiple vales 
        i+=1      # for increment in term of 1

for result in next(): # here we are iterating over the function next()
    if result > 100: # now we set the condition to stop while loop
        break        # break  statement  use to stop while loop
    print(result)
    
