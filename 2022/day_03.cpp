#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <algorithm>
#include <numeric>
#include <vector>

const std::string PRIORITY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

int to_priority(const char &item){
    return PRIORITY.find(item) + 1;
};

char get_shared_item(const std::vector<char> first, const std::vector<char> second){
    for (auto character: first){
        if((std::find(second.begin(), second.end(), character)) != second.end()){
            return character;
        }
    };
    throw std::runtime_error("There should always be a shared item.");
};

int main(void)
{
    std::vector<char> shared_items {};
    std::ifstream infile("day_03_input.txt");
    std::string line;
    while (std::getline(infile, line))
    {
        std::vector<char> first_half {line.begin(), line.length()/2 + line.begin()};
        std::vector<char> second_half {line.length()/2 + line.begin(), line.end()};
        shared_items.push_back(get_shared_item(first_half, second_half));
    };


    std::vector<int> item_priorities {};
    std::transform(shared_items.begin(), shared_items.end(), std::back_inserter(item_priorities), to_priority);

    std::cout << "Part 1: Sum of the Priorities of Shared Items" << std::endl;
    std::cout << std::accumulate(item_priorities.begin(), item_priorities.end(), 0) << std::endl;

    std::cout << "Part 2: Sum of the Priorities of Badges (Groups of 3)" << std::endl;

}
