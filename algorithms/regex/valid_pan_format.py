import re


def get_input():
    '''Reads input. Hackerrank style.'''
    n=input()
    lines=[]
    for i in range(int(n)):
        lines.append(input())
    return lines
    
    
def test_pan(line):
    '''PAN format test (CCCCCDDDDC).'''
    pt=re.compile('^[A-Z]{5}\d{4}[A-Z]$')
    return pt.search(line)
    
    
def main():
    lines=get_input()
    for l in lines:
        if test_pan(l):
            print('YES')
        else:
            print('NO')
        
    
if __name__ == '__main__':
    main()
