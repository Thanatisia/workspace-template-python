"""
Description of project here

GitHub URL: https://github.com/author/project-name-here
"""

# Import Internal Libraries
import os
import sys

# Import External Libraries


# Import self-defined user libraries
import modules.settings as settings
from modules.settings import app, database


def init():
	"""
	Class Initialization
	"""
	PROJ_INFO = app.init("project-title", "project-version", "repo-url")
	DB_INFO = database.init("database-name", "database-version", "database-username", "database-password")
	
	print(PROJ_INFO)
	print(DB_INFO)
	
def main():
	"""
	Main Program
	"""
	print("Hello World")	

if __name__ == "__main__":
	init()
	main()