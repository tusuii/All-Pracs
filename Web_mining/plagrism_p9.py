import difflib

# open the two text files to compare
with open('original.txt', 'r') as file1, open('myfile.txt', 'r') as file2:
    text1 = file1.read()
    text2 = file2.read()

matcher = difflib.SequenceMatcher(None, text1, text2)
match_ratio = matcher.ratio()
if match_ratio > 0.1: # 10% chances of plagiarism check
    print(f"The files have a match ratio of {match_ratio}, indicating possible plagiarism.")
else:
    print("The files do not contain plagiarism.")
