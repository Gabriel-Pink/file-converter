from abc import ABC, abstractmethod

class FileConverter(ABC):
    @abstractmethod
    def convert(self, input_file: str, output_file: str):
        pass
