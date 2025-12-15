import os
from PIL import Image

dossier = "C:/Users/PaulE/Documents/DataSet/AbstractArt"

liste_image = [os.path.join(dossier, path) for path in os.listdir(dossier) if path.endswith(".jpg")]
#print(liste_image)          

images = [Image.open(path) for path in liste_image]
for index, image in enumerate(images):
    name = str(index).zfill(3)+".jpg"
    image.save(os.path.join(dossier, "test", name))