# wanted_pre_onboarding
* 원티드 프리온보딩 백엔드 코스 사전과제입니다.
* **지원 접수**: 2022.06.08(수) ~ 2022.06.22(수) 19시
* **참가자 선발**: 2022.06.24(금) 17:00
* **온보딩 코스**: 2022.06.27(월) ~ 2022.07.29(금) 5주

***

### 🎬 과제 안내
* 아래 서비스 개요 및 요구사항을 만족하는 REST API 서버를 구현합니다.
* 사용가능 언어와 프레임워크: Python - Django, Flask / Javascript - Node.js(Express, NestJS)
* 선택한 언어와 프레임워크: **Python - DJango**


### 🎬 서비스 개요
* 본 서비스는 기업의 채용을 위한 웹 서비스입니다.
* 회사는 채용공고를 생성하고, 이에 사용자는 지원합니다.

### 🎬 필수 기술요건
* REST API로 구현.
* ORM 사용하여 구현.
* RDBMS 사용 - **SQLite** 선택

***

### 🎬 기본 세팅

```
pip install -r requirements.txt
```

```python
# post/tests.py
## SECRET_KEY 생성

import string, random
# Get ascii Characters numbers and punctuation (minus quote characters as they could terminate string).
chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')
SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])
print(SECRET_KEY)
```

***

### 🎬 전체 API (swagger 이미지)

<img src='https://user-images.githubusercontent.com/96091519/174990580-17e9f794-b8cb-4643-b82f-a9898bd2202e.JPG'>

***

### 🎬 요구사항 및 구현화면
**🎯 1. 채용공고를 등록합니다.**
```python
{
  "회사_id":회사_id,
  "채용포지션":"백엔드 주니어 개발자",
  "채용보상금":1000000,
  "채용내용":"원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..",
  "사용기술":"Python"
}
```
<img src='https://user-images.githubusercontent.com/96091519/174994264-e7ce3f85-940a-44fc-b8d1-749b4a5c4943.JPG'>

***

**🎯 2. 채용공고를 수정합니다. (회사 id 이외 모두 수정 가능)**

```python
{
  "채용포지션":"백엔드 주니어 개발자",
  "채용보상금":1500000, # 변경됨
  "채용내용":"원티드랩에서 백엔드 주니어 개발자를 '적극' 채용합니다. 자격요건은..", # 변경됨
  "사용기술":"Python"
}
```
<img src='https://user-images.githubusercontent.com/96091519/174994997-c5e78e22-8c61-4b5f-9c43-55ae1439ec29.JPG'>

***

**🎯 3. 채용공고를 삭제합니다.**
* DB에서 삭제된다.

<img src='https://user-images.githubusercontent.com/96091519/174995287-37ab99be-f519-4f06-9b60-9aa7e8f1ff79.JPG'>

***


**🎯 4. [일부 가산점] 채용공고 목록을 가져옵니다.**
* 사용자는 채용공고 목록을 아래와 같이 확인할 수 있음.
```python
[
  {
    "채용공고_id": 채용공고_id,
    "회사명":"원티드랩",
    "국가":"한국",
    "지역":"서울",
    "채용포지션":"백엔드 주니어 개발자",
    "채용보상금":1500000,
    "사용기술":"Python"
    },
  {
    "채용공고_id": 채용공고_id,
    "회사명":"네이버",
    "국가":"한국",
    "지역":"판교",
    "채용포지션":"Django 백엔드 개발자",
    "채용보상금":1000000,
    "사용기술":"Django"
    },
  ...
]
```

<img src='https://user-images.githubusercontent.com/96091519/174995651-2f5764f5-71ce-484f-9b57-ebefb07a7387.JPG'>

***

* 채용공고 검색기능 구현(선택사항 및 가산점 요소)
```python
# Example - 1) some/url?search=원티드
[
  {
    "채용공고_id": 채용공고_id,
    "회사명":"원티드랩",
    "국가":"한국",
    "지역":"서울",
    "채용포지션":"백엔드 주니어 개발자",
    "채용보상금":1500000,
    "사용기술":"Python"
	},
  {
    "채용공고_id": 채용공고_id,
    "회사명":"원티드코리아",
    "국가":"한국",
    "지역":"부산",
    "채용포지션":"프론트엔드 개발자",
    "채용보상금":500000,
    "사용기술":"javascript"
	}
]

# Example - 2) some/url?search=Django
[
  {
    "채용공고_id": 채용공고_id,
    "회사명":"네이버",
    "국가":"한국",
    "지역":"판교",
    "채용포지션":"Django 백엔드 개발자",
    "채용보상금":1000000,
    "사용기술":"Django"
	},
  {
    "채용공고_id": 채용공고_id,
    "회사명":"카카오",
    "국가":"한국",
    "지역":"판교",
    "채용포지션":"Django 백엔드 개발자",
    "채용보상금":500000,
    "사용기술":"Python"
	}
  ...
]
```

<img src='https://user-images.githubusercontent.com/96091519/174996274-cd266947-1607-4e55-9424-68afd39c26a9.JPG'>

***

**🎯 5. [일부 가산점] 채용 상세페이지를 가져옵니다.**
```python
{
  "채용공고_id": 채용공고_id,
  "회사명":"원티드랩",
  "국가":"한국",
  "지역":"서울",
  "채용포지션":"백엔드 주니어 개발자",
  "채용보상금":1500000,
  "사용기술":"Python",
  "채용내용": "원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..",
  "회사가올린다른채용공고":[채용공고_id, 채용공고_id, ..] # id List (선택사항 및 가산점요소).
}
``` 

<img src='https://user-images.githubusercontent.com/96091519/174996631-ec4ed246-a878-4e95-b5aa-566ecabd2d77.JPG'>

***

**🎯 6. [가산점] 사용자는 채용공고에 지원합니다. (1회만)**

```python
{
  "채용공고_id": 채용공고_id,
  "사용자_id": 사용자_id
}
```
<img src='https://user-images.githubusercontent.com/96091519/174996926-4bf1628b-d1bb-4821-87f8-fe7f918784f4.JPG'>

