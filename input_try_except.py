print("Hello world")

def  fdivide(x,y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = int(x) //int(y)
    except:
        print("Sorry ! You gave not numeric values or trying to devide by zero ")
    else:
        print("Yeah ! Your answer is :", result)
        global err
        err = 0
        print("Error indicator in function is: " + str(err))
        return err
		
err = 1

while err == 1:
    print("Error indicator is: " + str(err))
    x = input('x?\n')
    y = input('y?\n')
    fdivide(x,y)
    

print("Finished ")
