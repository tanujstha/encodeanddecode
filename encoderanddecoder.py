import random
def secret_code():
    ab = 'abcdefghijklmnopqrstuvwxyz'
    mk = 'mnbvcxzaqweopkjhgfds123456'
    

    print("Welcome to the code generator")

    code = input("enter the 9 letter secret code encode: ")
    if len(code) > 4 :
            
        first = code[0:-8]
        last = code[1:10]
        total =  last + first
        nak = "anjdbsine"
        encripted = ''.join(random.choice(ab) for _ in range(6))
        encripted2 = ''.join(random.choice(mk) for _ in range (6))
        nome = encripted + total + encripted2
        print(nome)
  
        

    else:
        mouth = code[::-1]
        print(mouth)


def to_decode():


# secret code = "Antidisestablish"
    
    to_decode = input("enter the secret code ").lower()
    if to_decode == "anti":
        print("you have successfully passed")
        ab = input("enter the code to decode")
        nam = ab[6:-6]
        op = nam[8:] + nam[:-1]
        

        
        print(op)
    else: 
        print("incorrect code")
    
        
       

        
        
                    






secret_code()
to_decode()

