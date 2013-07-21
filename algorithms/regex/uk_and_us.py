import re


def get_input():
    '''Reads input. Hackerrank style.'''
    n=input()
    lines=[]
    for i in range(int(n)):
        lines.append(input())
    t=input()
    words=[]
    for i in range(int(t)):
        words.append(input())
    return lines,words
    
    
def search_word(line,word):
    '''Search word in line. Return count.'''
    pt=re.compile('{}[sz]e'.format(word[:-2]))
    return len(pt.findall(line))
    
    
def main():
    lines,words=get_input()
    for w in words:
        counter=0
        for l in lines:
            counter += search_word(l,w)
        print(counter)
    
    
if __name__ == '__main__':
    main()
