#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    double x, y, y1, y2, r33; //Ініціалізація змінної х
    const double pi = 3.14;
	cout << "\nВведіть х : ";
	cin >> x;//Присвоєння значення змінній х
	r33 = 33.0 * pi / 180.0;
    y1 = exp(x + 1) * sqrt(fabs(2 * x - cos(x + r33) - 25)) ;
    y2 = pow(sin(pow(x, 2)), 1.0 / 3.0) * (log(fabs(pow(x, 3))) / log(5)) ;
	y = y1/y2 ; //Вирішення задачі
	cout << "y дорівнює : " << y;
    return 0;
}
