# primary list data
data = [4, 8, 1, 7, 6, 6, 4, 0, 12, 3]

# up sort
def maopao_up_sort(data):
    length = len(data)
    print 'Need sort data length = {0}'.format(str(length))
    for count in range(length):
        flag = False
        for site in range(length-count-1):
            tump = data[site+1]
            if data[site] > tump:
                data[site+1] = data[site]
                data[site] = tump
                flag = True
        if not flag:
            break
    return data

# down sort
def maopao_down_sort(data):
    length = len(data)
    print 'Need sort data length = {0}'.format(str(length))
    for count in range(length):
        flag = False
        for site in range(length-count-1):
            tump = data[site+1]
            if data[site] < tump:
                data[site+1] = data[site]
                data[site] = tump
                flag = True
        if not flag:
            break
    return data

# run test
print 'Primary list:'
print data
print 'Up sort:'
print maopao_up_sort(data)
print 'Down sort:'
print maopao_down_sort(data)