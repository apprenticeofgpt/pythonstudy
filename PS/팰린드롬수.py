def palindrome(args):
 s=str(args)
 if s[::]==s[::-1]:
  return True
 else:
  return False