# Yield-example-
## Key features
<ol>
  <li> In this program, we are explaining about the working of yield in python with break. So, for explaining this, we have coded the following program::smiley: 
     
     
   ```
   def next():
    i=1
    while True:
        yield i+i
        i+=1

for result in next():
    if result > 100:
        break
    print(result)
   
   ````
  <li> First, we have defined a function named <strong>next()</strong> which further contains a variable 'i' initialised to one and a while condition.
  <li> Yield statement suspends a function’s execution and sends a value back to caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather them computing them at once and sending them back like a list.
  <li> So, in our case while condition is true which makes an infinite loop . So, yield will retain the computed values in its state.
  <li> Further, we have used for loop for iterating over the function and checking for the stored values upto 100 in yield.
  <li> We are terminating from our for loop when it reaches to 100 using <strong>break statement</strong> and display the result which are as follows: 
  <pre>  
  1
  4
  9
  16
  25
  36
  49
  64
  81
  100
  </pre>
  
   ## How to run this file
   If you are using python 2.x version, you can run it using: 
   ```
   python2.x playing_with_python.py
   ```
   If you are using python 3.x version, you can run it using:
   ```
   python3.x playing_with_python.py
   ```
