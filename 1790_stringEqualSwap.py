# Solution to 1790. Check if One String Swap Can Make Strings Equal
# - You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two
#     indices in a string (not necessarily different) and swap the characters at these indices.
# - Return true if it is possible to make both strings equal by performing at most one string swap on exactly
#     one of the strings. Otherwise, return false.

def areAlmostEqual(s1, s2):
    flag = False

    if s1 == s2:
        return True

    if len(s1) == len(s2):
        neededLetter1, neededLetter2 = "", ""
        numDifferences = 0

        for i in range(len(s1)):
            char1, char2 = s1[i], s2[i]
            if char1 != char2:
                numDifferences += 1

                if numDifferences == 1:
                    neededLetter1, neededLetter2 = char2, char1

                elif numDifferences == 2:
                    if neededLetter1 == char1 and neededLetter2 == char2:
                        flag = True

                elif numDifferences > 2:
                    return False

    else:
        return False

    return flag


str1, str2 = "bank", "kanb"
str3, str4 = "attack", "defend"
str5, str6 = "kelb", "kelb"
str7, str8 = "this is a big long test", "shis is a big long tett"
str9, str10 = "this is a big long test part 2", "shis is a big long tett part 3"

print(areAlmostEqual(str9, str10))