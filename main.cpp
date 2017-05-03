#include <iostream>
#include <cmath>
using namespace std;

int main() {

    int n, x, i;

    cout << "Enter a # ";
    cin >> n;

    for(x=2; x<=n; x++)
    {
        i = int(floor(sqrt(x)));
        while (i<=x)
        {
            if(x%i==0)

                break;

            if(i == (x -1))
                {
                    cout << x << endl;
                }
             i++;
        }
    }
    return 0;
}