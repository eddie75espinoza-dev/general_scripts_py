from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def do_operation(self, param1, param2):
        pass


class Context:
    def __init__(self, strategy):
        self._strategy = strategy
    
    def execute_strategy(self, param1, param2):
        return self._strategy.do_operation(param1, param2)


class ConcreteStrategyAdd(Strategy):
    def do_operation(self, param1, param2):
        return param1 + param2


class ConcreteStrategySubtract(Strategy):
    def do_operation(self, param1, param2):
        return param1 - param2


class ConcreteStrategyMultiply(Strategy):
    def do_operation(self, param1, param2):
        return param1 * param2


context = Context(ConcreteStrategyAdd())
result = context.execute_strategy(10, 5)  # Resultado es 15
print(result)

context = Context(ConcreteStrategySubtract())
result = context.execute_strategy(10, 5)  # Resultado es 5
print(result)

context = Context(ConcreteStrategyMultiply())
result = context.execute_strategy(10, 5)  # Resultado es 50
print(result)
