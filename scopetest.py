def test():
    #global b
    #b=20
    #global a
    #a=10
    print("Inside test() a=%d"%(a))
    print("Inside test() b=%d"%(b))
a=1
print("Outside test() a=%d"%(a))
test()
print("Outside test() a=%d"%(a))
print("Outside test() b=%d"%(b))

#b is not visible outside of function and a is not visible inside the function.
#removing the # in front of global b doesnt change anything as b is undefined and # is just a statement.
#removing the # from global a doesnt change the output.
#removing the # from a=10 changes the output from a=1 to a=10.