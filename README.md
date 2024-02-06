# Am I The AI
This is a reddit bot that responds to r/aita with an AI-based answer.

## Installation
This package depends on llamacpp python. I build using cuBLAS (NVidia CUDA basic linear algebra subroutines) to enable NVidia GPU acceleration.

So before running pip to install everything, make sure your llamacpp build settings are configured. I use these:

```bash
export CMAKE_ARGS=-DLLAMA_CUBLAS=on
export FORCE_CMAKE=1
export CUDA_HOME=/usr/local/cuda
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64 # Note: the CUPTI/lib64 seems old, not found on my machine but this shouldn't hurt
export PATH=$PATH:$CUDA_HOME/bin
```

If you want to run this and scrape/post to reddit, you need to configure praw.ini

```ini
[DEFAULT]
# A boolean to indicate whether or not to check for package updates.
check_for_updates=True

# Object to kind mappings
comment_kind=t1
message_kind=t4
redditor_kind=t2
submission_kind=t3
subreddit_kind=t5
trophy_kind=t6

# The URL prefix for OAuth-related requests.
oauth_url=https://oauth.reddit.com

# The amount of seconds of ratelimit to sleep for upon encountering a specific type of 429 error.
ratelimit_seconds=5

# The URL prefix for regular requests.
reddit_url=https://www.reddit.com

# The URL prefix for short URLs.
short_url=https://redd.it

# The timeout for requests to Reddit in number of seconds
timeout=16

[am_i_the_ai]
client_id=<your reddit client id>
client_secret=<your reddit client secret>
password=<your reddit password>
username=<your reddit username>
user_agent=script:am_i_the_ai:1.0
```
