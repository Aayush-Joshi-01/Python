class PostNotFoundException(Exception):
    pass


class SocialMediaPlatform:
    def __init__(self):
        self.posts = []

    def create_post(self, content):
        self.posts.append(content)
        print("Post created successfully.")

    def view_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            print("Posts:")
            for i, post in enumerate(self.posts, 1):
                print(f"{i}. {post}")

    def delete_post(self, index):
        if index < 1 or index > len(self.posts):
            raise PostNotFoundException("Post does not exist.")
        del self.posts[index - 1]
        print("Post deleted successfully.")


def main():
    social_media = SocialMediaPlatform()

    while True:
        print("\nSocial Media Platform:")
        print("1. Create Post")
        print("2. View Posts")
        print("3. Delete Post")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            content = input("Enter the content of your post: ")
            social_media.create_post(content)
        elif choice == '2':
            social_media.view_posts()
        elif choice == '3':
            try:
                index = int(input("Enter the index of the post to delete: "))
                social_media.delete_post(index)
            except ValueError:
                print("Invalid input. Please enter a valid index.")
            except PostNotFoundException as e:
                print(e)
        elif choice == '4':
            print("Exiting the social media platform. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
