import inject
from test import BaseTestInject


class TestInjectInstance(BaseTestInject):
    def test_new(self):
        class Dummy:
            def __init__(self, param: int = None) -> None:
                self.param = param
        
        inject.configure(lambda binder: binder.bind(Dummy, Dummy))

        instance = inject.new(Dummy)
        assert instance.param == None

        instance = inject.new(Dummy, param=10)
        assert instance.param == 10

        instance = inject.new(Dummy, param=20)
        assert instance.param == 20
