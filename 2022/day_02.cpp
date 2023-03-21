#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>

using namespace std;

enum Move // Sadly you can't iterate over an enum as easily as you can in python. :(
{
    Rock = 1,
    Paper = 2,
    Scissors = 3,
};

enum Score
{
    Loss = 0,
    Draw = 3,
    Win = 6,
};

// If this was in python, this should just be a call to a dictionary.  How to use map with enums?
Move get_move_from_symbol(char symbol)
{
    switch (symbol)
    {
    case 'A':
    case 'X':
        return Rock;
    case 'B':
    case 'Y':
        return Paper;
    case 'C':
    case 'Z':
        return Scissors;
    default:
        throw runtime_error("Turn back now.");
    };
};

// If this was in python, this should just be a call to a dictionary.  How to use map with enums?
Score get_outcome_from_symbol(char symbol)
{
    switch (symbol)
    {
    case 'X':
        return Loss;
    case 'Y':
        return Draw;
    case 'Z':
        return Win;
    default:
        throw runtime_error("Turn back now.");
    };
};

int play_round(Move theirs, Move mine)
{
    int results = 0;
    switch (theirs)
    {
    case Rock:
        if (mine == Paper)
            results = Win;
        else if (mine == Rock)
            results = Draw;
        else
        {
            results = Loss;
        }
        break;
    case Paper:
        if (mine == Scissors)
            results = Win;
        else if (mine == Paper)
            results = Draw;
        else
        {
            results = Loss;
        }
        break;
    case Scissors:
        if (mine == Rock)
            results = Win;
        else if (mine == Scissors)
            results = Draw;
        else
        {
            results = Loss;
        }
        break;
    default:
        throw runtime_error("Dynamite not supported.");
    };
    return results;
};

int main()
{
    constexpr Move MOVES[] = {Rock, Paper, Scissors};
    int total_score_move = 0;
    int total_score_outcome = 0;

    ifstream infile("day_02_input.txt");
    std::string line_in_file;
    while (std::getline(infile, line_in_file))
    {
        char their_symbol = line_in_file[0];
        char my_symbol = line_in_file[2];

        Move their_move = get_move_from_symbol(their_symbol);
        Move my_move = get_move_from_symbol(my_symbol);

        // Part 1 - Second move is your move.
        total_score_move += play_round(their_move, my_move) + my_move;

        // Part 2 - Second move is outcome x: lose, y: draw and z: win
        Score round_results = get_outcome_from_symbol(my_symbol);
        for (auto move : MOVES)
        {
            if (play_round(their_move, move) == (int)round_results)
            {
                total_score_outcome += (int)round_results + (int)move;
                break;
            }
        }
    }
    cout << "Part 1: Total Score by Move: " << total_score_move << endl;
    cout << "Part 2: Total Score by Outcome: " << total_score_outcome << endl;

    return 0;
}
