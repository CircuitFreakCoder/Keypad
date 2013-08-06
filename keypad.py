ch = ['*','#']

numbers = [1,2,3,4,5,6,7,8,9,0]

letters = [[''],['a','b','c'],['d','e','f'],['g','h','i'],
           ['j','k','l'],['m','n','o'],['p','q','r','s'],
           ['t','u','v'],['w','x','y','z']]

def cnt(s):
    current = [s[0],1]
    out = [current]
    for c in s[1:]:
        if c == current[0]:
            current[1] += 1
        else:
            current = [c, 1]
            out.append(current)
    return out

s = "22223333377779999*5*4"
len_msg = len(cnt(s))
#print len_msg
#print cnt(s)
#consec_occurence = cnt(s)[0][1]
#print consec_occurence 


output = ""

for i in range(len_msg):

    
     consec_occurence = cnt(s)[i][1]
     number_pressed = cnt(s)[i][0]
     print number_pressed

     if(number_pressed == '2' or number_pressed == '3' or number_pressed == '4' or
        number_pressed == '5' or number_pressed == '6' or number_pressed == '8'):

         if(consec_occurence % 3 == 1):
             output += letters[int(number_pressed)-1][0]
         elif(consec_occurence % 3 == 2):
             output += letters[int(number_pressed)-1][1]
         else:
             output += letters[int(number_pressed)-1][2]
             
     elif(number_pressed == '7' or number_pressed == '9'):

         if(consec_occurence % 4 == 1):
             output += letters[int(number_pressed)-1][0]
         elif(consec_occurence % 4 == 2):
             output += letters[int(number_pressed)-1][1]
         elif(consec_occurence % 4 == 3):
             output += letters[int(number_pressed)-1][2]
         else:
             output += letters[int(number_pressed)-1][3]

     elif(s[i] == '*'):
        output += number_pressed
    

print output         
