import re


def task():
    word_list = ["Everest is the largest mountain in the World"]


    word_pattern1 = re.compile(r'.+?')  # побуквенно ))

    for word in word_list:
        print(word_pattern1.findall(word))


    word_pattern2 = re.compile(r'(\w)')  # последние буквы ))

    for word in word_list:
        print(word_pattern2.findall(word))


    word_pattern = re.compile(r'\w+')  # все вместе

    for word in word_list:
        print(word_pattern.findall(word))


    word_pattern = re.compile(r'\w*')  # все вместе

    for word in word_list:
        print(word_pattern.findall(word))


    word_pattern = re.compile(r'\b[aeioyuAEIOUY]\w+')  # гласные

    for word in word_list:
        print(word_pattern.findall(word))

if __name__ == "__main__":
    task()
