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

    int batch_size = 14;

    for (int i = 0; i < line.length() - batch_size; i++) {
        string batch = line.substr(i, batch_size);

        bool unique_batch = true;
        
        for (int j = 0; j < batch_size; j++) {
            for (int k = j + 1; k < batch_size; k++) {
                if (batch[j] == batch[k]) {
                    unique_batch = false;
                    break;
                }
            }
        }

        if (unique_batch) {
            cout << i + batch_size << endl;
            break;
        }
    }

    return 0;
}