import logging
import argparse
import sys
import psycopg2

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect("dbname='snippets' user='Jenny' host='localhost'")
logging.debug("Database connection established.")


def put(name, snippet):

    # python snippets.py put list "A sequence of things - created using []"
    """Store a snippet with an associated name."""
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    cursor.execute(command, (name, snippet))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet


def get(name):

    """Retrieve the snippet with a given name.
    If there is no such snippet...ask user to implement a snippet
    """
    cursor = connection.cursor()
    cursor.execute("select message from snippets where keyword=%s", (name,))
    row = cursor.fetchone()
    connection.commit()
    return row


def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")

    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="Name of snippet")

    arguments = parser.parse_args(sys.argv[1:])
    print arguments

    arguments = vars(arguments)
    print arguments

    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
    elif command == "get":
        snippet = get(**arguments)
        print snippet

if __name__ == "__main__":
    main()
