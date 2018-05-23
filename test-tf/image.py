from PIL import Image
img_path  ='./01.jpg'
img = Image.open(img_path)
size = img.size
print(size[0])