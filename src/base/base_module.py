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
    def build(self) -> None:
        """Build the module."""
        pass
