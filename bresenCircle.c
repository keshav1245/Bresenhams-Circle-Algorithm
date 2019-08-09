#include<stdio.h>
#include<graphics.h>

void drawCircle(int X,int Y,int P,int Q){
	putpixel(X+P,Y+Q,RED);
	putpixel(X-P,Y+Q,RED);
	putpixel(X+P,Y-Q,RED);
	putpixel(X-P,Y-Q,RED);
	putpixel(X+Q,Y+P,RED);
	putpixel(X-Q,Y+P,RED);
	putpixel(X+Q,Y-P,RED);
	putpixel(X-Q,Y-P,RED);
}


int main(){

	int gd = DETECT,gm;
	initgraph(&gd,&gm,"");
	
	int xCenter = 300,yCenter = 300,radius = 100,decisionParam;
	int p =0, q = radius;

	decisionParam = 3 - 2 *radius;

	drawCircle(xCenter,yCenter,p,q);

	while(q >= p){
		p++;
		if(decisionParam > 0){
			q--;
			decisionParam = decisionParam + 4*(p-q) +10;
		}else{
			decisionParam =decisionParam + 4*p + 6;			
		}		
		
		drawCircle(xCenter,yCenter,p,q);
		//delay(100);	
	}
	
	//delay(5000);	
	return 0;	

}
