"""Conftest.py with base shared fixtures for py-sdd-starter-kit.

Fixtures:
- domain_fake_user: Fake implementation of a User port for domain testing
- app_dto_user: DTO example for application layer testing
- client: Test client configuration
"""
from typing import Dict, Any


# Fixtures de doubles en memoria para puertos de domain/
class FakeUserRepository:
    """Fake implementation of a User repository port for testing."""
    
    def __init__(self) -> None:
        self._storage: Dict[str, Any] = {}
    
    async def get_by_id(self, user_id: str) -> Any:
        return self._storage.get(user_id)
    
    async def save(self, entity: Any) -> None:
        self._storage[entity.user_id if hasattr(entity, 'user_id') else str(entity)] = entity
    
    async def delete(self, user_id: str) -> None:
        self._storage.pop(user_id, None)


# Fixture para pytest
def domain_fake_user_repository() -> FakeUserRepository:
    """Provide a fake User repository for domain layer tests."""
    return FakeUserRepository()


# DTO example for application layer testing
class UserDTO:
    """Data Transfer Object for User in application layer."""
    
    def __init__(self, user_id: str, name: str, email: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email


def app_dto_user(sample_user_dict: Dict[str, str] | None = None) -> UserDTO:
    """Create a UserDTO for application layer tests."""
    if sample_user_dict is None:
        sample_user_dict = {"user_id": "test-001", "name": "Test User", "email": "test@example.com"}
    return UserDTO(
        user_id=sample_user_dict["user_id"],
        name=sample_user_dict["name"],
        email=sample_user_dict["email"],
    )