import MapReduce
import sys

"""

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    mr.emit_intermediate("key", value[:-10])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    list_of_values = set(list_of_values)
    for v in list_of_values:
        mr.emit(v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
