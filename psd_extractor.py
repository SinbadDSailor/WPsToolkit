from psd_tools import PSDImage

def extract():

    img_path = input("Enter PSD file path: ")
    psd = PSDImage.open(img_path)

    for layer in psd.descendants():
        if layer.kind == "smartobject":
            layer.compose().save(layer.name + ".png")
            print(layer.name)
