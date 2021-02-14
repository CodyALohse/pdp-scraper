from __future__ import print_function
import os
from typing import List
from googleapiclient.discovery import build
from google.oauth2 import service_account

flatten = lambda t: [item for sublist in t for item in sublist]

class GSheets:
    googleServiceAcctFile = os.environ["GOOGLE_SERVICE_ACCT_FILE"]
    googleSheetId = os.environ["GOOGLE_SHEET_ID"]

    currDir = os.path.dirname(os.path.realpath(__file__))
    serviceCredsFilePath = os.path.join(currDir, googleServiceAcctFile)

    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    creds = service_account.Credentials.from_service_account_file(serviceCredsFilePath, scopes=scopes)

    def __init__(self):
        self.service = build('sheets', 'v4', credentials=self.creds, cache_discovery=False)

    def getRange(self, range: str, skipFirst: bool) -> List[str]:
        # Call the Sheets API
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.googleSheetId,
                                    range=range).execute()

        values = result.get('values', [])

        if not values:
            return []
        else:
           return flatten(values)