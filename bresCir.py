from PIL import Image,ImageColor

im = Image.new('1',(1000,1000))

def drawCircle(X,Y,P,Q):
	im.putpixel((X+P,Y+Q),ImageColor.getcolor('red','1'))
	im.putpixel((X-P,Y+Q),ImageColor.getcolor('red','1'))
	im.putpixel((X+P,Y-Q),ImageColor.getcolor('red','1'))
	im.putpixel((X-P,Y-Q),ImageColor.getcolor('red','1'))
	im.putpixel((X+Q,Y+P),ImageColor.getcolor('red','1'))
	im.putpixel((X-Q,Y+P),ImageColor.getcolor('red','1'))
	im.putpixel((X+Q,Y-P),ImageColor.getcolor('red','1'))
	im.putpixel((X-Q,Y-P),ImageColor.getcolor('red','1'))


xCenter = 500
yCenter = 500
radius = 400
p = 0
q = radius
decisionParam = 3 - 2 * radius

drawCircle(xCenter,yCenter,p,q)

while(q >= p):
	p = p+1
	if decisionParam > 0:
		q = q-1
		decisionParam = decisionParam + 4*(p-q) + 10
	else:
		decisionParam = decisionParam + 4 * p +6

	drawCircle(xCenter,yCenter,p,q)
	

im.save('bresenhamCircle.jpg')
