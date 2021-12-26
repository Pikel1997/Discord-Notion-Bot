import os
import requests
import json
from jsonpath_ng import parse

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

  url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"

  payload={}
  headers = {
    'Authorization': f"Bearer {NOTION_KEY}",
    'Notion-Version': '2021-08-16'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  json_data = json.loads(response.text)

  query = parse('results[*].properties.Name.title[0].plain_text')

  emp_l=[]

  for match in query.find(json_data):
    emp_l.append(match.value)
  if len(emp_l) == 0:
    return "Table is empty"
  else:
    return emp_l

# def trun():
  
