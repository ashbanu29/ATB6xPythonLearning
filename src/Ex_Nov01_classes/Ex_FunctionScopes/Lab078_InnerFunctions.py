var1 = "var1"
var2 = "var2"
var3 = "var3"

def var_func():
    print(var1)
    print(var2)

    def inner_var_func2():
        print(var3)
        var4= "var4"
        print(var4)

    inner_var_func2()
var_func()
