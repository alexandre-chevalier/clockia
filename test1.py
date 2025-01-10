import time

def afficher_heure():
  s = 0
  m = 0
  h = 0

  if s == 60:
     m +=1 
 
     if m == 60:
        h +=1

 
  print(f"{h:02}, {m:02}, {s:02}",end='\r')
  time.sleep(1)

afficher_heure()


