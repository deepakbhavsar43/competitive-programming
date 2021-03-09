# without using textwrap

def wrap(string, max_width):
    wrap_list = []
    for i in range(0, len(string), max_width):
        tmp = string[i:i+max_width]
        wrap_list.append(tmp)
        
    return '\n'.join(wrap_list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)