import os

import httplib2

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def get_service_sacc():
    creds_json = os.path.dirname(__file__) + "/sacc.json"
    print(creds_json)
    scopes = 'https://www.googleapis.com/auth/spreadsheets'

    service_creds = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=service_creds)


def get_algebra_sheet():
    return sheet.values().get(spreadsheetId=sheet_algebra_id, range="ЖУРНАЛ").execute()


def get_geometry_sheet():
    return sheet.values().get(spreadsheetId=sheet_geometry_id, range="ЖУРНАЛ").execute()


def get_specmat_sheet():
    return sheet.values().get(spreadsheetId=sheet_specmat_id, range="ЖУРНАЛ").execute()


sheet_algebra_id = '1xqwFt48PaPnpS_yVSYwkBvQHRtxngyjxoD5AKVfDJgg'
sheet_geometry_id = '1o9dkLTrvBSKEOB0ScHGizfPZID4ive0RPewmZ_uVpEg'
sheet_specmat_id = '1spPzKnzeTUSD80S23JdtiM3ojnytGA1VAxiU1z8xras'

service = get_service_sacc()
sheet = service.spreadsheets()




