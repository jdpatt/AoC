#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>

using namespace std;

enum Move
{
    Rock,
    Paper,
    Scissors,
};
enum Score
{
    Win = 6,
    Loss = 0,
    Draw = 3,
};

std::map<const Move, const char *> MOVE_MAPPING{
    {Rock, 'A'},
    {Paper, 'B'},
    {Scissors, 'C'},
    {Rock, 'X'},
    {Paper, 'Y'},
    {Scissors, 'Z'}
};

Score play_rock_paper_scissors(Move &theirs, Move &mine)
{
    switch (theirs)
    {
    case Rock:
        if (mine == Paper)
            return Win;
        else if (mine == Rock)
            return Draw;
    case Paper:
        if (mine == Scissors)
            return Win;
        else if (mine == Paper)
            return Draw;
    case Scissors:
        if (mine == Rock)
            return Win;
        else if (mine == Scissors)
            return Draw;
    };
    return Loss;
}

int main()
{
    int total_score = 0;

    ifstream infile("day_02_input.txt");
    std::string line_in_file;
    while (std::getline(infile, line_in_file))
    {
        std::stringstream ss(line_in_file);
        Move theirs = Rock, mine = Rock;
        // ss >> theirs, mine;
        total_score += (int)play_rock_paper_scissors(theirs, mine);
    }
    cout << "Part 1: Total Score: " << total_score << endl;

    return 0;
}
