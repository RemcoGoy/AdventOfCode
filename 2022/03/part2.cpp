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

    vector<string> group;
    while (getline(file, line)) {
        group.push_back(line);
        if (group.size() == 3) {
            rucksacks.push_back(group);
            group.clear();
        }
    }

    file.close();

    vector<char> common_items;

    for (vector<string> group : rucksacks) {
        vector<char> common_in_group;

        for (char item : group[0]) {
            if (group[1].find(item) != string::npos && group[2].find(item) != string::npos) {
                if (find(common_in_group.begin(), common_in_group.end(), item) == common_in_group.end()) {
                    common_in_group.push_back(item);
                }
            }   
        }

        common_items.insert(common_items.end(), common_in_group.begin(), common_in_group.end());
    }

    int sum = 0;
    for (char item : common_items) {
        int item_value = (item >= 'a' && item <= 'z') ? (item - 'a' + 1) : (item - 'A' + 27);
        sum += item_value;
    }

    cout << sum << endl;

    return 0;
}