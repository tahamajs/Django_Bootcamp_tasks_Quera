def lcs(X, Y, m, n):
   L = [[None]*(n+1) for a in range(m+1)]
   for i in range(m+1):
      for j in range(n+1):
         if (i == 0 or j == 0):
            L[i][j] = 0
         elif (X[i - 1] == Y[j - 1]):
            L[i][j] = L[i - 1][j - 1] + 1
         else:
            L[i][j] = max(L[i - 1][j], L[i][j - 1])
   l = L[m][n]
   LCS = [None] * (l)
   a = m
   b = n
   while (a > 0 and b > 0):
      if (X[a - 1] == Y[b - 1]):
         LCS[l - 1] = X[a - 1]
         a = a - 1
         b = b - 1
         l = l - 1
      elif (L[a - 1][b] > L[a][b - 1]):
         a = a - 1
      else:
         b = b - 1;
   # print("LCS is ")
   # print(LCS)
   return L[m][n] , "".join(LCS)

# X = "ABSDHS"
# Y = "ABDHSP"
# m = len(X)
# n = len(Y)
# lc , stt = lcs(X, Y, m, n)
# print("Length of LCS is ")
# print(lc , stt)


X = input()
m = len(X)

k = int(input())

number = 0
all_chars = ''

# lis = []
for i in range(k):
   Y = input()
   n = len(Y)
   lc , stt = lcs(X, Y, m, n)
   if lc > number :
      number = lc
      all_chars = stt


print(all_chars)
print(number)