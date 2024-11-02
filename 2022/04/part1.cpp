#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

std::vector<int> stringToRange(const std::string& str) {
    std::vector<int> results;
    std::stringstream ss(str);
    int start, end;
    char dash;

    if (ss >> start >> dash >> end && dash == '-') {
        for (int i = start; i <= end; ++i) {
            results.push_back(i);
        }
    } else {
        std::cerr << "Invalid input string format." << std::endl;
    }

    return results;
}

bool isRangeWithin(const std::vector<int>& range1, const std::vector<int>& range2) {
    if (range1.size() > range2.size()) {
        return false;
    }

    auto it = search(range2.begin(), range2.end(), range1.begin(), range1.end());

    return (it != range2.end());
}

int main() {
    string line;
    ifstream file("input.txt");

    vector<vector<vector<int>>> pairs;

    while (getline(file, line)) {
        string firstRange = line.substr(0, line.find(","));
        string secondRange = line.substr(line.find(",") + 1);
        pairs.push_back({stringToRange(firstRange), stringToRange(secondRange)});
    }

    file.close();

    int total = 0;

    for (vector<vector<int>> pair : pairs) {
        vector<int> range1 = pair[0];
        vector<int> range2 = pair[1];

        if (isRangeWithin(range1, range2) || isRangeWithin(range2, range1)) {
            total += 1;
        }
    }

    cout << total << endl;

    return 0;
}