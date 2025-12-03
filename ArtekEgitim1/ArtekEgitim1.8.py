"""
class Person:

    def __init__(this,fname,lname,year):
        this.fname = fname
        this.lname = lname
        this.year = year
        print("Init fonksiyonu calisti")
    
    def intro(this):
        print(f"Hello my name is {this.name} and I was born in {this.year}")


class Student(Person):
    def __init__(this,fname,lname,year):
        Person.__init__(this,fname,lname,year)
        print("Student init calisti")


p1= Person("Atiba","Huchinson",1988)
s1= Student("Orkun","Kökcü",2001)

print(f"Isim: {p1.fname} {p1.lname} Yas: {2025-p1.year}")
print(f"Isim: {s1.fname} {s1.lname} Yas: {2025-s1.year}")

"""

#Quiz Programı

from random import choice


class Question:
    def __init__(this,text,choices,answer):
        this.text = text
        this.choices = choices
        this.answer = answer
    def checkAnswer(this,answer):
        return this.answer == answer

class Quiz:
    def __init__(this,questions):
        this.questions = questions
        this.score = 0
        this.questionIndex = 0
    def getQuestion(this):
        return this.questions[this.questionIndex]
    
    def displayQuestion(this):
        questions = this.getQuestion()
        print(f"Soru {this.questionIndex + 1}: {questions.text}")

        for q in questions.choices:
            print("-"+q)

        answer = input("Cevabiniz: ")
        this.guess(answer)

    def guess(this,answer):
        questions = this.getQuestion()

        if questions.checkAnswer(answer):
            this.score += 1
            print("Dogru cevap!")
        else:
            print("Yanlis cevap!")
        this.questionIndex += 1
        this.loadQuestions()
    
    def loadQuestions(this):
        if len(this.questions) == this.questionIndex:
            this.showScore()
        else:
            this.displayProgress()
            this.displayQuestion()
    
    def showScore(this):
        print(f"Toplam puaniniz: {this.score}")
    
    def displayProgress(this):
        totalQuestions = len(this.questions)
        questionNumber = this.questionIndex + 1

        if questionNumber > totalQuestions:
            print("Quiz bitti")
        else:
            print(f"Question {questionNumber} of {totalQuestions}".center(100,"*"))


    

q1 = Question("Türkiye'nin başkenti neresidir?", ["İstanbul", "Ankara", "İzmir", "Bursa"], "Ankara")
q2 = Question("Beşitaş hangi sezonda Şampiyonlar Ligi gruplarindan namaglup çikti?", ["2016-2017", "2017-2018", "2018-2019", "2019-2020"], "2017-2018")
q3 = Question("Beşiktaş en son hangi teknik direktör ile Süper Lig şampiyonu oldu?", ["Şenol Güneş", "Slaven Bilic", "Abdullah Avci", "Sergen Yalçin"], "Sergen Yalçin")

questions = [q1, q2, q3]
quiz = Quiz(questions)
quiz.loadQuestions()




    
    
        