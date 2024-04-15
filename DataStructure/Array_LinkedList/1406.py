string_list = list(input())
cursor = len(string_list)

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'P':
        string_list.insert(cursor, command[1])
        cursor += 1
  
    elif command[0] == 'L':
        if cursor > 0:
            cursor -= 1

    elif command[0] =='D':
        if cursor < len(string_list):
            cursor += 1
  
    else:
        if cursor > 0:
            string_list.remove(string_list[cursor-1])

print(''.join(string_list))
