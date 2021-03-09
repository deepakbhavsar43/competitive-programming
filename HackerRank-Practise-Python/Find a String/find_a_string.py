def count_substring(string, sub_string):
    count = 0
    len_str = len(string)
    len_substr = len(sub_string)
    for i in range(len_str-(len_substr-1)):
        chk = string[i:i+len_substr]
        # print(chk)
        if chk == sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)