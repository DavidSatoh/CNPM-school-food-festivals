from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# The connection string to test.
# This assumes the pymssql driver is installed and the database server is running
# and accessible at the specified address and port.
# Please note: For production, you should handle credentials more securely.
DATABASE_URL = "mssql+pymssql://sa:Aa123456@127.0.0.1:1433/FlaskApiDB"

def verify_db_connection(db_url):
    """
    Attempts to connect to the database and print a success or failure message.
    """
    try:
        # Create a database engine
        engine = create_engine(db_url)
        print("Attempting to connect to the database...")

        # Use the engine to connect to the database
        with engine.connect() as connection:
            # Execute a simple query to verify the connection is active
            result = connection.execute(text("SELECT 1"))
            print("Successfully connected to the database!")
            print(f"Query result: {result.scalar()}")

        print("\nConnection successful. The database is reachable and the credentials are valid.")
        return True

    except SQLAlchemyError as e:
        print(f"Failed to connect to the database. An error occurred:\n{e}")
        # Check for specific error messages to provide more context
        error_str = str(e)
        if "Data source name not found" in error_str:
            print("Troubleshooting Tip: The pyodbc driver for your SQL Server may not be installed or configured correctly.")
            print("Ensure you have the ODBC driver installed and it's compatible with your Python and system architecture (32-bit vs 64-bit).")
        elif "Login failed" in error_str:
            print("Troubleshooting Tip: The username or password in your connection string is incorrect.")
        elif "Cannot open database" in error_str:
            print("Troubleshooting Tip: The database name specified in the connection string does not exist.")
        elif "Could not open a connection to SQL Server" in error_str:
            print("Troubleshooting Tip: The SQL Server is either not running or not accessible at the specified IP address and port.")
            print("Please check the server status, firewall rules, and port forwarding.")
        return False
    finally:
        # Dispose of the engine to release the connection
        if 'engine' in locals():
            engine.dispose()

if __name__ == "__main__":
    verify_db_connection(DATABASE_URL)
