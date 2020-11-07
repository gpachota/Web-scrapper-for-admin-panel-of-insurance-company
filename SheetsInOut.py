import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

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
		return (tickets_list)

	def cleanSheet(self, tickets_list):
		"""Delete all rows which are done"""

		x = 1
		for i in range(0, len(tickets_list)):
			if not tickets_list[i][0][7]:
				x += 1
			else:
				self.sheet.delete_row(x)
				
	def deleteRow(self, ticket):
		
		rows = self.sheet.get_all_values()
		x = 1

		for i in rows:
			print(i)
			if i == ticket[0]:
				self.sheet.delete_row(x)
				print(ticket + " deleted")
			else:
				x += 1


class SheetsExport():
	"""Export Class - from to Google Sheets"""

	scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('SheetsAPIkey.json', scope)
	client = gspread.authorize(creds)

	def __init__(self):
		self.sheet = self.client.open(SheetsData.SHEET_NAME).get_worksheet(2)

	def exportAllData(self, tickets_list):
		"""Export all tickets"""

		next_row = len(self.sheet.get_all_values())
		for i in range(0, len(tickets_list)):
			row = []
			for y in range(11):
				row.append(tickets_list[i][0][y])
			print(row)
			self.sheet.update('A' + str(i + 1 + next_row) + ':K' +
						str(i + 1 + next_row), tickets_list[i])
		return tickets_list

	def exportSingleData(self, ticket):
		"""Export single ticket - in progress"""

		next_row = len(self.sheet.get_all_values())
		ticket.append([])

		# self.sheet.update('A' + str(1 + next_row) + ':K' + str(1 + next_row), row)

		# Need to change that for something easier.

		self.sheet.update('A' + str(1 + next_row), ticket[0])
		self.sheet.update('B' + str(1 + next_row), ticket[1])
		self.sheet.update('C' + str(1 + next_row), ticket[2])
		self.sheet.update('D' + str(1 + next_row), ticket[3])
		self.sheet.update('E' + str(1 + next_row), ticket[4])
		self.sheet.update('F' + str(1 + next_row), ticket[5])
		self.sheet.update('G' + str(1 + next_row), ticket[6])
		self.sheet.update('H' + str(1 + next_row), ticket[7])
		self.sheet.update('I' + str(1 + next_row), ticket[8])
		self.sheet.update('J' + str(1 + next_row), ticket[9])
		self.sheet.update('K' + str(1 + next_row), ticket[10])

		return None




