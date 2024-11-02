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

    vector<int> total_calories;
    for (vector<int> elf : calories_by_elf) {
        int sum = 0;
        for (int calorie : elf) {
            sum += calorie;
        }
        total_calories.push_back(sum);
    }

    sort(total_calories.begin(), total_calories.end(), greater<int>());
    for (int calories : total_calories) {
        cout << calories << " ";
    }
    cout << endl;
    cout << total_calories[0] + total_calories[1] + total_calories[2] << endl;

    return 0;
}
