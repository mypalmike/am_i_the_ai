import argparse
import praw
from datetime import datetime as dt
from openai import OpenAI

# openai.api_base = "http://localhost:4891/v1"
# openai.api_key = "not needed for a local LLM"

MODEL = "Mistral Instruct" #  "mistral-7b-openorca.Q4_0.gguf"

class RedditBot:
    def __init__(self, bot_name):
        self.reddit = praw.Reddit(bot_name)
        self.replied_comments = set()

    def filter_submission(self, submission):
        # Check if we have already replied to this post
        if submission.id in self.replied_comments:
            return False
        # Check if the post has at least 10 comments
        if submission.num_comments < 10:
            return False
        # Check if the post has at least 50 upvotes
        if submission.score < 20:
            return False
        # Check if the post is text only
        if not submission.is_self:
            return False
        # Check if the post is not locked
        if submission.locked:
            return False
        return True
    
    def query_replied_comments(self):
        # Collect all the recent comments we have replied to
        for comment in self.reddit.user.me().comments.new(limit=50):
            self.replied_comments.add(comment.submission.id)

    def reply_to_submission(self, submission):
        # Submit the selftext of the submission to the gpt4all API
        prompt = f"""
        Am I the asshole? Wihtout using the word "asshole" in the response, please respond with YTA, NTA, or ESH,
        followed by a brief explanation of why. {submission.selftext}
        """
        prompt = "Who is Michael Jordan?"

        client = OpenAI(
            api_key= "Don't need for local", # "sk-4c2gH8XjJfj6VXQfZtKJ3K1Wf8Uq3gYvGKQ3zQ9jZQe5x3",
            base_url="http://localhost:4891/v1"
        )
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model=MODEL,
            temperature=0.7,
            max_tokens=150,
            stop=None,

            # prompt=prompt,
            # max_tokens=50,
            # temperature=0.28,
            # top_p=0.95,
            # n=1,
            # echo=True,
            # stream=False
        )

        # request_obj = {
        #     'model': MODEL,
        #     'prompt': prompt,
        #     'max_tokens': 50,
        #     'temperature': 0.28,
        #     'top_p': 0.95,
        #     'n': 1,
        #     'echo': True,
        #     'stream': False,
        #     'api_key': '',
        # }

        # response = requests.post('http://localhost:4891/v1', json=request_obj)
        
        print (response)

        # # Reply to the submission
        # submission.reply(reply_text)

        # # Add the submission to the set of replied comments
        # self.replied_comments.add(submission.id)

    def run(self):
        self.query_replied_comments()

        # Get the newest 50 posts from r/AmITheAsshole
        for submission in self.reddit.subreddit('AmITheAsshole').new(limit=50):
            time = dt.fromtimestamp(submission.created_utc)
            print (f"Post: {submission.title} | Time: {time}")
            if not self.filter_submission(submission):
                continue
            self.reply_to_submission(submission)



def main():
    bot = RedditBot('am_i_the_ai')
    bot.run()

if __name__ == "__main__":
    main()
