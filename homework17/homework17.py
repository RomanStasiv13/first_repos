# Task 1
# Imports practice
# Make a directory with 2 modules; make a function in one of them;
# then import this function in the other module and use that in your script of choice.

from hw_module import some_func

func = some_func(10,2,4)
print(func)


# Task 2
# The sys module.
# The “sys.path” list is initialized from the PYTHONPATH environment variable.
# Is it possible to change it from within Python? If so, does it affect where Python looks for module files?
# Run some interactive tests to find it out.

import sys

class LookingForModule:
    @property
    def python_path(self):
        for path in sys.path:
            print(path)
    @python_path.setter
    def python_path(self, path):
        sys.path.append(path)

    def python_path_remover(self, path):
        sys.path.remove(path)

look = LookingForModule()
look.python_path
look.python_path = 'C:\RRR'
look.python_path
look.python_path_remover('C:\RRR')
look.python_path

# Task 3
# mymod.py - оно сдесь)







