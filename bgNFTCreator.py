from PIL import Image
import random

def img(x_, y_, nb, language):
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
      print("Your " + str(nb) + " images have been created.")

def fr(language):
      x_=int(input("Quel largeur voulez-vous pour votre fond ?  -->"))
      if x_ <= 0:
            print("Nombre Invalid, entrer en un supérieur à 0.")
            print("Pour entrer une valeur correct, redémarrer le programme.")
            exit()
      else:
            print("C'est bon!")
      y_=int(input("Quel longueur voulez-vous pour votre fond ?  -->"))
      if y_ <= 0:
            print("Nombre Invalid, entrer en un supérieur à 0.")
            print("Pour entrer une valeur correct, redémarrer le programme.")
            exit()
      else:
            print("C'est bon!")
      nb=int(input("Combien de fond voulez-vous ?  -->"))
      if nb <= 0:
            print("Nombre Invalid, entrer en un supérieur à 0.")
            print("Pour entrer une valeur correct, redémarrer le programme.")
            exit()
      else:
            print("C'est bon!")
      img(x_, y_, nb, language)

def en(language):
      print("Warning : Enter only positive ! ")
      x_=int(input("What lenght do you want for your background (in pixels) ?  -->"))
      if x_ <= 0:
            print("Invalid number, set one upper than 0. ")
            print("To enter valid number restart the programme.")
            exit()
      else:
            print("It's ok! ")
      y_=int(input("What width do you want for your background (in pixels) ?  -->"))
      if y_ <= 0:
            print("Invalid number, set one upper than 0.")
            print("To enter valid number restart the programme.  ")
            exit()
      else:
            print("It's ok!")
      nb=int(input("How many background do you want ?  -->"))
      if nb <= 0:
            print("Invalid number, set one upper than 0.")
            print("To enter valid number restart the programme.")
            exit()
      else:
            print("It's ok!")
      img(x_, y_, nb, language)

language = input("Which language do you use ? (Fr, En, more will be added soon...)  -->") #Language chooser
if language == "fr" or language == "French" or language == "Français":
      fr(language)
elif language == "en" or language == "English":
      en(language)
