import time

def afficher_heure(h, m, s):
 print(f"{h:02}, {m:02}, {s:02}",end='\r') #voir pour flush=True?

def heure_alarme(h, m, s):
    h = int(input("rentres les heures: "))
    m = int(input("rentres les minutes: "))
    s = int(input("rentres les secondes: "))
            
    return(h, m, s)
   

def main(): 
  s = 0
  m = 0
  h = 0

  while True:
    s += 1

    if s == 60:
        s = 0
        m += 1 
 
    if m == 60:
        m = 0
        h += 1
     
        

        afficher_heure(h, m, s)


     
        heure_alarme(h, m, s)
    
        if heure_alarme == afficher_heure:
          print("Alarme!!!")
          break


        time.sleep(1)
main() 

   


