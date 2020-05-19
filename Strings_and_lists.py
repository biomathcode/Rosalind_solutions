"""
Given: A string s of length at most 200 letters and 4 integers a, b, c and d
Return:The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
"""

SampleText = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."

while True:
    try:
        f1, f2, f3, f4 = [ int(x) for x in input("Enter the four indices: ").split()]
        break
    except ValueError:
        print('Please give four indices!!!! ')
        
Text= input("please give the text here")


print("this first indices is", f1)
print("the second indices is ", f2)

def Output_function(Text, f1 , f2 , f3, f4):
    if Text is not None:
        return print(Text[f1:f2 + 1] + " " + Text[f3:f4 + 1])
    else:
        return print(SampleText[f1:f2 + 1] + " " + SampleText[f3:f4 + 1])

    

Output_function(Text, f1, f2, f3, f4)
