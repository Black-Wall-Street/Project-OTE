from domain.services.create_comment_service_4 import CreateCommentService
from domain.adapters.in_memory_repository_7 import InMemoryCommentRepository

def main():
    print("🗨️  Create a Comment")
    author = input("Enter author name: ").strip()
    content = input("Enter comment text: ").strip()

    repository = InMemoryCommentRepository()
    service = CreateCommentService(repository)

    try:
        comment = service.execute(author, content)
        print("\nComment created successfully!")
        print(f"ID: {comment.id}")
        print(f"Author: {comment.author}")
        print(f"Content: {comment.content}")
        print(f"Created at: {comment.created_at}")

        # Optional: demo retrieval
        print("\nRetrieving comment from repository...")
        fetched = repository.get_by_id(str(comment.id))
        print(f"Retrieved: {fetched.content} by {fetched.author}")

    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
