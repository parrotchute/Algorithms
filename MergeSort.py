import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.disable(logging.CRITICAL)

def merge_sort(A):
    if len(A) == 1:
        logging.debug('returning ' + str(A))
        return A
    mid = len(A)//2
    B = merge_sort(A[0:mid])
    logging.debug('B is ' + str(B))
    C = merge_sort(A[mid:])
    logging.debug('C is ' + str(C))
    return merge(B, C)


def merge(B, C):
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
    # append the remaining
    while i < len(B):
        merged.append(B[i])
        i += 1
    while j < len(C):
        merged.append(C[j])
        j += 1
    logging.debug('merged is ' + str(merged))
    return merged

alist = [54,26,93,17,77,31,44,55,20]
newlist = merge_sort(alist)
print(newlist)