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

            response_text = response["choices"][0]["message"]["content"]

            # Submit the response to the post
            if dry_run:
                print(f"Would have replied to {submission.title}: {response_text}")
            else:
                self.reddit.reply_to_submission(submission, response_text)
                print(f"Replied to {submission.title}")


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
