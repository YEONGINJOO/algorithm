# 백준알고리즘

## 2557번
```python
print("Hello World")
```

## 1000번
```python
a, b = map(int, input().split())
print(a+b)
```

## 1001번
```python
a, b = map(int, input().split())
print(a-b)
```
## 1008번
```python
a, b = map(int, input().split())
print(a/b)
```
## 2558번
```python
a = int(input())
b = int(input())
print(a+b)
```
## 10171번
```python
#실패
# print("\    /\  " )
# print(" )  ( ') " )
# print("(  /  )  " )
# print(" \(__)|  " )
#실패
# print(r"\    /\  " )
# print(r" )  ( ') " )
# print(r"(  /  )  " )
# print(r" \(__)|  " )

 print(r"\    /\  ")
 print(r" )  ( ') ")
 print(r"(  /  )  ")
 print(r" \(__)|  ")
```

## 10172번
```python
print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"""\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")
```
## 10699번
```python
print("2023-01-13")
```
## 10950번
```python
T = int(input())
for i in range(1,T+1):
    nlist = map(int,input().split())
    print(sum(nlist))
```
## 10998번
```python
a, b = map(int,input().split())
print(a*b)
```
## 10951번
```python
while True:
    try:
        a,b = map(int,input().split())
        print(a+b)
    except:
        break
```
## 10952번
```python
while True:
    a,b = map(int,input().split())
    if (a and b) == 0:
        break
    else:
        print(a+b)
```
## 5338번
```python
print("       _.-;;-._")
print("'-..-'|   ||   |")
print("'-..-'|_.-;;-._|")
print("'-..-'|   ||   |")
print("'-..-'|_.-''-._|")
```
## 2475번
```python
a = input().split()
k = 0
for i in range(5):
    k = k + int(a[i])**2 
print(k % 10)
```

## 2475번
```python
T = int(input())
for i in range(1,T+1):
    a = input()
    print(f'{a[0]}{a[-1]}')
 ```