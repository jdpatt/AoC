// Day 1
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<int> read_expense_report( const std::string filename );
std::vector<int> two_combo_that_sum_to_value( const std::vector<int> *iterable, const int value );
std::vector<int> three_combo_that_sum_to_value( const std::vector<int> *iterable, const int value );
int multiply_vector( const std::vector<int> *iterable );
void display_vector( const std::vector<int> *iterable );

// Part 1: Combo: (631, 1389) Product: 876459
// Part 2: Combo: (708, 140, 1172) Product: 116168640
int main()
{
    std::vector<int> expense_report{read_expense_report( "input.txt" )};
    std::vector<int> combo{two_combo_that_sum_to_value( &expense_report, 2020 )};
    std::cout << "Part 1: Combo: ";
    display_vector( &combo );
    std::cout << " Product: " << multiply_vector( &combo ) << std::endl;
    combo = three_combo_that_sum_to_value( &expense_report, 2020 );
    std::cout << "Part 2: Combo: ";
    display_vector( &combo );
    std::cout << " Product: " << multiply_vector( &combo ) << std::endl;
    return 0;
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

std::vector<int> two_combo_that_sum_to_value( const std::vector<int> *iterable, const int value )
{
    std::vector<int> combo;
    for( auto one : *iterable )
    {
        for( auto two : *iterable )
        {
            if( one + two == value )
            {
                combo.push_back( one );
                combo.push_back( two );
                goto exit;
            }
        }
    }
exit:
    return combo;
}

std::vector<int> three_combo_that_sum_to_value( const std::vector<int> *iterable, const int value )
{
    std::vector<int> combo;
    for( auto one : *iterable )
    {
        for( auto two : *iterable )
        {
            for( auto three : *iterable )
            {
                if( one + two + three == value )
                {
                    combo.push_back( one );
                    combo.push_back( two );
                    combo.push_back( three );
                    goto exit;
                }
            }
        }
    }
exit:
    return combo;
}

int multiply_vector( const std::vector<int> *iterable )
{
    int product{1};
    for( const auto &item : *iterable )
    {
        product *= item;
    }
    return product;
}

/**
 * Display the content of the vector mimicing python's view.
 */
void display_vector( const std::vector<int> *iterable )
{
    std::cout << "(";
    for( int i = 0; i < iterable->size(); i++ )
    {
        std::cout << iterable->at( i );
        if( i != iterable->size() - 1 )
        {
            std::cout << ", ";
        }
    }
    std::cout << ")";
}
