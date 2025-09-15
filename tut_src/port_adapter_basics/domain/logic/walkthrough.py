from ..services.create_comment_service_4 import CreateCommentService
from ..adapters.in_memory_repository_7 import InMemoryCommentRepository
from ..objects.author_2 import Author
from ..objects.content_3 import Content
from ..ports.comment_repository_port_13 import CommentRepositoryPort
from ..objects.comment_1 import Comment
import time

def print_step(title, data=None):
    print(f"\n🔹 {title}")
    if data is not None:
        print(f"   ↳ {data}")

def main():
    print("🧪 Hexagonal Architecture Walkthrough")
    
    # === PRIMARY ADAPTER ===
    print_step("1. Primary Adapter receives input")
    author_input = input("👤 Enter author name: ").strip()
    content_input = input("💬 Enter comment text: ").strip()

    time.sleep(3)

    # === SETUP ===
    repository: CommentRepositoryPort = InMemoryCommentRepository()
    service = CreateCommentService(repository)

    # === INBOUND PORT ===
    print_step("2. Inbound Port (Service) validates and creates domain objects")
    author = Author(author_input)
    print_step("   - Author object created", author)

    content = Content(content_input)
    print_step("   - Content object created", content)

    time.sleep(3)

    # === DOMAIN ENTITY ===
    comment = Comment.create(author, content)
    print_step("3. Domain Entity (Comment) constructed", {
        "id": comment.id,
        "author": str(comment.author),
        "content": str(comment.content),
        "created_at": comment.created_at
    })

    time.sleep(3)

    # === OUTBOUND PORT ===
    print_step("4. Outbound Port called (CommentRepositoryPort.save)")
    service._repository.save(comment)

    time.sleep(3)

    # === OUTBOUND ADAPTER ===
    print_step("5. Outbound Adapter (InMemoryRepository) handles persistence")
    print_step("   - Repository state", repository._store)

    print("\n✅ End of walkthrough.")

if __name__ == "__main__":
    main()
