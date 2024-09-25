names = ['James', 'Robert', 'Lisa', 'Mary']
scores = [95, 96, 97, 94]

for x,y in zip(names, scores):
    print(x,y)
print()
if len(names) == len(scores):
    for i in range(len(names)):
        print(names[i], scores[i])
