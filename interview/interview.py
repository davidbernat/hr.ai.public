# HR.ai interview problem
# Please see repository README.md for more information
#
# Author: David Bernat
# Date: 05/30/17

from load import load

l = load("data/descriptions.txt", "data/queries.txt")
descriptions, queries = l.load()

ID = "00001"
print("Document Text: {}".format(descriptions[ID]))
print("Queries List: {}".format(queries[ID]))

