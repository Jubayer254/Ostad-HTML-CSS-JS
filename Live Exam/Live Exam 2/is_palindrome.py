def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def get_all_substrings(s):
    substrings = []
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings.append(s[i:j])
    return substrings

def show_palindromic_substrings(s):
    list_of_palindrome_chk = get_all_substrings(s)
    is_palindrome_list = []
    for i in list_of_palindrome_chk:
        if is_palindrome(i):
            is_palindrome_list.append(i)
    print(is_palindrome_list)

print(is_palindrome("madam"))
show_palindromic_substrings("madam")