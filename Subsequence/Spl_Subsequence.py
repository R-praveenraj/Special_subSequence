#You have given a string A having Uppercase English letters.
#You have to find how many times subsequence "AG" is there in the given string.

#Input   A = "ABCGAG"     Output  3


def Subsequence(string):
    count =0
    count2=0
    for i in string:
        if i=="A":
            count+=1
        elif i=="G":
            count2+=1
    if count==count2:
        return count
    else:
        return min(count,count2)

string="ABCGAG"
print(Subsequence(string))