import re

word=re.compile('hackerrank')


def get_input():
    '''Reads input. Hackerrank style.'''
    l=input()
    lines=[]
    for i in range(int(l)):
        lines.append(input())
    return l,lines
    
    
def search_word(line):
    try:
        begin,end=list(zip(*[x.span() for x in word.finditer(line)]))
    except ValueError:
        return -1
    b = 0 in begin
    e = len(line) in end
    if b and e:
        return 0
    elif b:
        return 1
    elif e:
        return 2
    else:
        return -1
    
    
def main():
    line_counts,lines=get_input()
    for line in lines:
        print(search_word(line))
    
if __name__ == '__main__':
    main()
