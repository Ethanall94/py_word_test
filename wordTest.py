BGCOLOR = "#4682b4"
WRONG_COLOR = "#d3d3d3"
CORRECT_COLOR = "#9acd32" 
BTN_COLOR = "#F0F0F0"
NEXT_BTN = "#c0c0c0"

import csv
from tkinter import *
import random

with open("eng_word.csv", "r", encoding="UTF-8-sig") as file:
	questions = list(csv.reader(file))

answer = 0
cnt = 0
multi_choice = []
word_list = []

# 문제 생성
def next_question():
	global answer
	global multi_choice

	for i in range(4):
		buttons[i].config(bg=BTN_COLOR)

	# 문제와 정답 추출
	multi_choice = random.sample(questions, 4)
	answer = random.randint(0,3)
	cur_question = multi_choice[answer][0]

	question_label.config(text=cur_question)

	for i in range(4):
		buttons[i].config(text=multi_choice[i][1])

# 정답 체크
def check_answer(idx, multi_choice, answer):
	global word_list
	global cnt

	idx = int(idx)

	cnt = cnt + 1

	if cnt == 500: # 500번 돌고 끝남
		window.destroy()
	else:
		if answer == idx:
			# 버튼 색 변경
			buttons[idx].config(bg=CORRECT_COLOR)
			window.after(500, next_question)
		else: # 틀렸을 때
			buttons[idx].config(bg=WRONG_COLOR)
			word_list.append(multi_choice[answer])
			window.after(500, next_question)
			

window = Tk()

window.title("영어 퀴즈")
window.config(padx=30, pady=10, bg=BGCOLOR)
question_label = Label(window, width=20, height=2, text="Test",
	font=("나눔바른펜", 25, "bold"), bg=BGCOLOR, fg="white")
question_label.pack(pady=30)

buttons=[]

for i in range(4):
	btn = Button(window, text=f"{i}번", width=35, height=2, 
	font=("나눔바른펜", 15, "bold"), bg=BTN_COLOR,
	command = lambda idx=i: check_answer(idx, multi_choice, answer))
	btn.pack()
	buttons.append(btn)


next_btn = Button(window, text="NEXT", width=15, height=2, 
command = next_question,
font = ("나눔바른펜", 15, "bold"), bg=NEXT_BTN)
next_btn.pack(pady=30)

next_question()

window.mainloop()


# 출력처리 ------------------------------------
ws = Tk()
ws.title('result')
ws.geometry('500x600')
ws.config(bg=BGCOLOR)

frame = Frame(ws)
frame.pack(expand=True, fill=BOTH)

lb = Listbox(
    frame,
    font=("나눔바른펜", 15, "bold"), bg=BGCOLOR, fg="white"
    )
lb.pack(expand=True, fill=BOTH, side=LEFT)

sb = Scrollbar(
    frame, 
    orient=VERTICAL
    )
sb.pack(fill=Y, side=RIGHT)

lb.configure(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# 결과 받아와서 순서대로 넣어주기
for i in range(len(word_list)):
	string = ' '.join(word_list[i])
	lb.insert(i, string)

ws.mainloop()