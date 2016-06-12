import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.disable(logging.CRITICAL)

def sort_n_count(A, count):
    # B, C and D are tuples containing a sorted list, and a count.
    # Therefore sort_n_count needs to return the merged list, and the total count from all 3 tuples
    if len(A) == 1:
        logging.debug('returning ' + str(A))
        return (A, count)
    mid = len(A)//2
    B = sort_n_count(A[0:mid], count) # left split
    logging.debug('B is ' + str(B))
    C = sort_n_count(A[mid:], count) # right split
    logging.debug('C is ' + str(C))
    D = merge_n_count_split(B[0], C[0], count) # merge step with split inverse
    return (D[0], (B[1] + C[1] + D[1]))

def merge_n_count_split(B, C, count):
    logging.debug('B is type ' + str(type(B)))
    logging.debug('C is type ' + str(type(C)))
    i = 0 # looping through B
    j = 0  # looping through C
    merged = []
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            merged.append(B[i])
            i += 1
        elif B[i] > C[j]:
            merged.append(C[j])
            j += 1
            count += (len(B) - i)
            logging.debug('current count ' + str(count))
    # append the remaining
    while i < len(B):
        merged.append(B[i])
        i += 1
    while j < len(C):
        merged.append(C[j])
        j += 1
    logging.debug('merged is ' + str(merged))
    return (merged, count)

alist = [54,26,93,17,77,31,44,55,20]
#alist = [1,3,5,2,4,6]
newlist = sort_n_count(alist, 0)
print(newlist)