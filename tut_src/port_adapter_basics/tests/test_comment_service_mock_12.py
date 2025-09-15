import pytest
from unittest.mock import Mock

from domain.services.create_comment_service_4 import CreateCommentService
from domain.objects.comment_1 import Comment
from domain.ports.comment_repository_port_13 import CommentRepositoryPort

def test_create_comment_calls_repository_save():
    mock_repo = Mock(spec=CommentRepositoryPort)
    service = CreateCommentService(mock_repo)

    comment = service.execute("Mocky", "This is a mock test")

    # Assert repository.save was called once
    mock_repo.save.assert_called_once()
    
    # Assert that the saved comment is the one returned
    saved_comment = mock_repo.save.call_args[0][0]
    assert isinstance(saved_comment, Comment)
    assert comment.id == saved_comment.id
