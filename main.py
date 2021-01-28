from PIL import Image

img = Image.open('tomato.png')  # image extension *.png,*.jpg
new_width = 250
new_height = 250
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('tomato.png')  # format may what you want *.png, *jpg, *.gif
