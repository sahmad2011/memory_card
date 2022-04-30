#Great app!


from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
    

app=QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card App")
main_win.move(400,300)
main_win.resize(400, 300)
main_win.current_qst = -1
label1 = QLabel("Which nationality does not exist?")
gbox1 = QGroupBox("Answer options")
gbox2 = QGroupBox("Correct or incorrect?")
label2 =QLabel("Correct/Incorrect")
label3 =QLabel("correct answer")
v4 = QVBoxLayout()
v4.addWidget(label2, alignment=Qt.AlignLeft)
v4.addWidget(label3, alignment = Qt.AlignCenter)
gbox2.setLayout(v4)

class Question():
    def __init__(
        self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
q1 = Question("When did the first comic book come out?", "1933", "1700", "2000", "1960")
q2 = Question("How long was Nelson Mandela in prison?", "27 years", "20 years", "5 years", "All of his life.")
q3 = Question("What word that starts with 'n' that means the practice to release all desires in Buddhism?", "nirvana", "nothing", "nealing", "nightpeace")
q4 = Question("In the past, (in South Africa) what word meant the separation of white people and black people?", "apartheid", "apetite", "apart", "diskriminasie")
q5 = Question("What date did Hurricane Katrina first start?", "23rd Aug 2005", "24th Aug 2005", "22nd Aug 2005", "24th Aug 2021")
q_list = [q1, q2, q3, q4, q5]

def show_ans():
        gbox1.hide()
        gbox2.show()
        ans_b.setText("Next Question")
        if answers[0].isChecked():
                label2.setText("Correct!")
        else:
                label2.setText("Incorrect! The answer is:") 
def show_qst():
        gbox2.hide()
        gbox1.show()
        ans_b.setText("Submit")
        RadioGroup.setExclusive(False)
        b1.setChecked(False)
        b2.setChecked(False)
        b3.setChecked(False)
        b4.setChecked(False)
        RadioGroup.setExclusive(True)
def test():
        if ans_b.text() == "Submit":
                show_ans()
        else:
                next_qst()
def ask(q: Question):
        shuffle(answers)
        label1.setText(q.question)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        label1.setText(q.question)
        label3.setText(q.right_answer)
        show_qst()


def next_qst():
    main_win.current_qst = main_win.current_qst + 1
    if main_win.current_qst >= len(q_list):
        main_win.current_qst = 0
    q = q_list[main_win.current_qst]
    ask(q)


ans_b = QPushButton("Answer")
RadioGroup = QButtonGroup()
b1=QRadioButton("Option 1")
b2=QRadioButton("Option 2")
b3=QRadioButton("Option 3")
b4=QRadioButton("Option 4")
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)
answers = [b1, b2, b3, b4]

v1=QVBoxLayout()
v2=QVBoxLayout()
v3=QVBoxLayout()
h1=QHBoxLayout()

v1.addWidget(label1)
v1.addWidget(gbox1)
v1.addWidget(gbox2)
v1.addWidget(ans_b, stretch=3)
v2.addWidget(b1)
v2.addWidget(b2)
v3.addWidget(b3)
v3.addWidget(b4)
h1.addLayout(v2)
h1.addLayout(v3)
gbox1.setLayout(h1)

main_win.setLayout(v1)

#gbox1.hide()
gbox2.hide()

#ask("In what year was the Great Fire of London?", "1666", "1999", "1862", "1665 ")
#ask("How long was Nelson Mandela in prison?", "27 years", "20 years", "5 years", "All of his life.")
#ask("What word that starts with 'n' that means the practice to release all desires in Buddhism?", "nirvana", "nothing", "nealing", "nightpeace")
#ask("In the past, (in South Africa) what word meant the separation of white people and black people?", "apartheid", "apetite", "apart", "diskriminasie")
ans_b.clicked.connect(test)
next_qst()
main_win.show()
app.exec()
