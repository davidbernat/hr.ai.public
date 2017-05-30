
#
# HR.ai interview problem class for loading text files into database-like dictionaries.
# Author: David Bernat
# Date: 05/30/17
#
# Sample Usage:
#
# l = load("data/descriptions.txt", "data/queries.txt")
# descriptions, queries = l.load()
# ID = "00001"
# print("Document Text: {}".format(descriptions[ID]))
# print("Queries List: {}".format(queries[ID]))


class load():

    RECORD_SEPARATOR = "|||||"
    ID_COLUMN = "ID"
    DOCUMENT_COLUMN = "DOCUMENT"
    HEADER_COLUMNS = ["TITLE", "META", ID_COLUMN]

    def __init__(self, descriptions_path, queries_path):
        self._descriptions_path = descriptions_path
        self._queries_path = queries_path

    def load(self):

        # Load Descriptions File
        descriptions = {}
        with open(self._descriptions_path) as f:
            record, document = {}, ""
            for line in f.readlines():
                # Is the line a separator?
                if line.strip() == self.RECORD_SEPARATOR:
                    record[self.DOCUMENT_COLUMN] = document
                    descriptions[record[self.ID_COLUMN]] = record
                    record, document = {}, ""
                # Otherwise, parse its content
                else:
                    # Is the line a header column?
                    s = line.split(":")
                    if len(s) > 0 and s[0] in self.HEADER_COLUMNS:
                        record[s[0]] = ":".join(s[1:]).strip()
                    else:
                        document += line

        # Load Queries File
        queries = {}
        with open(self._queries_path) as f:
            for line in f.readlines():
                # ID:q1|q2|q3...
                s = line.strip().split(":")
                queries[s[0]] = s[1].split("|")

        return descriptions, queries