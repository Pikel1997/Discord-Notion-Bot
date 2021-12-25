import os
import requests

NOTION_KEY = os.getenv('NOTION_KEY')
NOTION_DATABASE_ID = os.environ['NOTION_DATABASE_ID']

def add_req(j):

  headers = {
      'Authorization': f"Bearer {NOTION_KEY}",
      'Content-Type': 'application/json',
      'Notion-Version': '2021-08-16',
  }

  data = '{{"parent": {{ "database_id": "{0}" }}, "properties": {{ "title": {{ "title": [ {{ "text": {{ "content": "{1}" }} }} ] }} }} }}'.format(NOTION_DATABASE_ID, j)

  response = requests.post('https://api.notion.com/v1/pages', headers=headers, data=data)

def ret_req():
  
  url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}"

  payload={}
  headers = {
    'Authorization': f'Bearer {NOTION_KEY}',
    'Notion-Version': '2021-08-16'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  info = response.text
  return info

