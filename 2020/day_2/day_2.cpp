// Day 1
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

bool is_valid_password_for_sled_rental( const std::string password_and_policy );
bool is_valid_password_for_toboggan( const std::string password_and_policy );

int main()
{
    std::string filename {"input.txt"};
    std::cout << "Reading Password File: " << filename << std::endl;
    std::ifstream file( filename );

    int sled_valid_passwords {0};
    int toboggan_valid_passwords {0};
    std::string password_and_policy;
    while( std::getline( file, password_and_policy ) )
    {
        if( is_valid_password_for_sled_rental( password_and_policy ) )
        {
            sled_valid_passwords++;
        }
        if( is_valid_password_for_toboggan( password_and_policy ) )
        {
            toboggan_valid_passwords++;
        }
    }
    std::cout << "Valid Sled Passwords: " << sled_valid_passwords << std::endl;
    std::cout << "Valid Toboggan Passwords: " << toboggan_valid_passwords << std::endl;

    return 0;
}

bool is_valid_password_for_sled_rental( const std::string password_and_policy )
{
    std::istringstream ss( password_and_policy );
    std::string amounts, letter, password;
    ss >> amounts >> letter >> password;
    std::vector<int> bounds {};
    std::istringstream ss2( amounts );
    std::string item;
    while( std::getline( ss2, item, '-' ) )
    {
        bounds.push_back( std::stoi( item ) );
    }
    int occurrences {0};
    for( auto character : password )
    {
        if( character == letter.at( 0 ) )
        {
            occurrences++;
        }
    }
    if( bounds.at( 0 ) <= occurrences && occurrences <= bounds.at( 1 ) )
    {
        return true;
    }
    return false;
}

bool is_valid_password_for_toboggan( const std::string password_and_policy )
{
    std::istringstream ss( password_and_policy );
    std::string amounts, letter, password;
    ss >> amounts >> letter >> password;
    std::vector<int> position {};
    std::istringstream ss2( amounts );
    std::string item;
    while( std::getline( ss2, item, '-' ) )
    {
        position.push_back( std::stoi( item ) );
    }
    if( ( password.at( position.at( 0 ) - 1 ) == letter.at( 0 ) ) ^ ( password.at( position.at( 1 ) - 1 ) == letter.at( 0 ) ) )
    {
        return true;
    }
    return false;
}
