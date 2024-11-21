import os
import requests

from dotenv import load_dotenv
# Load environment variables when the module is imported
load_dotenv()


def authenticate():
    """
    Authenticates the user using the Reddit API.

    This assumes you have a .env file with the following variables:
    - REDDIT_CLIENT_ID
    - REDDIT_CLIENT_SECRET
    - REDDIT_USERNAME
    - REDDIT_PASSWORD

    Returns:
        str: The access token for the authenticated user.
    """
    
    # Use my client ID and client secret to authenticate
    client_auth = requests.auth.HTTPBasicAuth(os.getenv("REDDIT_CLIENT_ID"), os.getenv("REDDIT_CLIENT_SECRET"))

    # Reddit API also requires that I pass my username and password
    post_data = {"grant_type": "password", 
                 "username": os.getenv('REDDIT_USERNAME'), 
                 "password": os.getenv('REDDIT_PASSWORD')}

    # Reddit API also requires that I identify myself in the User-Agent header
    headers = {"User-Agent": f"LSE DS105A (2024/25) API practice by {os.getenv('REDDIT_USERNAME')}"}

    # From their documentation, I learned this is the endpoint I need
    ACCESS_TOKEN_ENDPOINT = "https://www.reddit.com/api/v1/access_token"

    # Send a HTTP POST request to the Reddit API to authenticate
    response = requests.post(ACCESS_TOKEN_ENDPOINT, auth=client_auth, data=post_data, headers=headers)
    token = response.json()['access_token']

    # Return the token
    return token

def get_next_top100_posts(subreddit, token, after=None):
    """
    Retrieves the next 100 top posts from a specified subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit to retrieve posts from.
        token (str): The access token required for authentication.
        after (str, optional): The ID of the post to start retrieving from. Defaults to None.

    Returns:
        tuple: A tuple containing the list of posts and the ID of the last post retrieved.

    """
    headers = {"Authorization": f"bearer {token}", 
               "User-Agent": f"LSE DS105A (2024/25) API practice by {os.getenv('REDDIT_USERNAME')}"}
    
    params = {"t": "year", "limit": 100}

    if after:
        params['after'] = after
    
    response = requests.get(f"https://oauth.reddit.com/r/{subreddit}/top", headers=headers, params=params)

    json_response = response.json()

    # Let's be smart about this
    # Let's return the 'children' key of the 'data' key of the response
    # and the 'after' key of the 'data' key of the response
    return json_response['data']['children'], json_response['data']['after']

def get_n_pages_of_top_posts(subreddit, token, n):
    """
    Retrieves the next n*100 top posts from a specified subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit to retrieve posts from.
        token (str): The access token required for authentication.
        n (int): The number of pages to retrieve.

    Returns:
        list: A list of the top posts from the subreddit.
    """
    posts = []
    after = None

    # We need a normal for loop for this, list comprehensions won't work
    for _ in range(n):
        new_posts, after = get_next_top100_posts(subreddit, token, after)
        posts.extend(new_posts)

    return posts