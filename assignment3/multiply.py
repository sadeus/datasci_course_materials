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
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    for k in range(4):
        if matrix == "a":
            mr.emit_intermediate((i,k), ("a", j, value))
        else:
            mr.emit_intermediate((k,j),("b", i, value))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    a = {}
    b = {}
    for v in list_of_values:
        if v[0] == "a":
            i = v[1]
            a[i] = v[2]
        else:
            j = v[1]
            b[j] = v[2]
    if key[0] == 1 and key[1] == 3:
        print(a,b)
    result = 0
    for j in range(4):
        a_ij = 0
        b_jk = 0
        if j == 0 or j == 4:
            print(key)
            print(a[j] * b[j])
        if j in a:
            a_ij = a[j]
        if j in b:
            b_jk = b[j]
        result += a_ij * b_jk
    print(key[0],key[1], result)
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
