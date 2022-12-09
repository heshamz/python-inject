from abc import ABC, abstractmethod
import inject
from test import BaseTestInject

class IDummy(ABC):
    @abstractmethod
    def do(): pass

class Dummy(IDummy):
    def __init__(self, param: int = None) -> None:
        self.param = param
    
    def do(): pass                

def my_config(binder):
    binder.bind(Dummy, Dummy(param=1001))
    binder.bind_to_type(IDummy, Dummy)

class TestInjectInstance(BaseTestInject):
    def test_new(self):

        inject.configure(my_config)

        instance1 = inject.instance(Dummy)
        assert instance1.param == 1001

        instance2 = inject.instance(Dummy)
        
        assert instance1 == instance2
        
        instance1 = inject.instance(IDummy)
        assert instance1.param == None
        
        instance2 = inject.instance(IDummy)
        assert instance2.param == None

        assert instance1 != instance2

        with self.assertRaises(inject.InjectorException):
            inject.new(Dummy)

        instance1 = inject.new(IDummy, param=10)
        assert instance1.param == 10

        instance2 = inject.new(IDummy, param=20)
        assert instance2.param == 20

        assert instance1 != instance2
        