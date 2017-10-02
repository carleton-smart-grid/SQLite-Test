1.	Install SQLite3. Use command: "sudo apt-get install sqlite3"

2.	Run SQLite3 with setup command using: "sqlite3 mydatabase.db < setup.txt"
	Note that setup.txt creates a tables for usages called "usages".
	Running with setup also drops any table called usages, ensuring a clean start.
	The usages table is setup as:

	date | time | house_ id | usage 
	-------------------------------
	     |      |           |

3.	Run command: "python3 xml_to_db.py mydatabase.db house.xml 60".
	(Note that the last argument is the frequency that the program checks the XML file for changes in seconds)
	
