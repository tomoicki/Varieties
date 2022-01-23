from library import Base

assert hasattr(Base, 'foo'), 'doesnt'


class Derived(Base):
    def bar(self):
        return self.foo()
