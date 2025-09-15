from domain.objects.author_2 import Author, InvalidAuthorError
from domain.objects.content_3 import Content, InvalidContentError
from domain.objects.comment_1 import Comment
from domain.ports import CommentRepositoryPort

class CreateCommentService:
    def __init__(self, repository: CommentRepositoryPort):
        self._repository = repository

    def execute(self, author_name: str, comment_text: str) -> Comment:
        try:
            author = Author(author_name)
            content = Content(comment_text)
        except (InvalidAuthorError, InvalidContentError) as e:
            raise ValueError(f"Invalid input: {e}")

        comment = Comment.create(author, content)
        self._repository.save(comment)
        return comment
