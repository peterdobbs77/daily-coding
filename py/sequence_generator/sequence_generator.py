# import os
import sys

class sequence_generator:
    '''This class utilizes the Context Manager pattern to provide a sequence generator'''

    def __init__(self, start: int, step: int):
        self._step = step
        self._current = start
    
    def __enter__(self):
        while True:
            yield self._current
            self._current += self._step
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    start = int(input().strip())
    step = int(input().strip())
    num = int(input().strip())
    
    with sequence_generator(start, step) as gen:
        for i in range(num):
            fptr.write(str(next(gen)) + '\n')

    fptr.close()