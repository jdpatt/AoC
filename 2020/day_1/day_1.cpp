// Day 1
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<int> read_expense_report( const std::string filename );
std::vector<int> find_combo_that_sum_to_value( const std::vector<int> *iterable, const int value, const int length );
int multiply_vector( const std::vector<int> *iterable );
void display_vector( const std::vector<int> *iterable );

int main()
{
    std::vector<int> expense_report{read_expense_report( "input.txt" )};
    std::vector<int> combo{find_combo_that_sum_to_value( &expense_report, 2020, 2 )};
    std::cout << "Combo: ";
    display_vector( &combo );
    std::cout << " Product: " << multiply_vector( &combo ) << std::endl;
}

/**
 * Read in the expense report line by line and convert each item to an integer.
 * */
std::vector<int> read_expense_report( std::string filename )
{
    std::vector<int> file_contents;
    std::cout << "Reading expense report: " << filename << std::endl;
    std::ifstream file( filename );
    std::string line_in_file{};
    while( std::getline( file, line_in_file ) )
    {
        file_contents.push_back( std::stoi( line_in_file ) );
    }
    return file_contents;
}

std::vector<int> find_combo_that_sum_to_value( const std::vector<int> *iterable, const int value, const int length )
{
}

int multiply_vector( const std::vector<int> iterable )
{
    int product{1};
    for( const auto &item : iterable )
    {
        product *= item;
    }
    return product;
}

void display_vector( const std::vector<int> iterable )
{
    std::cout << "(";
    for( int i = 0; i < iterable.size(); i++ )
    {
        std::cout << iterable.at( i );
        if( i != iterable.size() )
        {
            std::cout << ", ";
        }
    }
    std::cout << ")";
}
