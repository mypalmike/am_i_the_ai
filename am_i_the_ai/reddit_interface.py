
import praw

DEFAULT_BOT_NAME = "am_i_the_ai"
DEFAULT_SUBREDDIT = "AmITheAsshole"

class Reddit:
    def __init__(self, bot_name=DEFAULT_BOT_NAME):
        self.reddit = praw.Reddit(bot_name)
        self.replied_comments = set()
        self._query_replied_comments()
    
    def query_interesting_submissions(self, subreddit=DEFAULT_SUBREDDIT, limit=50):
        submissions = self.reddit.subreddit(subreddit).new(limit=limit)
        return [submission for submission in submissions if self._filter_submission(submission)]

    def _query_replied_comments(self):
        # Collect all the recent comments we have replied to
        for comment in self.reddit.user.me().comments.new(limit=50):
            self.replied_comments.add(comment.submission.id)

    def _filter_submission(self, submission):
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
    
    def reply_to_submission(self, submission, comment):
        # Submit the comment to reddit as a reply to the submission
        submission.reply(comment)
        self.replied_comments.add(submission.id)
