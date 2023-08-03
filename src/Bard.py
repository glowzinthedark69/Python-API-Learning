from bardapi import Bard
import os

os.environ[
    "_BARD_API_KEY"
] = "YAi8BgMmsiIkHrsFiuqJp73SDhq7y8HtMiH6-AZuxwPeWS9RI5IBvsDuC83hh-OcgBqmgw."

var = Bard().get_answer("How do I test an API without any documentation")["content"]
print(var)
