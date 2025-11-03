# Complete a solução de forma que ela inverta a string que lhe foi passada.
# 'world'  =>  'dlrow'.
# 'word'   =>  'drow'.

def solution(string):
    invert = ''
    for each_letter in string:
        invert = each_letter + invert

    return invert

solution('world')
solution('word')
solution('hello')