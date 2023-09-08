"""
Define a family of algorithms, encapsulate each one, and make them
interchangeable. Strategy lets the algorithm vary independently from
clients that use it.
"""

import abc


class IStrategy(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported algorithms. Context
    uses this interface to call the algorithm defined by a
    ConcreteStrategy.
    """

    @abc.abstractmethod
    def algorithm_interface(self):
        pass


class Context:
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface()


class ConcreteStrategyA(IStrategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def algorithm_interface(self):
        print('Concrete Strategy A')


class ConcreteStrategyB(IStrategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def algorithm_interface(self):
        print('Concrete Strategy B')


def main():
    # concrete_strategy = ConcreteStrategyA()
    concrete_strategy = ConcreteStrategyB()
    context = Context(concrete_strategy)
    context.context_interface()


if __name__ == "__main__":
    main()