from PIL import Image, ImageDraw , ImageFont
#name = input("Enter the name")
image = Image.open('certificate.jpg')

font_type = ImageFont.truetype('arial.ttf',24)
draw = ImageDraw.Draw(image)
draw.text (xy=(240,245), text="name", fill=(255,69,0), font =font_type )
  
image.save( 'certi.pdf', "PDF", resolution=100.0)


image.show()