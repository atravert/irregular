from random import choice
from IPython.display import clear_output

N_questions = 10

liste = (
        ("be", "was", "been", "être"),
        ("begin", "began", "begun", "commencer"),
        ("break", "broke", "broken", "casser"),
        ("bring", "brought", "brought", "apporter"),
        ("eat", "ate", "eaten", "manger"),
        # ("", "", "", "")
        )

questions = ["Quel est l'infinitif (anglais !) correspondant à ",
            "Quel est le preterit associé à ",
            "Quel est le participe passé associé à ",
            "Quel est l'infinitif français associé à "]


def exercice(n_questions=10):

    score = 0
    clear_output
    for i in range(n_questions):
        verbe = choice(liste)
        i_v = choice(range(4))
        i_q = choice([x for x in range(4) if x != i_v])

        print(f"Question {i+1}/{n_questions} : {questions[i_q]} \"{verbe[i_v]}\" ?")
        print("\r>", end=" ")
        reponse = input()
        if reponse.lower() == verbe[i_q]:
            score = score + 1 
            print("Bravo !!!")
        else:
            print("Bouhhhh... la reponse était: \"" + verbe[i_q]+"\"")
        
    note = (score / n_questions) * 10
    print(f"Exercice terminé, note = {note} / 10")

if __name__ == "__main__":
    exercice(N_questions)