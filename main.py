
def main(prefm, prefw):
    IS_SINGLE = -1
    
    n       = len(prefm)
    free    = []
    wife    = [0] * n
    husband = [0] * n
    count   = [0] * n
    inverse = [[]] * n
    
    for i in range(n):
        inverse[i] = [0] * n

    for i in range(n):
        free.append(i)
        wife[i] = IS_SINGLE
        husband[i] = IS_SINGLE
        count[i] = 0
        for j in range(n):
            inverse[i][prefw[i][j]] = j
    
    while free:
        m = free.pop(0)
        w = prefm[m][count[m]]
        count[m] = count[m] + 1

        if husband[w] == IS_SINGLE:
            husband[w], wife[m] = m, w
        elif inverse[w][m] < inverse[w][husband[w]]:
            free.insert(0, husband[w])
            wife[husband[w]] = IS_SINGLE
            husband[w], wife[m] = m, w
        else:
            free.insert(0, m)

    return zip(range(0, n), wife)


if __name__ == '__main__':
    ntests = int(input())

    for test in range(ntests):
        
        nmarriages = int(input())
        if nmarriages < 0 or nmarriages > 27:
            raise 'Invalid paramater n'

        # encode input
        m, w, = 0, 0
        idvm_id_map, idvw_id_map = {}, {}
        id_idvm_map, id_idvw_map = {}, {}
        individuals = input().split()

        for idv in individuals:
            if idv.islower():
                idvm_id_map[idv] = m
                id_idvm_map[m] = idv
                m = m + 1
            else:
                idvw_id_map[idv] = w
                id_idvw_map[w] = idv
                w = w + 1

        # parse preferences
        prefm, prefw = [[]] * nmarriages, [[]] * nmarriages
        for m in range(nmarriages):
            name, prefs = input().split(':')
            prefm[idvm_id_map[name]] = list(map(lambda x: idvw_id_map[x], list(prefs)))

        for m in range(nmarriages):
            name, prefs = input().split(':')
            prefw[idvw_id_map[name]] = list(map(lambda x: idvm_id_map[x], list(prefs)))
        
        # run algorithm
        r = main(prefm, prefw)

        # decode output
        for m, w in r:
            print(id_idvm_map[m], ' ', id_idvw_map[w])
