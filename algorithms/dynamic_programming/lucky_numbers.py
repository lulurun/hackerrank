'''
Created on Jul 21, 2013

@author: nirvam


A number is called lucky if the sum of its digits, as well as the sum of the squares of its digits is a prime number. How many numbers between A and B are lucky?

Input:
The first line contains the number of test cases T. Each of the next T lines contains two integers, A and B.

Output:
Output T lines, one for each case containing the required answer for the corresponding case.

Constraints:
1 <= T <= 10000
1 <= A <= B <= 10^18

Sample Input:
2
1 20
120 130

Sample Output:
4
1

Explanation:
For the first case, the lucky numbers are 11, 12, 14, 16.
For the second case, the only lucky number is 120.
'''

# TODO:(Nirvam) Answer not accepted by hackerrank. Too slow.
import random

def _get_input():
    numbers = []
    for l in range(int(input())):
        temp=[int(x) for x in input().split()]
        numbers.append(range(temp[0],temp[1]+1))
    return numbers


def _miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        #a_to_power = pow(a_to_power,2,n)
        a_to_power = (a_to_power ** 2) % n
    return a_to_power == n - 1


def _miller_rabin(n):
    if n == 2:
        return True
    elif n % 2 == 0 or n == 1:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    
    for repeat in range(20):
        a = 0
        while a == 0:
            #a = random.randint(n-1)
            a = random.randrange(n)
        if not _miller_rabin_pass(a, s, d, n):
            return False
    return True

if __name__ == '__main__':
    cases = _get_input()
    for case in cases:
        lucky_numbers=[]
        for number in case:
            number=str(number)
            digits=[int(x) for x in number]
            sum1=sum(digits)
            sum2=sum([x**2 for x in digits])
            if _miller_rabin(sum1) and _miller_rabin(sum2):
                lucky_numbers.append(number)
        print(len(lucky_numbers))

