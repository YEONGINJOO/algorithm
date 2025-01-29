n = int(input())
s = 'WelcomeToSMUPC'
a = len(s)
if a >= n:
    print(s[n-1])
else:
    print(s[n % a -1])