from PIL import Image,ImageFilter


#get every frame of thr gif file
im=Image.open("a.gif")
cnt=0
im.seek(1)
try:
    while 1:
        im.seek(im.tell()+1)
        newimage = Image.new('RGB', im.size)
        newimage.paste(im)
        newimage.save("%d.jpg"%(cnt))
        cnt+=1
except EOFError:
    pass


#Exchange the color(RGB) of an image
im1=Image.open("b.jpg")
x,y=im1.size
for i in range(x):
    for k in range(y):
        r,g,b=im1.getpixel((i,k))
        if b>r and b>g:
            b=0
            r=0
            g=0
        im1.putpixel((i,k),(r,g,b))
        
im1.save("exchanged_image.jpg")


#Get the contour of an image
im2=Image.open("c.png")
im2.filter(ImageFilter.EDGE_ENHANCE)
im2.filter(ImageFilter.FIND_EDGES).save("edge_enhance.png")
