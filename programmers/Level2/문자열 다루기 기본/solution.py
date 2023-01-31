def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            if type(int(s)) == int:
                return True
        except ValueError:
            return False
    else:
        return False