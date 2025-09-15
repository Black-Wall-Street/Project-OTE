from abc import ABC, abstractmethod
from domain.objects.comment_1 import Comment

class CommentRepositoryPort(ABC):
    @abstractmethod
    def save(self, comment: Comment) -> None:
        pass
