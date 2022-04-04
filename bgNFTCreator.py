from PIL import Image
import random

def fr():
  print("Quel largeur voulez-vous pour votre fond ?")
  input(x_)
  print("Quel longueur voulez-vous pour votre fond ?")
  input(y_)
  print("Combien de fond voulez-vous ?")
  input(nb)

def en():
  print("What lenght do you want for your background (in pixels) ?")
  input(x_)
  print("What width do you want for your background (in pixels) ?")
  input(y_)
  print("How many background do you want ?")
  input(nb)

print("Which language do you use ? (Fr, En, more will be added soon...)") #Language chooser
input(language)
if language == "fr" or language == "French" or language == "Français":
  fr()
elif language == "en" or language == "English":
  en()

im = Image.new("RGB", (x, y), (255, 255, 255))

for x in range(0, x_):
    for y in range(0, x_):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        im.putpixel((x, y), (0, 0, 255))
