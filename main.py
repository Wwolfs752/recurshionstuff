
def is_palindrome(string_to_check):
    if len(string_to_check) == '':
        return True
    if len(string_to_check) == 1:
        return True
    if string_to_check[0] != string_to_check[-1]:
        return False
    return is_palindrome(string_to_check[1:-1])


def main():
    maybe_palindrome = input("What to check for palindrome")
    answer = is_palindrome(maybe_palindrome)
    if answer:
        print("Yes this is a palindrome")
    else:
        print("Nope!")


main()
