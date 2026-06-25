def solution(s):
    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, w in enumerate(word):
        s = s.replace(w, str(i))
    return int(s)