from domain.objects.comment_1 import Comment
from domain.ports.comment_repository_port_13 import CommentRepositoryPort

class InMemoryCommentRepository(CommentRepositoryPort):
    def __init__(self):
        self._store = {}

    def save(self, comment: Comment) -> None:
        self._store[str(comment.id)] = comment
        print(f"[Repository] Saved comment: {comment.id}")

    def get_by_id(self, comment_id: str) -> Comment | None:
        return self._store.get(comment_id)
