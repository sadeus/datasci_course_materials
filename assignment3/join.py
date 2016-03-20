import MapReduce
import sys

"""
Join relations in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    values = record
    mr.emit_intermediate(key, values)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    order = None
    joins = []
    list_of_values.sort(lambda x, y: x[0] < y[0])
    #print(list_of_values)
    for i in range(len(list_of_values)):
        for j in range(len(list_of_values)):
            if list_of_values[i][0] == 'order' and list_of_values[i][0] != list_of_values[j][0]:
                mr.emit(list_of_values[i] + list_of_values[j])


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
