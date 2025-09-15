from abc import ABC, abstractmethod
from domain.objects.comment_1 import Comment

class CommentRepositoryPort(ABC):
    @abstractmethod
    def save(self, comment: Comment) -> None:
        """Save a comment to a storage backend."""
        pass

    @abstractmethod
    def get_by_id(self, comment_id: str) -> Comment | None:
        """Retrieve a comment by its ID."""
        pass
