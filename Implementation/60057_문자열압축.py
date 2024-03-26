import sys
input = sys.stdin.readline
s = input().strip()
answer = 0
answer_list = []
for cut in range(1,int(len(s)//2)+1):
    # cut = 1~ 문자열 길이 절반
    print('cut',cut)
    total = []
    cnt = 1
    tmp_answer = 0
    print('s: ',s)
    print('len(s)//cut-1: ',len(s)//cut-1)
    if len(s)//cut-1 >=0:
        for i in range(len(s)//cut-1):
            print('s[',i*cut,':',(i+1)*cut,']:',s[i*cut:(i+1)*cut])
            print('s[',(i+1)*cut,':',(i+2)*cut,']:',s[(i+1)*cut:(i+2)*cut])
            if s[i*cut:(i+1)*cut] == s[(i+1)*cut:(i+2)*cut]:
                cnt +=1
                print('cnt 추가: ',cnt)
            else:
                print('cnt append: ',cnt)
                total.append(cnt)
                print('total: ',total)
                cnt = 1
        total.append(cnt)
        print('최종 total: ',total)
        
        num_cnt = 0 # 1이 아닌 숫자 개수
        for j in range(len(total)):
            if total[j]==1:
                continue
            num_cnt += len(str(total[j]))
        if len(s)%cut !=0:
            tmp_answer += len(s)%cut
        tmp_answer += num_cnt + len(total)*cut # 숫자 개수 + 문자 개수
        print('tmp_answer:',tmp_answer)
        answer_list.append(tmp_answer)

print('최종 tmp_answer : ',tmp_answer)
answer = min(answer_list)
print('answer: ',answer)

