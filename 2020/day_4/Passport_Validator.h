#ifndef _PASSPORT_VALIDATOR_H
#define _PASSPORT_VALIDATOR_H

#include <string>
#include <vector>


class PassPortValidator
{
private:
    std::vector<std::string> REQUIRED_FIELDS
    {
        "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
    };
    bool validate_birth_year( const std::string value ) const;
    bool validate_issue_year( const std::string value ) const;
    bool validate_expiration_year( const std::string value ) const;
    bool validate_height( const std::string value ) const;
    bool validate_hair_color( const std::string value ) const;
    bool validate_eye_color( const std::string value ) const;
    bool validate_pid( const std::string value ) const;
public:
    bool has_required_fields( const std::string passport ) const;
    bool is_valid_passport( const std::string passport ) const;
    bool is_valid_field( const std::string field, const std::string value ) const;
};

#endif // _PASSPORT_VALIDATOR_H
