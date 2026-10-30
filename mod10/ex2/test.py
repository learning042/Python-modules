a = 1
def outer():
    a = 2
    def inner():
        print(a)
    return inner

func = outer()
func()
