#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "Passport_Validator.h"

std::vector<std::string> read_in_batch_file(const std::string filename);

int main()
{
    auto passports = read_in_batch_file("input.txt");
    auto checker = PassPortValidator();

    int num_missing_cid{0}, num_valid_passports{0};

    for (auto passport : passports)
    {
        if (checker.has_required_fields(passport))
        {
            num_missing_cid++;
            if (checker.is_valid_passport(passport))
            {
                num_valid_passports++;
            }
        }
    }
    std::cout << "Missing cid (Part 1): " << num_missing_cid << std::endl;
    std::cout << "Missing cid with Validated Data (Part 2): " << num_valid_passports << std::endl;
}

std::vector<std::string> read_in_batch_file(const std::string filename)
{
    std::vector<std::string> passports;
    std::cout << "Reading Batch file: " << filename << std::endl;
    std::ifstream file(filename);
    std::string line;
    std::string passport;
    while (std::getline(file, line))
    {
        if (line.empty())
        {
            passports.push_back(passport);
            passport = "";
        }
        else
        {
            if (passport.empty())
            {
                passport = line;
            }
            else
            {
                passport += " " + line;
            }
        }
    }
    if (!passport.empty())
    {
        passports.push_back(passport);
    }
    return passports;
}
