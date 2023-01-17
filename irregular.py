from random import choice

N_questions = 20

list = (
        ("be", "was", "been", "être"),
        ("begin", "began", "begun", "commencer"),
        ("break", "broke", "broken", "casser"),
        ("bring", "brought", "brought", "apporter"),
        ("eat", "ate", "eaten", "manger"), 
        ("build", "built", "built", "construire"),
        ("burn", "burnt", "burnt", "brûler"),
        ("buy", "bought", "bought", "acheter"),
        ("can", "could", "", "pouvoir"),
        ("catch", "caught", "caught", "attraper"),
        ("choose", "chose", "chosen", "choisir"),
        ("come", "came", "come", "venir"),
        ("cut", "cut", "cut", "couper"),
        ("do", "did", "done", "faire"),
        ("dream", "dreamt", "dreamt", "rêver"),
        ("drink", "drank", "drunk", "boire"),
        ("drive", "drove", "driven", "conduire"),
        ("fall", "fell", "fallen", "tomber"),
        ("feel", "felt", "felt", "resentir"),
        ("find", "found", "found", "trouver"),
        ("forget", "forgot", "forgotten", "oublier"),
        ("get", "got", "got", "obtenir"),
        ("give", "gave", "given", "donner"),
        ("go", "went", "gone", "aller"),
        ("have", "had", "had", "avoir"),
        ("hear", "heard", "heard", "entendre"),
        ("hide", "hid", "hidden", "cacher"),
        ("hit", "hit", "hit", "frapper"),
        ("hurt", "hurt", "hurt", "blesser"),
        # ("", "", "", ""),
        )

questions = ["What is the (english !) infinive of ",
            "What is the preterite corresponding to ",
            "What is the past participe corresponding to ",
            "What is the french infinive of "]


def exercise(n_questions=10):

    points = 0
    for i in range(n_questions):
        
        verb = choice(list)
        
        if verb[0] == "can":
            # an exception for modal verb
            i_v = choice((0, 1, 3))
        else:
            i_v = choice(range(4))
        
        i_q = choice([x for x in range(4) if x != i_v])

        print(f"Question {i+1}/{n_questions} : {questions[i_q]} \"{verb[i_v]}\" ?")
        print(">", end=" ")
        answer = input()
        
        if answer.lower() == verb[i_q]:
            points += 1 
            print("Bravo !!!")
        else:
            print("Bouhhhh... the correct answer was: \"" + verb[i_q]+"\"")
        
    score = (points / n_questions) * 10
    print(f"Exercise terminated, score = {score} / 10")

if __name__ == "__main__":
    exercise(N_questions)
