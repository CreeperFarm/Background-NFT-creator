from PIL import Image
import random

def img(x_, y_, nb, language):
      im = Image.new("RGB", (x_, y_), (255, 255, 255))
      
      t=0
      while t != nb:
            rbase = int(random.randint(0, 255))
            gbase = int(random.randint(0, 255))
            bbase = int(random.randint(0, 255))
            for x in range(0, x_):
                  for y in range(0, x_):
                        r = int(random.randint(rbase-10, rbase+10))
                        g = int(random.randint(gbase-10, gbase+10))
                        b = int(random.randint(bbase-10, bbase+10))
                        im.putpixel((x, y), (r, g, b))
            t=t+1
            im.save("smoothbackground " + str(t) + ".png")
      if language == "fr" or language == "French" or language == "Français":
            if nb == 1:
                  print("Votre image a correctement été créer.")
            else:
                  print("Vos " + str(nb) + "images ont correctement été créer.")
      elif language == "en" or language == "English":
            if nb == 1:
                  print("Your image have been correctly created.")
            else:
                  print("Your " + str(nb) + " images have been correctly created.")

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

print("Which language do you use ? (Fr, En, more will be added soon...)") #Language chooser
language=input()
if language == "fr" or language == "French" or language == "Français":
      fr(language)
elif language == "en" or language == "English":
      en(language)
