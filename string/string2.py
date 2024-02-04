"""  """
print('---------- 문자열 처리 ----------')
"""  """

python = "Python is Amazing"

# ----------- 1. 대소문자 -----------
# 1-1. 변환 (.lower(), .upper())
print(python.lower()) # 문자열 소문자 변환
print(python.upper()) # 문자열 대문자 변환
print(python) # Python is Amazing (원본 문자열 출력됨)

# 1-2. 확인 (.isupper(), .islower())
print(python[0].isupper()) # True
print(python[0].islower()) # False


# 2. ----------- 문자열 길이 (len(str)) -----------
print(len(python))


# 3. ----------- 문자열 치환 (.replace("target", "newStr")) -----------
print(python.replace("Python", "Java"))


# 4. ----------- 문자열에서 인덱스 확인 -----------
# 4-1. (.index("char")) => 해당하는 첫 문자에 대한 인덱스 반환
index = python.index("n")
print(index) # 5

# 4-1-2. 해당하는 두 번째 인덱스 찾고싶으면 두번째 인자에 +1 한 값을 넣어주면 그 다음 등장하는 문자의 인덱스 반환.
index = python.index("n", index + 1)
print(index) # 15

# 4-2. .find() : .index()와 유사
print(python.find("n"))

#4-2-2. 인자로 넣은 문자가 문자열에 없을 경우 -1 반환
print(python.find("j"))
# print(python.index("j")) # .index()는 오류 발생 (substring not found)
print("hi") # 위 코드 뒤에 출력문 있을 때, .find()는 출력 가능하지만 .index()는 출력 안됨


# 5. ----------- 문자열에 있는 문자(열) 개수 (.count("char" | "str")) -----------
print(python.count('Python'))
print(python.count('n'))

