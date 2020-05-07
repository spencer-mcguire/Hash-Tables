
def word_count(s):
    word_dic = {}
    # Case should be ignored. Output keys must be lowercase.
    # Key order in the dictionary doesn't matter.
    # Split the strings into words on any whitespace.
    # Ignore each of the following characters:
    # ```
    # " : ; , . - + = / \ | [ ] { } ( ) * ^ &
    # ```
    # If the input contains no ignored characters, return an empty dictionary.

    # split the string down to elements in a list
    new_words = []
    split = s.lower().split()
    print(split)
    for word in split:
        new_words.append(word.replace(':','').replace(';','').replace(',','').replace('.','').replace('-','').replace('+','').replace('=','').replace('/','').replace('|','').replace('[','').replace(']','').replace('{','').replace('}','').replace('(','').replace(')','').replace('*','').replace('^','').replace('&','').replace('"','').replace('\\',''))
    print(new_words)

    if new_words == ['']:
        return word_dic

    for w in new_words:
        word_dic[w] = new_words.count(w)

    
    return word_dic

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))