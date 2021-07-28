// std::set<std::string> a;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <fstream>
#include <numeric>
#include <vector>
#include <set>

void read_in_customs_forms( std::vector<std::vector<std::set<char>>> &passenger_groups, const std::string filename );

int main()
{
    std::vector<std::vector<std::set<char>>> passenger_groups;
    read_in_customs_forms( passenger_groups, "input.txt" );

    int anyone_who_said_yes {0};
    for( auto group : passenger_groups )
    {
        std::set<char> yes_in_group {};
        for( auto passenger : group )
        {
            yes_in_group.insert( passenger.begin(), passenger.end() );
        }
        anyone_who_said_yes += yes_in_group.size();
    }
    std::cout << "Sum of yes for anyone in passenger groups: " << anyone_who_said_yes << std::endl; // 6259

    int everyone_said_yes {0};

    for( auto group : passenger_groups )
    {
        std::set<char> result {group.at( 0 )};
        for( int index = 1; index < group.size(); index++ )
        {
            std::set<char> intersection;
            std::set_intersection( result.begin(), result.end(), group.at( index ).begin(), group.at( index ).end(),  std::inserter( intersection, intersection.begin() ) );
            result = intersection;
        }
        everyone_said_yes += result.size();
    }
    std::cout << "Sum of yes for everyone in passenger groups: " << everyone_said_yes << std::endl; // 3178

}

void read_in_customs_forms( std::vector<std::vector<std::set<char>>> &passenger_groups, const std::string filename )
{
    std::ifstream file( filename );
    std::string line;
    std::vector<std::set<char>> group;
    std::set<char> passenger;
    while( std::getline( file, line ) )
    {
        if( line.empty() )
        {
            passenger_groups.push_back( group );
            group.clear();
        }
        else
        {
            for( auto character : line )
            {
                passenger.insert( character );
            }
            group.push_back( passenger );
            passenger.clear();
        }

    }
    passenger_groups.push_back( group );
}
