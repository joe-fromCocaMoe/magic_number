x= [xx for xx in range(1,64)]
num_i = [i for i in range(1,64,2)]
num_ii = x[1::16]+ x[2::16]+ x[5::16]+ x[6::16]+ \
         x[9::16]+ x[10::16]+ x[13::16]+ x[14::16]
num_ii.sort()
num_iii= x[3::16]+ x[4::16]+ x[5::16]+ x[6::16]+ \
         x[11::16]+ x[12::16]+ x[13::16]+ x[14::16]
num_iii.sort()
num_iv=  x[7::16]+ x[8::16]+ x[9::16]+ x[10::16]+ \
        x[11::16]+ x[12::16]+ x[13::16]+ x[14::16]
num_iv.sort()
num_v= x[15::32]+ x[16::32]+ x[17::32]+ x[18::32]+ \
       x[19::32]+ x[20::32]+ x[21::32]+ x[22::32]+ \
       x[23::32]+ x[24::32]+ x[25::32]+ x[26::32]+ \
       x[27::32]+ x[28::32]+ x[29::32]+ x[30::32]
num_v.sort()
num_vi= [x for x in range(32,64)]
num_lists=[num_i,num_ii,num_iii,num_iv,num_v,num_vi]
addition_num= [1,2,4,8,16,32]
start_end= ["Think of a number between 1 and 63","I think the number you thought of was ..."]
intro= ["Is your number in the group of numbers below?",
        "Is your number in this group of numbers ?","Is your number in this third group of numbers ?",
        "Half way there. Is your number in this group of numbers ?",
        "One more after this one. Is your number in this group of numbers ?",
        "Last one. Is your number in this group of numbers ?"]
def format_list(xx):    
    for a,b,c,d,e,f,g,h in zip(xx[::8],xx[1::8],xx[2::8],xx[3::8],xx[4::8],xx[5::8],xx[6::8],xx[7::8]):
        print('{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<}'.format(a,b,c,d,e,f,g,h))
    print('-'*62)
def main():    
    count=0
    your_guess= 0
    print(start_end[0])
    ready= input('are you ready?(enter to quit or any key)')
    if ready:
        while count < 6:
            print(intro[count])    
            format_list(num_lists[count])
            reply = input("y/n ?")
            if reply == "y" :
                your_guess += addition_num[count]
            count +=1
    print(start_end[1] + str(your_guess))
    replay= input('Play again? (enter to quit or any key)')
    if replay:        
        main()
if __name__ == '__main__':
    main()       
