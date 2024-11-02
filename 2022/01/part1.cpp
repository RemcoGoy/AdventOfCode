#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string line;
    ifstream file("input.txt");

    vector<vector<int>> calories_by_elf;
    vector<int> current_elf;
    
    while (getline(file, line)) {
        if (line.empty()) {
            calories_by_elf.push_back(current_elf);
            current_elf.clear();
            continue;
        }
        current_elf.push_back(stoi(line));
    }
    calories_by_elf.push_back(current_elf);
    file.close();
    
    int max_calories = 0;
    for (vector<int> elf : calories_by_elf) {
        int sum = 0;
        for (int calorie : elf) {
            sum += calorie;
        }
        max_calories = max(max_calories, sum);
    }
    cout << max_calories << endl;
    return 0;
}
