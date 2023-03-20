#include <algorithm>
#include <numeric>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main(void)
{
    vector<int> elves;
    int current_calories = 0;

    ifstream infile("day_01_input.txt");
    std::string line_in_file;
    while (std::getline(infile, line_in_file))
    {
        if (line_in_file.empty())
        {
            elves.push_back(current_calories);
            current_calories = 0;
        }
        else
        {

            current_calories += std::stoi(line_in_file);
        }
    }

    std::sort(elves.begin(), elves.end());
    cout << "Part 1: Elf with the most calories: " << elves.back() << endl;

    // Let it infer the op and just sum ints.
    cout << "Part 2: Top Three Elves: " << std::accumulate(elves.end() - 3, elves.end(), 0) << endl;
    return 0;
}
