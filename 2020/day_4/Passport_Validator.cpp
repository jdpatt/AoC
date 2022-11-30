#include "Passport_Validator.h"

#include <algorithm>
#include <regex>
#include <sstream>
#include <string>
#include <vector>

bool PassPortValidator::has_required_fields(const std::string passport) const
{
    for (auto field : this->REQUIRED_FIELDS)
    {
        if (passport.find(field) == std::string::npos)
        {
            return false;
        }
    }
    return true;
}

bool PassPortValidator::is_valid_passport(const std::string passport) const
{
    std::istringstream ss(passport);
    std::string key_value_pair;
    while (std::getline(ss, key_value_pair, ' '))
    {
        std::istringstream ss2(key_value_pair);
        std::string key, value;
        std::getline(ss2, key, ':');
        ss2 >> value;
        if (!this->is_valid_field(key, value))
        {
            return false;
        }
    }
    return true;
}

bool PassPortValidator::is_valid_field(const std::string field, const std::string value) const
{
    if (field == "byr")
    {
        return this->validate_birth_year(value);
    }
    else if (field == "iyr")
    {
        return this->validate_issue_year(value);
    }
    else if (field == "eyr")
    {
        return this->validate_expiration_year(value);
    }
    else if (field == "hgt")
    {
        return this->validate_height(value);
    }
    else if (field == "hcl")
    {
        return this->validate_hair_color(value);
    }
    else if (field == "ecl")
    {
        return this->validate_eye_color(value);
    }
    else if (field == "pid")
    {
        return this->validate_pid(value);
    }
    else
    {
        return true;
    }
}

// byr (Birth Year) - four digits; at least 1920 and at most 2002.
bool PassPortValidator::validate_birth_year(const std::string value) const
{
    int year{std::stoi(value)};
    if (year >= 1920 && year <= 2002)
    {
        return true;
    }
    return false;
}

// iyr (Issue Year) - four digits; at least 2010 and at most 2020.
bool PassPortValidator::validate_issue_year(const std::string value) const
{
    int year{std::stoi(value)};
    if (year >= 2010 && year <= 2020)
    {
        return true;
    }
    return false;
}

// eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
bool PassPortValidator::validate_expiration_year(const std::string value) const
{
    int year{std::stoi(value)};
    if (year >= 2020 && year <= 2030)
    {
        return true;
    }
    return false;
}

bool PassPortValidator::validate_height(const std::string value) const
{
    std::smatch regex_match;
    if (std::regex_match(value, regex_match, std::regex("(\\d+)(cm|in)")))
    {
        int height{std::stoi(regex_match[1])};
        std::string units{regex_match[2]};

        if (units == "cm" && height >= 150 && height <= 193)
        {
            return true;
        }
        if (units == "in" && height >= 59 && height <= 76)
        {
            return true;
        }
    }
    return false;
}

bool PassPortValidator::validate_hair_color(const std::string value) const
{
    if ((value.length() == 7) && std::regex_match(value, std::regex("#[a-f0-9]{6}")))
    {
        return true;
    }
    return false;
}

bool PassPortValidator::validate_eye_color(const std::string value) const
{
    std::vector<std::string> eye_colors{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};

    if (std::find(eye_colors.begin(), eye_colors.end(), value) != eye_colors.end())
    {
        return true;
    }
    return false;
}

bool PassPortValidator::validate_pid(const std::string value) const
{
    if (value.length() == 9 && std::regex_match(value, std::regex("\\d{9}")))
    {
        return true;
    }
    return false;
}
