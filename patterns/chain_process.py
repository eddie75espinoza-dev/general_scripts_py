class Handler:
    def __init__(self, successor=None):
        self._successor = successor
    
    def handle(self, data):
        handled = self._handle(data)
        if not handled and self._successor:
            self._successor.handle(data)
    
    def _handle(self, data):
        raise NotImplementedError('Debe implementar este método en una subclase.')

class ConcreteHandler1(Handler):
    def _handle(self, data):
        if "proceso1" in data:
            print(f"El proceso 1 ha sido manejado por {self.__class__.__name__}")
            return True

class ConcreteHandler2(Handler):
    def _handle(self, data):
        if "proceso2" in data:
            print(f"El proceso 2 ha sido manejado por {self.__class__.__name__}")
            return True

class ConcreteHandler3(Handler):
    def _handle(self, data):
        if "proceso3" in data:
            print(f"El proceso 3 ha sido manejado por {self.__class__.__name__}")
            return True

class ConcreteHandler4(Handler):
    def _handle(self, data):
        if "proceso4" in data:
            print(f"El proceso 4 ha sido manejado por {self.__class__.__name__}")
            return True

class DefaultHandler(Handler):
    def _handle(self, data):
        if "proceso6" in data:
            print(f"El proceso 6 ha sido manejado por {self.__class__.__name__}")
            return True
        else:
            print(f"Ningún proceso ha sido manejado por {self.__class__.__name__}")
        return True

class Client:
    def __init__(self):
        self.handler = ConcreteHandler1(ConcreteHandler2(ConcreteHandler3(ConcreteHandler4(DefaultHandler()))))

    def delegate(self, data):
        self.handler.handle(data)

# Ejemplo de uso
client = Client()

data5 = "proceso5"
data1 = "proceso1"
data6 = "proceso6"
data4 = "proceso4"
data2 = "proceso2"
data3 = "proceso3"

client.delegate(data1)
client.delegate(data2)
client.delegate(data3)
client.delegate(data4)
client.delegate(data5)
client.delegate(data6)
