class TraceBlock:
    def message(self, args):
        print('Running', args)
    def __enter__(self):
        print('starting with block')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise un exception', exc_type)
            return False

with TraceBlock() as action:
    action.message('test 1')
    print('reaching')

with TraceBlock as action:
    action.message('test 2')
    raise TypeError
    print('not reached')
