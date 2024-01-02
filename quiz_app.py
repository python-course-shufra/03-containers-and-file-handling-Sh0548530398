import sys
import random


               
def q(subgect,num_question,i):
    with open(f'questions\{subgect}.txt')as read_file:
        for line in read_file:
            if(i==num_question):
                i+=1
                line=line.strip()
                parts= line.split(';')
                question=parts[0]
                answer=parts[1].strip()
                spare_answers=parts[2].strip()
                spare_answers=spare_answers.split(', ')
                l=spare_answers
                l.append(answer.strip())
                random.shuffle(l)
                print (question)
                for j,an in enumerate(l):
                    print(f'{j+1}. {an}')
                choose=input("select your answer: ")
                choose_num= int(choose)
                return l[choose_num-1]==answer   
            else:
                i+=1

def main():
    subgect=sys.argv[1]
    num_question=sys.argv[2]
    num_question=int(num_question)
    i=num_question
    sum=0
    for k in range(num_question):
    #   print(q(subgect,num_question,i))
      sum+=q(subgect,num_question,i)
      i-=1
    print(f'you answer{sum}/{num_question} question')
   
   
   





if __name__ == '__main__':
    main()
