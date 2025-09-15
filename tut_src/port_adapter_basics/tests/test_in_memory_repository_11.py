from domain.objects.author_2 import Author
from domain.objects.content_3 import Content
from domain.objects.comment_1 import Comment
from domain.adapters.in_memory_repository_7 import InMemoryCommentRepository

def test_save_and_get_comment():
    repository = InMemoryCommentRepository()

    author = Author("BWS")
    content = Content("Hexagonal is fire!")
    comment = Comment.create(author, content)

    repository.save(comment)
    result = repository.get_by_id(str(comment.id))

    assert result is not None
    assert result.id == comment.id
    assert result.author.name == "BWS"
    assert result.content.value == "Hexagonal is fire!"
