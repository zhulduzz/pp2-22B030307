import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))


#regex2

import re
def match(text):
        model = 'ab{2,3}'
        if re.search(model,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(match("ab"))
print(match("aabbbbbc"))


#regex3

import re
def text1(text):
        result = '^[a-z]+_[a-z]+$'
        if re.search(result,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text1("aab_cbbbc"))
print(text1("aab_Abbbc"))
print(text1("Aaab_abbbc"))


#regex4


import re
def text_match1(text):
        patterns1 = '[A-Z]+[a-z]+$'
        if re.search(patterns1, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match1("AaBbGg"))
print(text_match1("Python"))
print(text_match1("python"))
print(text_match1("PYTHON"))
print(text_match1("aA"))
print(text_match1("Aa"))


#regex5

import re
def text_match2(text):
        patterns2 = 'a.*?b$'
        if re.search(patterns2,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match2("aabbbbd"))
print(text_match2("aabAbbbc"))
print(text_match2("accddbbjjjb"))


#regex6

import re
my_text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", my_text))


#regex7

def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('python_exercises'))


#regex8

import re
Text = "PythonTutorialAndExercises"
print(re.findall('[A-Z][^A-Z]*', Text))


#regex9

import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))


#regex10

def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(camel_to_snake('PythonExercises'))