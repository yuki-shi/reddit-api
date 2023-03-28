from reddit_api import Reddit
from transform import prepare_csv


def main():
  data_limite = '2023-03-20' # em formato #%Y-%m-%d
  subreddit = 'r/cats'

  reddit = Reddit()
  posts = reddit.get_posts_data(data_limite, subreddit)
  prepare_csv(posts, data_limite)

  return


if __name__ == '__main__':
  main()