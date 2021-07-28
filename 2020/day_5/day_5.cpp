#include <algorithm>
#include <iostream>
#include <iterator>
#include <fstream>
#include <numeric>
#include <vector>

int get_seat_id( int row, int column )
{
    return ( row * 8 ) + column;
}

// If the character is F or L, return the lower half of the list.
std::vector<int> down_select_seats( const std::vector<int> iterable, const char character )
{
    if( character == 'F' or character == 'L' )
    {
        return std::vector<int>( iterable.begin(), iterable.begin() + static_cast<int>( iterable.size() / 2 ) );
    }
    return std::vector<int>( iterable.begin() + static_cast<int>( iterable.size() / 2 ), iterable.end() );
}

std::vector<std::string> read_in_boarding_passes()
{
    std::vector<std::string> boarding_passes;
    std::ifstream file( "input.txt" );
    std::string boarding_pass;
    while( std::getline( file, boarding_pass ) )
    {
        boarding_passes.push_back( boarding_pass );
    }
    return boarding_passes;
}

/**
 * From the list of seat ids, there is only one missing and that is your seat.
 *
 * If {6, 4, 7, 8} is the list then 5 is your seat.
 * */
int find_your_seat( std::vector<int> &seats )
{
    std::vector<int> ideal_seats;
    std::sort( seats.begin(), seats.end() );
    for( int index = seats.front(); index < seats.back() + 1; index++ )
    {
        ideal_seats.push_back( index );
    }
    std::vector<int> diff;
    std::set_difference( ideal_seats.begin(), ideal_seats.end(), seats.begin(), seats.end(),  std::inserter( diff, diff.begin() ) );
    if( diff.empty() )
    {
        throw std::runtime_error( "set_difference didn't find element." );
    }
    return diff.at( 0 );
}

int main()
{
    std::vector<int> seat_ids {};
    auto boarding_passes = read_in_boarding_passes();
    for( auto pass : boarding_passes )
    {
        std::vector<int> rows( 128 );
        std::vector<int> columns( 8 );
        std::iota( rows.begin(), rows.end(), 0 );
        std::iota( columns.begin(), columns.end(), 0 );
        for( int index = 0; index < pass.size(); index++ )
        {
            if( index < 7 )
            {
                rows = down_select_seats( rows, pass[index] );
            }
            else
            {
                columns = down_select_seats( columns, pass[index] );
            }
        }
        seat_ids.push_back( get_seat_id( rows.at( 0 ), columns.at( 0 ) ) );
    }
    std::cout << "Highest Seat ID Found (Part 1): "
              << *std::max_element( seat_ids.begin(), seat_ids.end() )
              << std::endl; // 871
    std::cout << "Your Seat is: "
              << find_your_seat( seat_ids )
              << std::endl; // 640


}
