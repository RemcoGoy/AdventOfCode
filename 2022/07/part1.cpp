#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <functional>
using namespace std;


class Content {
public:
    string name;
    int size;
    bool is_dir;
    Content(string n, int s, bool d) : name(n), size(s), is_dir(d) {}
};

class Command {
public:
    string cmd;
    string args;
    vector<Content> output;
    
    Command(string c, string a) : cmd(c), args(a) {}
};

void print_dir_structure(const map<string, vector<Content>>& dir_structure) {
    // Print directory structure
    for (const auto& dir : dir_structure) {
        cout << "Directory: " << dir.first << endl;
        for (const Content& content : dir.second) {
            cout << "  ";
            if (content.is_dir) {
                cout << "dir " << content.name;
            } else {
                cout << content.size << " " << content.name;
            }
            cout << endl;
        }
        cout << endl;
    }
}

map<string, vector<Content>> create_dir_structure(const vector<Command>& commands) {
    // Create directory structure
    map<string, vector<Content>> dir_structure;
    vector<string> current_path;

    for (const Command& cmd : commands) {
        if (cmd.cmd == "cd") {
            if (cmd.args == "/") {
                current_path.clear();
            } else if (cmd.args == "..") {
                if (!current_path.empty()) {
                    current_path.pop_back();
                }
            } else {
                current_path.push_back(cmd.args);
            }
        } else if (cmd.cmd == "ls") {
            // Build current directory path
            string dir_path = "/";
            for (const string& dir : current_path) {
                dir_path += dir + "/";
            }
            
            // Store contents in directory structure
            dir_structure[dir_path] = cmd.output;
        }
    }

    return dir_structure;
}

void print_commands(const vector<Command>& commands) {
    cout << "Commands:" << endl;
    for (const Command& cmd : commands) {
        cout << "$ " << cmd.cmd;
        if (!cmd.args.empty()) {
            cout << " " << cmd.args;
        }
        cout << endl;
        
        for (const Content& content : cmd.output) {
            if (content.is_dir) {
                cout << "dir " << content.name << endl; 
            } else {
                cout << content.size << " " << content.name << endl;
            }
        }
    }
    cout << endl;
}

// Function to calculate directory size (including subdirectories)
int calculate_dir_size(const string& dir_path, const map<string, vector<Content>>& dir_structure) {
    int total_size = 0;
    
    // Sum up all files in current directory
    for (const Content& content : dir_structure.at(dir_path)) {
        if (!content.is_dir) {
            total_size += content.size;
        } else {
            // For directories, recursively calculate size of subdirectory
            string subdir_path = dir_path + content.name + "/";
            total_size += calculate_dir_size(subdir_path, dir_structure);
        }
    }
    
    return total_size;
}

int main() {
    ifstream file("input.txt");
    string line;

    bool output_mode = false;

    vector<Command> commands;

    while (getline(file, line)) {
        if (line[0] == '$') {
            string cmd = line.substr(2, 2);
            string args = line.length() > 5 ? line.substr(5) : "";
            commands.push_back(Command(cmd, args));
            output_mode = (cmd == "ls");
        } else if (output_mode) {
            Content content("", 0, false);
            if (line.substr(0, 3) == "dir") {
                content.name = line.substr(4);
                content.is_dir = true;
            } else {
                size_t space_pos = line.find(' ');
                content.size = stoi(line.substr(0, space_pos));
                content.name = line.substr(space_pos + 1);
            }
            commands.back().output.push_back(content);
        }
    }

    file.close();

    map<string, vector<Content>> dir_structure = create_dir_structure(commands);

    long long sum = 0;

    // Calculate and print sizes of all directories
    for (const auto& dir : dir_structure) {
        int size = calculate_dir_size(dir.first, dir_structure);
        cout << "Directory " << dir.first << " size: " << size << endl;
        if (size <= 100000) {
            sum += size;
        }
    }

    cout << "Sum of directories with size <= 100000: " << sum << endl;

    return 0;
}