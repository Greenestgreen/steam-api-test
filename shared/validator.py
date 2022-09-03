from abc import ABC,abstractmethod


class Validator(ABC):
    
    @abstractmethod
    def invoke(self, events) -> str:
        pass
