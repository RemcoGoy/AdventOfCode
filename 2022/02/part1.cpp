#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main() {
    string line;
    ifstream file("input.txt");

    vector<vector<string>> games;

    while (getline(file, line)) {
        if (!line.empty()) {
            string opponent = line.substr(0, line.find(' '));
            string player = line.substr(line.find(' ') + 1);
            games.push_back({opponent, player});
        }
    }

    file.close();

    map<string, string> opponent_moves = {
        {"A", "Rock"},
        {"B", "Paper"}, 
        {"C", "Scissors"}
    };

    map<string, string> player_moves = {
        {"X", "Rock"},
        {"Y", "Paper"},
        {"Z", "Scissors"}
    };

    map<string, string> beats = {
        {"Rock", "Scissors"},
        {"Paper", "Rock"},
        {"Scissors", "Paper"}
    };

    map<string, int> move_scores = {
        {"Rock", 1},
        {"Paper", 2},
        {"Scissors", 3}
    };

    int score = 0;
    for (vector<string> game : games) {
        string opponent = game[0];
        string player = game[1];

        string opponent_move = opponent_moves[opponent];
        string player_move = player_moves[player];

        score += move_scores[player_move];

        if (beats[player_move] == opponent_move) {
            score += 6;
        } else if (player_move == opponent_move) {
            score += 3;
        }
    }

    cout << score << endl;
    return 0;
}