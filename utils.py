import datetime as dt

def timestamp_to_datetime(timestamp):
  return dt.datetime.utcfromtimestamp(int(timestamp))
  

def str_to_datetime(date):
  return dt.datetime.strptime(date, '%Y-%m-%d')
