from PIL import Image

def bilde():

  datne = "30.11./suns.jpg"

  with Image.open(datne) as im:

    print(datne, im.format, f"{im.size}x{im.mode}")
    im.show()

    izmers = (100,100)

    im.thumbnail(izmers)

    im.save("30.11./maza_bilde.jpg", im.format)
    




bilde()