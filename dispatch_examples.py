def handle_Duck(self, obj):
    pass

def handle_Trombonist(self, obj):
    pass

def handle_Cyclist(self, obj):
    pass

# Metdodo ignorante
if isinstance(obj, Duck):
   handle_duck(obj)
elif isinstance(obj, Trombonist):
   handle_trombonist(obj)
elif isinstance(obj, Cyclist):
   handle_cyclist(obj)
else:
   raise RuntimeError('Unknown object')

# Usando un dizionario
handlers = {
    Duck: handle_duck,
    Trombonist: handle_trombonist,
    Cyclist: handle_cyclist
}

# Dispatch
def dispatch(obj):
    func = handlers.get(type(obj))
    if func:
         return func(obj)
    else:
         raise RuntimeError(f'No handler for {obj}')

def dispatch(obj):
    for ty in type(obj).__mro__:
        func = handlers.get(ty)
        if func:
            return func(obj)
    raise RuntimeError(f'No handler for {obj}')

class Dispatcher:
    def handle(self, obj):
        for ty in type(obj).__mro__:
            meth = getattr(self, f'handle_{ty.__name__}', None)
            if meth:
                return meth(obj)
        raise RuntimeError(f'No handler for {obj}')
    
