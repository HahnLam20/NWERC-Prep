#used for finding patterns within text or strings

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0]*M