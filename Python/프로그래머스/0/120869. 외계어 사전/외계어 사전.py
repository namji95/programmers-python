def solution(spell, dic):
    str_spell = ''.join(sorted(spell))
    for d in dic:
        if str_spell == ''.join(sorted(d)):
            return 1
    return 2