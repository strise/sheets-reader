from __future__ import print_function

from googleapiclient.discovery import build

# The ID and range of a sample spreadsheet.
sheets_id = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
sheets_data_range = 'Class Data'


def main():
  service = build('sheets', 'v4')

  # Call the Sheets API
  sheet = service.spreadsheets()
  result = sheet.values().get(spreadsheetId=sheets_id, range=sheets_data_range).execute()
  values = result.get('values', [])

  if not values:
    print('No data found.')
  else:
    for row in values:
      # Print columns A and E, which correspond to indices 0 and 4.
      print('%s, %s' % (row[0], row[4]))


if __name__ == '__main__':
  main()
