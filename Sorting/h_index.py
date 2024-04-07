citations = [3,0,6,1,5]
answer = 0
citations.sort(reverse=True)
h = 0
for i in range(len(citations)):
    if i+1 <= citations[i] and len(citations)-1 <= i+1:
        if h < i+1:
            h = i+1
answer = h
print(answer)