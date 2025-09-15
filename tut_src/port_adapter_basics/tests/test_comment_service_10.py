from domain.services.create_comment_service_4 import CreateCommentService
from domain.adapters.in_memory_repository_7 import InMemoryCommentRepository

def test_create_comment_success():
    repository = InMemoryCommentRepository()
    service = CreateCommentService(repository)

    author = "Onyx"
    content = "This is a test comment."
    comment = service.execute(author, content)

    # Ensure the comment was returned properly
    assert comment.author.name == author
    assert comment.content.value == content
    assert comment.id is not None

    # Ensure it was saved in the repository
    stored = repository.get_by_id(str(comment.id))
    assert stored is not None
    assert stored.id == comment.id
