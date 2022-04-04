from PIL import Image

print("Which language do you use ? (Fr, En)") #Language chooser
input(language)
if language == "fr" or language == "French" or language == "Français":
  print("")

im = Image.new("RGB", (x, y), (255, 255, 255))
