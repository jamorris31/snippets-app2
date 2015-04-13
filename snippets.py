import logging
import argparse
import sys

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)


def put(name, snippet):

    #python snippets.py put list "A sequence of things - created using []"
    """
    Store a snippet with an associated name.

    Returns the name and the snippet
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet

  
def get(name):
    if len(name) == 0:
        logging.error("name of snippet is empty")
    """Retrieve the snippet with a given name.

    If there is no such snippet...ask user to implement a snippet

    Returns the snippet.
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""

  
def main():
    """Main function"""
    # arguments.name = name
    # arguments.snippet = snippet

    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")

    parser.add_argument("-t", "--type", type=str,
                        help="specify get or push operation")

    parser.parse_args()

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.parse_args()

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")

    arguments = parser.parse_args(sys.argv[1:])

    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: {!r}".format(snippet))


if __name__ == "__main__":
    main()