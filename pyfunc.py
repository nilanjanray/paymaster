'''
def outerfunc(func):
    def innerfunc(**args):
        return func(**args)
    return innerfunc
'''

def outnerfuncv(**args):
    def innerfuncv(func):
        def anotherinner(**arg):
            print(args.items())
            return func(**arg)
        return anotherinner
    return innerfuncv 

'''
@outerfunc
def apyfuncv(**args):
    return args.items()
'''

@outnerfuncv(team='india', nation='Indian')
def apyfuncanother(**args):
    return args.items()

#print(apyfunc(name='nilanjan',stack='Kubernetes'))
print(apyfuncanother(name='nilanjan',stack='Kubernetes'))
