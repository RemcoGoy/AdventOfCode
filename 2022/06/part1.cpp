#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;


int main()
{
    ifstream file("input.txt");
    string line;

    getline(file, line);

    file.close();

    for (int i = 0; i < line.length() - 3; i++) {
        string batch = line.substr(i, 4);

        bool unique_batch = true;
        
        for (int j = 0; j < 4; j++) {
            for (int k = j + 1; k < 4; k++) {
                if (batch[j] == batch[k]) {
                    unique_batch = false;
                    break;
                }
            }
        }

        if (unique_batch) {
            cout << i + 4 << endl;
            break;
        }
    }

    return 0;
}