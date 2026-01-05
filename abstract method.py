from abc import ABC, abstractmethod
class ABCClass(ABC):

    def print(self,x):
        print("Passed value:",x)
    
    @abstractmethod
    def task(self):
        print(" You successfully entered ABCclass task")

class test_class(ABCClass):
    def task(self):
        print(" You have implemented the abstract method task")


test_obj = test_class()
test_obj.task()
test
_obj.print(100)

