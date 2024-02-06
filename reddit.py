import praw
import pymongo


# Initialize Reddit API with praw
def initialize_reddit_api(client_id, client_secret, user_agent):
    """
    Initialize the Reddit API client with praw.

    Parameters:
    - client_id: Reddit application client ID
    - client_secret: Reddit application client secret
    - user_agent: User agent string for the API access

    Returns:
    - reddit: An instance of the Reddit API client
    """
    reddit = praw.Reddit(
        client_id=client_id, client_secret=client_secret, user_agent=user_agent
    )
    return reddit


# Fetch the submission and its comments
def fetch_submission_comments(reddit, url):
    """
    Fetch a submission and its comments from Reddit.

    Parameters:
    - reddit: The Reddit API client instance
    - url: URL of the Reddit post to fetch

    Returns:
    - submission: The Reddit submission object
    """
    submission = reddit.submission(url=url)
    submission.comments.replace_more(limit=None)  # Expand all comments
    return submission


# Recursively traverse comments
def traverse_comments(comments):
    """
    Recursively traverse and structure comments and replies.

    Parameters:
    - comments: The comment forest or reply list

    Returns:
    - comment_list: A list of dictionaries with comment data and replies
    """
    comment_list = []
    for comment in comments:
        comment_data = {
            "commentId": comment.id,
            "comment": comment.body,
            "replies": traverse_comments(comment.replies) if comment.replies else [],
        }
        comment_list.append(comment_data)
    return comment_list


# Connect to MongoDB and return the collection
def connect_to_mongodb(db_name, collection_name):
    """
    Connect to MongoDB and return the specified collection.

    Parameters:
    - db_name: Name of the database
    - collection_name: Name of the collection

    Returns:
    - collection: The MongoDB collection object
    """
    client = pymongo.MongoClient()
    db = client[db_name]
    collection = db[collection_name]
    collection.drop()  # Clear existing collection
    return collection


# Main function to encapsulate the logic
def main():
    # Reddit API credentials and post URL
    CLIENT_ID = "YOUR_CLIENT_ID"
    CLIENT_SECRET = "YOUR_CLIENT_SECRET"
    USER_AGENT = "YOUR_USER_AGENT"
    POST_URL = "https://www.reddit.com/r/Layoffs/comments/12spouo/nordstrom_layed_off_2025_it_workforce_without/"

    # Initialize Reddit API
    reddit = initialize_reddit_api(CLIENT_ID, CLIENT_SECRET, USER_AGENT)

    # Fetch submission and comments
    submission = fetch_submission_comments(reddit, POST_URL)

    # Traverse and structure comments
    comments_data = {
        "commentId": submission.id,
        "replies": traverse_comments(submission.comments),
    }

    # Connect to MongoDB and get the collection
    comments_collection = connect_to_mongodb("Reddit", "Comments")

    # Store comments in MongoDB
    comments_collection.insert_one(comments_data)

    print("Comments have been stored in MongoDB.")


# Execute the main function
if __name__ == "__main__":
    main()
