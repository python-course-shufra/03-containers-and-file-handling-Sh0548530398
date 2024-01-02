classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]

def index(name):
    for i in classroom:
        if i['name']==name:
            return classroom.index(i)
        
def add_student(name, email=None):
    if email:
      classroom.append({'name':name ,'email':email, 'grades':[]})
    else: 
      classroom.append({'name':name ,'email':name.lower()+'@example.com', 'grades':[]})

def delete_student(name):
    i=index(name)
    del classroom[i]


def set_email(name, email):
     i=index(name)
     classroom[i]['email']=email


def add_grade(name, profession, grade):
     i=index(name)
     t=profession,grade
     classroom[i]['grades'].append(t)


def avg_grade(name, profession):
     i=index(name)
     sum=0
     count=0
     for i in classroom[i]['grades']:
          if i[0]==profession:
               sum+=i[1]
               count+=1
     return sum/count  


def get_professions(name):
     i=index(name)
     s=set()
     for i in classroom[i]['grades']:
          s.add(i[0])
     l=[]
     l=s          
     return l     
