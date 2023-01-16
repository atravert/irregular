from random import choice
from IPython.display import clear_output

N_questions = 10

list = (
        ("be", "was", "been", "être"),
        ("begin", "began", "begun", "commencer"),
        ("break", "broke", "broken", "casser"),
        ("bring", "brought", "brought", "apporter"),
        ("eat", "ate", "eaten", "manger"),
        # ("", "", "", ""),
        )

questions = ["What is the (english !) infinive of ",
            "What is the preterite corresponding to ",
            "What is the past participe corresponding to ",
            "What is the french infinive of "]


def exercise(n_questions=10):

    score = 0
    clear_output
    for i in range(n_questions):
        verb = choice(list)
        i_v = choice(range(4))
        i_q = choice([x for x in range(4) if x != i_v])

        print(f"Question {i+1}/{n_questions} : {questions[i_q]} \"{verb[i_v]}\" ?")
        print("\r>", end=" ")
        answer = input()
        if answer.lower() == verb[i_q]:
            score = score + 1 
            print("Bravo !!!")
        else:
            print("Bouhhhh... the correct answer was: \"" + verb[i_q]+"\"")
        
    note = (score / n_questions) * 10
    print(f"Exercize terminated, grade = {note} / 10")

if __name__ == "__main__":
    exercise(N_questions)