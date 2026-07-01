from abc import ABC, abstractmethod
from models.user import LoginRequest

class AuthStrategy(ABC):

    @abstractmethod
    def authenticate(self, data: LoginRequest):
        pass