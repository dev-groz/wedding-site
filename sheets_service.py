import os 
import json
from google.oauth2.service_account import Credentials
import gspread


creds_json = os.getenv('GOOGLE_CREDENTIALS_JSON')

if not creds_json:
    raise Exception('GOOGLE_CREDENTIALS_JSON is not found')

creds_dict = json.loads(creds_json)

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)

sheet_url = 'https://docs.google.com/spreadsheets/d/1ZLKs6phWGjEya8rEx1k9CBynmLt9p0MQXlBSyNe__UM/edit'
sheet = client.open_by_url(sheet_url).sheet1


def write_to_sheet(first_name: str, last_name: str, phone: str):
    new_row = [first_name, last_name, phone]
    sheet.append_row(new_row)
