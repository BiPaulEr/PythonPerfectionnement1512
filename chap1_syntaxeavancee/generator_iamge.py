import os
from PIL import Image

def generator_image(dossier):
    liste_image = [os.path.join(dossier, path) for path in os.listdir(dossier) if path.endswith(".jpg")]
    for path in liste_image:
        yield Image.open(path)
dossier = "C:/Users/PaulE/Documents/DataSet/AbstractArt"

#print(liste_image)          

for index, image in enumerate(generator_image(dossier)):
    name = str(index).zfill(3)+".jpg"
    image.save(os.path.join(dossier, "test", name))