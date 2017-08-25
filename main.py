import mysql.connector

conn = mysql.connector.connect(user='test_user', password='password',
                               host='127.0.0.1',
                               database='test_db')

conn.close()

# OK, so that's it - line 1 imports the necessary library, line 3 defines the connection object and connects and line 7
# closes said connection. Now whilst this may not look impressive from the command line, you have actually created a
# mysql object and used to both connect to a database and then disconnect from it.
# You can do it in a slightly different and, some may say, clearer way like so:

from mysql.connector import connection

conn = connection.MySQLConnection(user='test_user', password='password',
                                  host='127.0.0.1',
                                  database='test_db')

conn.close()

# But I hear you say, "what if something goes wrong and why can't I see what's happening?", well you are quite right,
# not providing the user with some sort of feedback is a cardinal sin as is not preparing for possible errrors, so:

# import mysql.connector  // already done, so can be ignored here
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(user='dud_user', password='not_right',
                                   host='127.0.0.1',
                                   database='non_existent')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The named database does not exist")
    else:
        print(err)
else:
    print("We connected to the database. Connection is now closing.")
    conn.close()

# The biggest problem here, as you may have figured out, is the details are hard-coded so readable by anyone with enough
# savvy to open the .py file in a text editor. Move on to lesson two to discover how to prevent this issue.
    
