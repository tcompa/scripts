def sum_cython(int N, K):
    cdef int i, tot_i
    tot_i = 0
    tot_j = 0
    for i in range(N):
        tot_i += i
    for j in range(K):
        tot_j += j
    return
