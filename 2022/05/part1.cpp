#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void printStacks(vector<vector<string>> stacks) {
    for (int i = 0; i < stacks.size(); i++) {
        cout << "Stack " << i + 1 << ": ";
        for (int j = 0; j < stacks[i].size(); j++) {
            cout << stacks[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    ifstream file("input.txt");
    string line;

    vector<vector<string>> stacks;
    vector<vector<int>> moves;

    bool moves_section = false;

    while (getline(file, line))
    {
        if (line.empty())
        {
            moves_section = true;
            continue;
        }

        if (line[1] == '1')
            continue;

        if (moves_section) {
            int count, from, to;
            sscanf(line.c_str(), "move %d from %d to %d", &count, &from, &to);
            moves.push_back({count, from, to});
        } else {
            if (stacks.empty()) {
                int numStacks = (line.length() + 1) / 4;
                stacks.resize(numStacks);
            }

            for (int i = 0; i < stacks.size(); i++) {
                char crate = line[i * 4 + 1];
                if (crate != ' ') {
                    vector<string> temp;
                    temp.push_back(string(1, crate));
                    for (const string& s : stacks[i]) {
                        temp.push_back(s);
                    }
                    stacks[i] = temp;
                }
            }
        }
    }

    for (vector<int> move : moves) {
        printStacks(stacks);

        int count = move[0];
        int from = move[1];
        int to = move[2];

        for (int i = 0; i < count; i++) {
            stacks[to - 1].push_back(stacks[from - 1].back());
            stacks[from - 1].pop_back();
        }
        
        cout << "--------------------------------" << endl;
    }

    for (const auto& stack : stacks) {
        if (!stack.empty()) {
            cout << stack.back();
        }
    }
    cout << endl;

    return 0;
}