from bardapi import Bard
import os

os.environ['_BARD_API_KEY'] = "XQi8Bh3LN5phZU_Mx1ajZfofSy5xm16j17y0aTVyP1fC80-nYww1PMngf9spfaq0rqXzXw."

var = Bard().get_answer("How do I test an API without any documentation")['content']
print(var)



