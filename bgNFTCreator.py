from PIL import Image
import random

x_=0
y_=0
nb=0
language="?"

def img(x_, y_, nb):
      im = Image.new("RGB", (x_, y_), (255, 255, 255))
      
      t=0
      while t != nb:
            for x in range(0, x_):
                  for y in range(0, x_):
                        r = int(random.randint(0, 255))
                        g = int(random.randint(0, 255))
                        b = int(random.randint(0, 255))
                        im.putpixel((x, y), (r, g, b))
            t=t+1
            im.save("background " + str(t) + ".png")        

def fr():
      print("Quel largeur voulez-vous pour votre fond ?")
      x_=int(input())
      print("Quel longueur voulez-vous pour votre fond ?")
      y_=int(input())
      print("Combien de fond voulez-vous ?")
      nb=int(input())
      img(x_, y_, nb)

def en():
      print("Warning : Enter only positive ! ")
      x_=int(input("What lenght do you want for your background (in pixels) ? "))
      if x_ <= 0:
            print("Invalid number, set one upper than 0. ")
            print("To enter valid number restart the programme.")
            exit()
      else:
            print("It's ok! ")
      y_=int(input("What width do you want for your background (in pixels) ?  "))
      if y_ <= 0:
            print("Invalid number, set one upper than 0.")
            print("To enter valid number restart the programme.  ")
            exit()
      else:
            print("It's ok!")
      nb=int(input("How many background do you want ?  "))
      if nb <= 0:
            print("Invalid number, set one upper than 0.")
            print("To enter valid number restart the programme.")
            exit()
      else:
            print("It's ok!")
      img(x_, y_, nb)

print("Which language do you use ? (Fr, En, more will be added soon...)") #Language chooser
language=input()
if language == "fr" or language == "French" or language == "Français":
      fr()
elif language == "en" or language == "English":
      en()