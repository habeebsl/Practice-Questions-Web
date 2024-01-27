import random, os

def generate_pq(topic):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(f"{os.path.join(base_dir, 'project', 'static', 'Practice questions', topic)}.txt", "r") as file:  # Changed backslash to forward slash
        questions = file.readlines()
        random_question = random.randint(0, len(questions)-1)
        return f"{questions[random_question]}"
           
    # else:        
    #     random_course = random.randint(0, len(courses)-1)
    #     choose_question(courses[random_course])

    # user_input=input("Would you like another?? ")
    # if user_input.lower() == 'yes':
    #     continue
    # else:
    #     break
