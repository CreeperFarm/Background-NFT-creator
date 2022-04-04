from PIL import Image
import random


x_=0
y_=0
nb=0
language="?"

def fr():
      print("Quel largeur voulez-vous pour votre fond ?")
      input(x_)
      print("Quel longueur voulez-vous pour votre fond ?")
      input(y_)
      print("Combien de fond voulez-vous ?")
      input(nb)
      img()

def en():
      print("What lenght do you want for your background (in pixels) ?")
      input(x_)
      if x_ <= 0:
            print("Invalid number, set one upper than 0. ")
            print("To enter valid number restart the programme. ")
      else:
            print("It's ok! ")
      print("What width do you want for your background (in pixels) ?")
      input(y_)
      if y_ <= 0:
            print("Invalid number, set one upper than 0.")
            print("To enter valid number restart the programme.")
      else:
            print("It's ok!")
      print("How many background do you want ?")
      input(nb)
      if nb <= 0:
            print("Invalid number, set one upper than 0.")
            print("To enter valid number restart the programme.")
      else:
            print("It's ok!")
      img()

print("Which language do you use ? (Fr, En, more will be added soon...)") #Language chooser
input(language)
if language == "fr" or language == "French" or language == "Français":
      fr()
elif language == "en" or language == "English":
      en()

im = Image.new("RGB", (x_, y_), (255, 255, 255))

def img():
      t=0
      while t <= nb:
            for x in range(0, x_):
                  for y in range(0, x_):
                        r = random.randint(0, 255)
                        g = random.randint(0, 255)
                        b = random.randint(0, 255)
                        im.putpixel((x, y), (r, g, b))
      im.save("background" + t +".png")
      t=t+1