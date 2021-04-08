class Devops:
    def __init__(self, **kwargs)):
        for k, v in kwargs.items():
            setattr(self, k, v)


p1 = Devops("John", 36)

#print(p1.name)
#print(p1.age) 