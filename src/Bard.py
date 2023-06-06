from bardapi import Bard
import os

os.environ['_BARD_API_KEY'] = "WAi8BgSML1yQxmr3hd-M15iePeVD_EYTp4Y0KTwpR7lbnrxYC6_jCXZ4h3Luo5TFRa55tw."

var = Bard().get_answer("What makes Bard better?")['content']
print(var)



