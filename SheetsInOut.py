import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import gspread_dataframe as gd
import pandas as pd

from Resources.CredentialData import SheetsData

class SheetsImport():
	"""Import Class - from Google Sheets to tickets_list"""

	scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('SheetsAPIkey.json', scope)
	client = gspread.authorize(creds)

	def __init__(self):
		self.sheet = self.client.open(SheetsData.SHEET_NAME).get_worksheet(1)

	def importData(self):
		"""Import all tickets numbers from Google Sheets"""

		tickets = self.sheet.get_all_values()
		tickets_list = []


		for i in tickets:
			tickets_list.append(int(i[0]))

		print(tickets_list)
		print("")
		return (tickets_list)

	def cleanSheet(self):
		"""Delete all rows which are done"""
		x = 1
		for i in range(0, len(data['ticket_number'].tolist())):
			if not data.loc[data['ticket_number'] == int(data['ticket_number'].tolist()[i]), 'shipment_date'].empty:
				x += 1
			else:
				self.sheet.delete_row(x)


class SheetsExport():
	"""Export Class - from to Google Sheets"""

	scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('SheetsAPIkey.json', scope)
	client = gspread.authorize(creds)

	def __init__(self):
		self.sheet = self.client.open(SheetsData.SHEET_NAME).get_worksheet(2)

	def exportDataFrame(self, df):
		"""Update sheet with new tickets"""
		print("")
		print(df)
		existing = gd.get_as_dataframe(self.sheet)
		updated = existing.append(df)
		gd.set_with_dataframe(self.sheet, updated)

		global data
		data = df

		updated.to_csv('export_dataframe.csv', index = False, header=True)

		return None




