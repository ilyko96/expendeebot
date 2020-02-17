import sqlite3
import datetime as dt

class ExpendeeDB(object):
	def __init__(self, filename="expendee.db"):
		self.filename = filename
		db = sqlite3.connect(self.filename)
		c = db.cursor()
		c.execute(
		"CREATE TABLE IF NOT EXISTS records ("
			"uid INTEGER	PRIMARY KEY, "
			"amount   		REAL, "
			"timestamp		INTEGER, "
			"description	TEXT)")
		db.commit()
		c.close()

	def add_record(self, amount=0, timestamp=dt.datetime.now(), description=''):
		db = sqlite3.connect(self.filename)
		c = db.cursor()
		c.execute('INSERT INTO records(amount, timestamp, description) \
					VALUES(?,?,?)', (amount, timestamp, description))
		db.commit()
		c.close()

	def update_record(self, uid, amount=0, timestamp=dt.datetime.now(), description=''):
		db = sqlite3.connect(self.filename)
		c = db.cursor()
		c.execute('UPDATE records set amount=?, timestamp=?, description=? \
					WHERE uid=?', (amount, timestamp, description, uid))
		db.commit()
		c.close()

	def delete_record(self, uid):
		db = sqlite3.connect(self.filename)
		c = db.cursor()
		c.execute('DELETE FROM records where uid=?', (uid,))
		db.commit()
		c.close()

	def list_all_records(self, ):
		db = sqlite3.connect(self.filename)
		c = db.cursor()
		c.execute('SELECT * from records')
		records = c.fetchall()
		c.close()
		return records

	def get_record(self, uid):
		db = sqlite3.connect(self.filename)
		c = db.cursor()
		c.execute('SELECT * from records WHERE uid=?', (uid,))
		records = c.fetchall()
		c.close()
		return records[0]