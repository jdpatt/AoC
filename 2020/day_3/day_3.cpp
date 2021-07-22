#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<std::string> read_in_map_slice( const std::string filename );
int navigate_terrain_and_count_trees( const std::vector<std::string> &terrain, const std::vector<int> &slope );
void update_position( std::vector<int> &position, int width, int length, const std::vector<int> &slope );


// Reading map file: input.txt
// Part 1: Tree Count: 289
// Part 2: Tree Count: 5522401584
int main()
{
    std::vector<std::string> terrain_map {read_in_map_slice( "input.txt" )};

    std::cout << "Part 1: Tree Count: " << navigate_terrain_and_count_trees( terrain_map, {3, 1} ) << std::endl;

    std::vector<std::vector<int>> slopes
    {
        {1, 1},
        {3, 1},
        {5, 1},
        {7, 1},
        {1, 2}
    };
    std::vector<int> tree_counts {};
    for( auto slope : slopes )
    {
        tree_counts.push_back( navigate_terrain_and_count_trees( terrain_map, slope ) );
    }
    size_t product {1};
    for( auto item : tree_counts )
    {
        product *= item;
    }
    std::cout << "Part 2: Tree Count: " << product << std::endl;
    return 0;
}

/**
 * Read in every line of the file into a vector.  The map is represented with '#' as trees and
 * '.' as open space.
 * */
std::vector<std::string> read_in_map_slice( const std::string filename )
{
    std::vector<std::string> terrain;
    std::cout << "Reading map file: " << filename << std::endl;
    std::ifstream file( filename );
    std::string map_segment{};
    while( std::getline( file, map_segment ) )
    {
        terrain.push_back( map_segment );
    }
    return terrain;
}

int navigate_terrain_and_count_trees( const std::vector<std::string> &terrain, const std::vector<int> &slope )
{
    int num_of_trees {0};
    std::vector<int> position {0, 0};
    constexpr int X {0};
    constexpr int Y {1};
    while( position.at( Y ) < terrain.size() - 1 )
    {
        update_position( position, terrain.at( 0 ).size() - 1, terrain.size() - 1, slope );
        if( terrain.at( position.at( Y ) ).at( position.at( X ) ) == '#' )
        {
            num_of_trees++;
        }
    }
    return num_of_trees;
}

/**
 *  Update the current position based off the slope, wrap when at the edge of the map.
 * */
void update_position( std::vector<int> &position, int width, int length, const std::vector<int> &slope )
{
    constexpr int X {0};
    constexpr int Y {1};
    if( position.at( X ) + slope.at( X ) > width )
    {
        position.at( X ) = ( position.at( X ) + slope.at( X ) ) - width - 1;
    }
    else
    {
        position.at( X ) = position.at( X ) + slope.at( X );
    }
    if( position.at( Y ) + slope.at( Y ) > length )
    {
        position.at( Y ) = length - 1;
    }
    else
    {
        position.at( Y ) = position.at( Y ) + slope.at( Y );
    }
}
