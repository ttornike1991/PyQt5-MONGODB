import random
import pymongo


conn=pymongo.MongoClient()
DATADB=conn.UNIVERSITY






def create_doc():
    LNames = ['SMITH', 'BROWN', 'WILSON', 'THOMSON', 'ROBERTSON', 'CAMPBELL', 'STEWART', 'ANDERSON', 'MACDONALD',
          'MARSHALL', 'STEVENSON', 'WOOD', 'CRAIG', 'SUTHERLAND', 'MCKENZIE', 'KENNEDY', 'JONES', 'BURNS',
          'WHITE', 'MUIR', 'MURPHY', 'JOHNSTONE', 'HUGHES', 'WATT', 'MCMILLAN', 'MCINTOSH', 'MILNE', 'MUNRO',
          'RITCHIE', 'DICKSON', 'WALKER', 'PATERSON', 'YOUNG', 'WATSON', 'MORRISON', 'MILLER', 'FRASER',
          'CAMERON', 'FERGUSON', 'MARTIN', 'SIMPSON', 'KERR', 'HAMILTON', 'CUNNINGHAM',  'DOCHERTY', 'DAVIDSON',
          'DUNCAN', 'FLEMING', 'DONALDSON', 'CHRISTIE', 'DOUGLAS', 'GRAHAM', 'MACKENZIE', 'BLACK', 'MACKAY',
          'MACLEOD', 'THOMPSON', 'GORDON', 'WALLACE', 'GIBSON', 'RUSSELL', 'MCLEAN', 'MACLEOD',
          'ALLAN', 'ANDERSON', 'BLACK', 'BROWN', 'MCKAY', 'MCLEAN', 'MCMILLAN', 'MILLAR', 'MILLER',
          'ROBERTSON', 'RITCHIE', 'DUNCAN', 'DONALDSON', 'DOCHERTY', 'CUNNINGHAM', 'CRAWFORD', 'MITCHELL', 'MILNE',
          'SUTHERLAND', 'STEVENSON', 'SINCLAIR', 'SIMPSON', 'GORDON', 'GIBSON', 'FRASER', 'ROSS', 'RUSSELL',
          'TAYLOR', 'THOMPSON', 'THOMSON', 'WALKER', 'JOHNSTONE', 'JONES', 'WATT', 'KERR', 'WILLIAMS',
          'WILLIAMSON']
    FNames = ['Alina', 'Arya', 'Carina', 'Daisy', 'Eliana', 'Farrah', 'Gianna', 'Hana', 'Irene', 'Jasmine', 'Kiara',
          'Lucia', 'Maya', 'Meera', 'Naomi', 'Nadia', 'Nina', 'Reina', 'Sophia', 'Sahara', 'Sasha', 'Talia', 'Vera',
          'Abner', 'Adalius', 'Aerin', 'Alaric', 'Aleph', 'Amias', 'Arjan', 'Arlo', 'Bevan', 'Bexley', 'Binx', 'Brea',
          'Brinley', 'Bastien', 'Beckett', 'Bohan', 'Brio', 'Brixton', 'Cala', 'Camari', 'Carine', 'Charon', 'Cleo',
          'Cora', 'Cosima',   'Caius', 'Caspar', 'Caspian','Cillian', 'Cohen', 'Cullen', 'Danica', 'Delaney', 'Decker', 'Delphine', 'Denver', 'Diem', 'Declan', 'Demarcus',
          'Deveraux', 'Elin', 'Elettra', 'Elodie', 'Elora', 'Ember', 'Eliseo', 'Emil', 'Emrys', 'Ephraim', 'Everett',
          'Fabiola', 'Dempsey', 'Farren', 'Floriana', 'Freja', 'Fergus', 'Francisco']
    x = ['Fundamentals of programming', 'Calculus II', 'Introduction to physics', 'computer skills','Introduction to Chemistry', 'Introduction to Biology',
     'Algorithms I', 'Introduction to Electronics','Data structures', 'Algorithms II''Fundamentals of programming', 'Calculus II', 'Introduction to Physics',
      'computer skills','Introduction to Biology','Data structures', 'Algorithms II''Fundamentals of programming', 'Calculus II', 'Introduction to Physics',
      'computer skills','Introduction to Biology','Data structures', 'Algorithms II''Fundamentals of programming', 'Calculus II', 'Introduction to Physics',
      'computer skills','Introduction to Biology','Data structures', 'Algorithms II''Fundamentals of programming', 'Calculus II', 'Introduction to Physics', ]
    subjex=[]
    for i in range(len(FNames)):
        for k in x:
            subjex.append(k)
            
    ids=[] 
    for i in range(len(FNames)): ids.append(i)

    P = [str(i) for i in range(101)]
    Point = [random.choice(P) for i in range (len(LNames))  ]
    

    docs=[]
    


    for a, b ,c,d,e in zip (FNames,LNames,ids,subjex,Point):
        doc={"first_name":a,"last_name":b,"_id":c,"Subject":d,"Point":e}
        docs.append(doc)
    
    print(docs)
    DATADB.students.insert_many(docs)
    
    

