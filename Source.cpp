#include <iostream>
#include <fstream>
using namespace std;

class figura {
protected:
	double x, y;
public:
	figura() {
		x = 0;
		y = 0;
	}
	figura(double a, double b) {
		x = a;
		y = b;
	}
	figura(const figura&z) {
		x = z.x;
		y = z.y;
	}
	virtual double lenotr(double x1, double y1, double x2, double y2) {
		return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
	}


virtual	~figura() {
	}
virtual double perimetr() = 0;
virtual	void show(){

	}

};

class triang:public figura {
protected:
	double x1, y1, x2, y2;
public:
	triang():
	figura(){
		x1 = 0;
		y1 = 0;
		x2 = 0;
		y2 = 0;
	}
	triang(double xa1, double ya1, double xa2, double ya2, double xa3, double ya3):
	figura(xa1, ya1){
		x1 = xa2;
		y1 = ya2;
		x2 = xa3;
		y2 = ya3;
	}
	triang(const triang&z){
		x = z.x;
		y = z.y;
		x1 = z.x1;
		y1 = z.y1;
		x2 = z.x2;
		y2 = z.y2;
	}
virtual ~triang() {

	}
virtual void show() {
	cout << "t";
}

	double perimetr(){
	return (figura::lenotr(x1, y1, x2, y2) + figura::lenotr(x2, y2, x, y) + figura::lenotr(x1, y1, x, y));
	}
};


class rectang :public figura {
protected:
	double x1, y1;
	public:
	rectang():
	figura(){
		x1 = 0;
		y1 = 0;
	}
	rectang(double xa1, double ya1, double xa2, double ya2) :
		figura(xa1, ya1){
		x1 = xa2;
		y1 = ya2;
	}
	rectang(const rectang& z) {
		x = z.x;
		y = z.y;
		x1 = z.x1;
		y1 = z.y1;
	}
	virtual ~rectang() {

	}
	virtual void show() {
		cout << "r";
	}
	double perimetr() {
		return(((abs(x - x1) + abs(y - y1)))*2);
	}
};


class coloredtriang :public triang {
	char colour;
public:
	coloredtriang():
		triang() {
		colour = ' ';
	}
	coloredtriang(double x1, double y1, double x2, double y2, double x3, double y3, char r) :
		triang(x1, y1, x2, y2, x3, y3) {
		colour = r;
	}
	coloredtriang(const coloredtriang& z)
	{
		x = z.x;
		x1 = z.x1;
		y = z.y;
		y1 = z.y1;
		x2 = z.x2;
		y2 = z.y2;
		colour = z.colour;
	}
	virtual ~coloredtriang() {

	}
	virtual void show() {
		cout << "tc";
	}
	double perimetr(){
		return(triang::perimetr());
	}
};



class coloredrectang :public rectang {
	char colour;
public:
	coloredrectang() :
		rectang() {
		colour = ' ';
	}
	coloredrectang(double x1, double y1, double x2, double y2, char r) :
		rectang(x1, y1, x2, y2) {
		colour = r;
	}
	coloredrectang(const coloredrectang& z)
	{
		x = z.x;
		y = z.y;
		x1 = z.x1;
		y1 = z.y1;
		colour = z.colour;
	}
	virtual ~coloredrectang() {

	}
	virtual void show() {
		cout << "rc";
	}
	double perimetr() {
		return(rectang::perimetr());
	}

};










int main() {
	ifstream in("figures.txt");
	int n;
	in >> n;
	char type[3] = "";
	//int x1, x2, x3, y1, y2, y3;
	double sum_per = 0;
	figura** a = new figura*[n];
	for (int i = 0; i < n and !in.eof(); i++) {
		in >> type;
		if (strcmp(type, "r") == 0) {
			int x1, y1, x2, y2;
			in >> x1;
			in >> y1;
			in >> x2;
			in >> y2;
			a[i] = new rectang(x1, y1, x2, y2);
		}
		else if (strcmp(type, "t") == 0) {
			int x1, y1, x2, y2, x3, y3;
			in >> x1;
			in >> y1;
			in >> x2;
			in >> y2;
			in >> x3;
			in >> y3;
			a[i] = new triang(x1, y1, x2, y2, x3, y3);
		}
		else if (strcmp(type, "rc") == 0) {
			int x1, y1, x2, y2;
			char r;
			in >> x1;
			in >> y1;
			in >> x2;
			in >> y2;
			in >> r;
			a[i] = new coloredrectang(x1, y1, x2, y2, r);
		}
		else if (strcmp(type, "tc") == 0) {
			int x1, y1, x2, y2, x3, y3;
			char r;
			in >> x1;
			in >> y1;
			in >> x2;
			in >> y2;
			in >> x3;
			in >> y3;
			in >> r;
			a[i] = new coloredtriang(x1, y1, x2, y2, x3, y3, r);
		}
		sum_per += a[i]->perimetr();

	}
	sum_per = sum_per / n;
	cout << "average perimetr is: " << sum_per << endl;
	for (int i = 0; i < n; i++) {
		/*if (a[i]->perimetr() > sum_per) {
			a[i]->show();
			cout << " with perimetr: " << a[i]->perimetr() << endl;
		}*/
		cout << a[i]->perimetr() << " ";
	}
	//5.24  10.24  4   12
	for (int i = 0; i < n; i++) {
		delete a[i];
	}
	delete a;



	return 0;
}