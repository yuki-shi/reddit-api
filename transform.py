import pandas as pd
import datetime as dt
import os.path
from utils import str_to_datetime


def prepare_csv(posts: list, data_limite: str) -> None:
  df = pd.DataFrame(posts, columns=['title',
                                    'author',
                                    'flair',
                                    'ups',
                                    'downs',
                                    'url',
                                    'created',
                                    'text'])


  df['created'] = pd.to_datetime(df['created'])
  df['created'] = df['created'] - dt.timedelta(hours=3) # conversão para UTC -3

  data_limite = str_to_datetime(data_limite)
  last_entry = 0

  for index, date in enumerate(df.iloc[:, 6]):
    if date < data_limite:
      last_entry = index
      break
      
  df = df.iloc[:last_entry, :]
  df.to_csv('reddit_data.csv', index=False)

  print(f'Arquivo salvo em {os.path.abspath("reddit_data.csv")}')

  return
