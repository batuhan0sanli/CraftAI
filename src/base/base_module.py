from abc import ABC, abstractmethod, abstractproperty

from .base_schema import BaseSchema  # noqa: F401
from src.variables import Variables


class BaseModule(ABC):
    """Abstract base class for all modules."""

    schema: BaseSchema

    def __init__(self, data: dict, variables: Variables):
        self.data = self.schema().load(data)
        self.variables = variables

    @abstractmethod
    def build_method(self) -> None:
        """Build the module."""
        pass

    def build(self) -> None:
        """Build the module."""
        response = self.build_method()
        if 'var' in self.data:
            if response:
                self.variables.set(self.data['var'], response)
            else:
                self.variables.set(self.data['var'], '')
