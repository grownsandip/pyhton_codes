def isPalindrome(s):
    n=len(s)
    for i in range(n):
        if(s[i]!=s[n-i-1]):
            return False
    return True
    
def main():
    s=input("Enter a string as your wish:")
    if(isPalindrome(s)):
        print("The string is palindrome")
    else:
        print("The string is not palindrome")

if __name__=="__main__":
    main()