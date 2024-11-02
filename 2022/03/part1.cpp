#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string line;
    ifstream file("input.txt");

    vector<vector<string>> rucksacks;

    while (getline(file, line)) {
        rucksacks.push_back(vector<string>{line.substr(0, line.length() / 2), line.substr(line.length() / 2)});
    }

    file.close();

    vector<char> common_items;

    for (vector<string> rucksack : rucksacks) {
        string first_compartment = rucksack[0];
        string second_compartment = rucksack[1];

        vector<char> current_common_items;

        for (char item : first_compartment) {
            if (second_compartment.find(item) != string::npos) {
                if (find(current_common_items.begin(), current_common_items.end(), item) == current_common_items.end()) {
                    current_common_items.push_back(item);
                }
            }
        }

        common_items.insert(common_items.end(), current_common_items.begin(), current_common_items.end());
    }

    int sum = 0;
    for (char item : common_items) {
        int item_value = (item >= 'a' && item <= 'z') ? (item - 'a' + 1) : (item - 'A' + 27);
        sum += item_value;
    }

    cout << sum << endl;

    return 0;
}