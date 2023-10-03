#include <iostream>
#include <cmath>// підключення бібліотеки математичних функцій
using namespace std;

int main ()
{

	// Integer1.	Дано відстань L в сантиметрах. 
	// Використовуючи операцію ділення, 
	// визначити кількість повних метрів в ньому 
	// (1 метр = 100 см).
	
	cout <<"Integer1." << endl;
	int L, res; // декларація цілих змінних
	//введення данних
	cout << endl <<"L (sm) =";	cin >> L;
	// підрахунок
	res = L / 100;
	// виведення результату
	cout <<"L (m) =" << res << endl;

	// Boolean1. Дано ціле число A.
	// Перевірити істинність висловлювання: «Число A є додатнім».
	cout <<"\n Boolean1. \n";
	int A;
	//введення данних
	cout <<"\n A =";	
	cin >> A;
	// підрахунок
	bool is_pos = A > 0; // визначення ЛОГІЧНОЇ змінної
	// виведення результату
	cout << "A is positive:" << is_pos << endl;

	// y = ... (tab.3 N1)
	cout <<"\n Math.1. \n";
	const double pi = 3.141592; // визначення дійсної константи

	double x, num, denom, y; // декларація дійсних змінних
	//введення данних
	cout <<"\n Real argument x =";	
	cin >> x;
	// підрахунок
	num = pow (log (x * x + cos (37 * pi / 180)), 2); // чисельник
	denom = pow (sin (x * x), 2) + sqrt (fabs (1 - 2 * cos (x) - pow (sin (x * x), 2))); // знаменник
   y = num / denom;
	// виведення результату
	cout <<"\n Function y =" << y << endl;


	system ("Pause"); // затримка консольного вікна
	return 0;
}
