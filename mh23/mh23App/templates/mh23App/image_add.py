# Import the required library
import psycopg2
  
# Method to create a connection object
# It creates a pointer cursor to the database 
# and returns it along with Connection object
def create_connection():
    # Connect to the database
    # using the psycopg2 adapter.
    # Pass your database name ,# username , password , 
    # hostname and port number
    conn = psycopg2.connect(dbname='MH23',
                            user='postgres',
                            password='asdf',
                            host='localhost',
                            port='5432')
    # Get the cursor object from the connection object
    curr = conn.cursor()
    return conn, curr
  
def create_table():
    try:
        # Get the cursor object from the connection object
        conn, curr = create_connection()
        try:
            # Fire the CREATE query
            curr.execute("CREATE TABLE IF NOT EXISTS \
            cartoon(cartoonID INTEGER, name TEXT,\
            cartoonImg BYTEA)")
              
        except(Exception, psycopg2.Error) as error:
            # Print exception
            print("Error while creating cartoon table", error)
        finally:
            # Close the connection object
            conn.commit()
            conn.close()
    finally:
        # Since we do not have to do anything here we will pass
        pass
  
def write_blob(cartoonID,file_path,name):
    try:
        # Read data from a image file
        drawing = open(file_path, 'rb').read()
        # Read database configuration
        conn, cursor = create_connection()
        try:           
            # Execute the INSERT statement
            # Convert the image data to Binary
            cursor.execute("INSERT INTO cartoon\
            (cartoonID,name,cartoonImg) " +
                    "VALUES(%s,%s,%s)",
                    (cartoonID,name, psycopg2.Binary(drawing)))
            # Commit the changes to the database
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while inserting data in cartoon table", error)
        finally:
            # Close the connection object
            conn.close()
    finally:
        # Since we do not have to do
        # anything here we will pass
        pass
        
# Call the create table method      
create_table()
# Prepare sample data, of images, from local drive
write_blob(1,"C:\\Users\\johnn_j6r\\Dropbox\\My PC (DESKTOP-6ES92QP)\\Downloads\\download.jpg","r34")