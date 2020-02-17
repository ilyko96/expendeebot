from db import ExpendeeDB
import shlex

class ExpendeeApp(object):
	def __init__(self, filename='expendee.db'):
		self.db = ExpendeeDB(filename)

	def runCommand(self, command):
		''' takes string command and applies it. returns (err_code, data) '''
		argv = shlex.split(command)
		if len(argv) == 0: return (-1, None)
		cmd = argv.pop(0).lower()
		def switchCmd(arg, argv):
			return {
				'add': self.add(argv),
				'edit': self.edit(argv),
				'del': self.delete(argv),
				'ls': self.list(argv)
			}.get(arg, (-2, None))
		return switchCmd(cmd, argv)

	def add(self, argv):
		return (0, 'add: '.format(argv))
	def edit(self, argv):
		return (0, 'edit: '.format(argv))
	def delete(self, argv):
		return (0, 'delete: '.format(argv))
	def list(self, argv):
		return (0, 'list: '.format(argv))