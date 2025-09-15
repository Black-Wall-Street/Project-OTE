from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

from domain.objects.author_2 import Author
from domain.objects.content_3 import Content

@dataclass
class Comment:
    id: UUID
    author: Author
    content: Content
    created_at: datetime

    @staticmethod
    def create(author: Author, content: Content) -> "Comment":
        return Comment(
            id=uuid4(),
            author=author,
            content=content,
            created_at=datetime.utcnow()
        )
