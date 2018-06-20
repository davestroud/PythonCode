with open('heart_disease.csv') as fid:
    for idx, row in enumerate(fid):
        print(row, end=' ')
        if idx >= 4:
            break
