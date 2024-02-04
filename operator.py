"""  """
print("---------- 연산자 ----------")
"""  """

print( 1+1)
print(5/3) # 1.6666666666666667
print(5//3) # 몫 구하기 : 1

# 비교 연산자
print(3 == 3) # True

print(1 != 1) # False
print(not (1 != 1)) # True

print((3 > 0) and (3 < 5)) # True (True and True)
print((3 > 0) & (3 < 5)) # 위와 같음

print((3 > 0) or (3 > 5)) # True (True or False)
print((3 > 0) | (3 > 5)) # 위와 같음

print(5 > 4 > 3) # True (5는 4보다 크고, 4는 3보다 크다 = True & True)
print(5 > 4 > 7) # False (5는 4보다 크고, 4는 7보다 크다 = True & False)
print(5 > 7 > 10) # False (False & False)