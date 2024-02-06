import argparse
from datetime import datetime as dt

from llm_interface import Llm
from reddit_interface import Reddit

class RedditBot:
    def __init__(self, reddit, llm):
        self.reddit = reddit
        self.llm = llm

    def run(self, dry_run=False):
        # Get the newest 50 posts from r/AmITheAsshole
        for submission in self.reddit.query_interesting_submissions():
            # Combine the title and the body of the post
            prompt = f"{submission.title}\n\n{submission.selftext}"
            # Get a response from the model
            response = self.llm.respond(prompt)
            # response = {'id': 'chatcmpl-cf54b536-a9f9-4da5-9a04-bc5ef70e20bd', 'object': 'chat.completion', 'created': 1707208978, 'model': '/home/mwhite/aimodels/mistral-7b-instruct-v0.2.Q5_K_M.gguf', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': "\nNTA - While it is true that it may not be your business what your boyfriend buys, the financial implications of his decision have an impact on your shared living situation and future expenses. It's important to have open communication and mutual understanding regarding financial commitments, especially when they involve shared responsibilities and potential financial burdens.\n"}, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 779, 'completion_tokens': 77, 'total_tokens': 856}}

            response_text = response["choices"][0]["message"]["content"]

            # Submit the response to the post
            if dry_run:
                print(f"Would have replied to {submission.title}: {response_text}")
            else:
                self.reddit.reply_to_submission(submission, response_text)
                import sys
                sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Run the Reddit bot")
    parser.add_argument("--dry-run", action="store_true", help="Print the responses instead of submitting them")
    args = parser.parse_args()

    reddit = Reddit()
    llm = Llm()
    bot = RedditBot(reddit, llm)

    bot.run(args.dry_run)


if __name__ == "__main__":
    main()
