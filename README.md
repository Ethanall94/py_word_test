# py_word_test

[참고한 영상](https://youtu.be/IAmNZrrrHmE)

### 추가한 기능
- 종료 후 틀린 단어 모아서 띄우기
- 틀린 단어 스크롤해서 보기
- 500번 테스트 후 종료되도록 설정
- 우측 하단에 푼 문제 수 출력
- 문제 중복 방지
- pyttsx3를 통한 TTS
- NEXT 버튼 클릭 시 넘긴 문제도 결과창에서 같이 볼 수 있음
  
### exe file 만들기
파이썬 버전문제, path 해결 후<br>
`pip install pyinstaller`<br>
`pyinstaller -F -w wordTest.py`<br>
-F 옵션을 통해 단일파일 생성<br>
-w 옵션을 통해 실행 시 터미널 뜨지 않도록 적용<br>

### task
- 넘어가는 속도 - 해결, 230810
- NEXT 클릭 시 틀린 단어로 넘기기 - 해결, 230825
- 1/500 카운팅하기 - place로 해결, 230810
- 3000 후 다음 문제로 이동 : 해당 기능 불필요
- 다른 TTS 찾아보기

### Usage
- (주의) csv 파일과 exe 파일이 같은 폴더 내에 있어야 정상 작동함
- 사용 시 csv file 이름을 eng_word.csv 로 변경 요망
- 데이터는 `단어,뜻` 형식으로 입력되어야함


### 동작 화면
![quiz](https://github.com/Ethanall94/py_word_test/assets/85244599/2722cd1d-3139-4be1-9205-b499f2ae672f)
![result](https://github.com/Ethanall94/py_word_test/assets/85244599/7d2a5e7a-37f6-4aa8-9371-2723cc270aa7)

