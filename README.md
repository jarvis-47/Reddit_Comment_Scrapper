# Reddit Comments Scrapper

## Overview
The Reddit Comments Scrapper is a Python script designed to extract comments from a specified Reddit post and store them in a MongoDB database. Utilizing the `praw` (Python Reddit API Wrapper) library for fetching data from Reddit and `pymongo` for interacting with MongoDB, this script is ideal for data analysis, sentiment analysis, or archiving discussions.

## Features
- Fetch a Reddit post and all associated comments, including nested replies.
- Recursively traverse through comment threads.
- Store comments in a structured format in MongoDB for easy retrieval and analysis.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher installed
- A MongoDB server running locally or accessible remotely
- Reddit API credentials (client ID, client secret, and a user agent string)

## Installation
1. **Clone the repository:**
2. **Install dependencies:** "pip install praw pymongo"
3. **Configuration:**
   - Open the script in your favorite text editor.
   - Replace `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, and `YOUR_USER_AGENT` with your Reddit API credentials.
   - Update the `POST_URL` variable with the URL of the Reddit post you wish to fetch comments from.

## Usage
To run the script, navigate to the script's directory in your terminal and execute:
"python reddit_comments_fetcher.py"

Upon successful execution, the script will fetch comments from the specified Reddit post and store them in the `Comments` collection within the `Reddit` database in MongoDB.

## Contributing
Contributions to the Reddit Comments Fetcher are welcome!

1. Fork the project.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.
