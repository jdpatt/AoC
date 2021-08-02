#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>


struct Results
{
    int exit_code;
    int accumulator;
};

struct Instruction
{
    std::string operation;
    int argument;
    bool executed;
};


std::vector<Instruction> read_in_boot_code( void );
Results run_program( std::vector<Instruction> program );

int main()
{
    auto boot_code {read_in_boot_code()};
    auto copy_of_boot_code {boot_code};
    auto results {run_program( copy_of_boot_code )};
    std::cout << "Value prior to repeating instructions: " << results.accumulator << std::endl;
    for( int i = 0; i < boot_code.size(); i++ )
    {
        if( boot_code.at( i ).operation == "acc" )
        {
            continue;
        }
        auto modified_boot_code {boot_code};
        if( modified_boot_code.at( i ).operation == "jmp" )
        {
            modified_boot_code.at( i ).operation = "nop";
        }
        else if( modified_boot_code.at( i ).operation == "nop" )
        {
            modified_boot_code.at( i ).operation = "jmp";
        }
        // std::cout << "Running Program " << i << "..." << std::endl;
        auto results = run_program( modified_boot_code );
        if( results.exit_code == 0 )
        {
            break;
        }
    }

}

std::vector<Instruction> read_in_boot_code( void )
{
    std::vector<Instruction> boot_code {};
    std::ifstream file( "input.txt" );
    std::string line {};

    while( std::getline( file, line ) )
    {
        std::string operation;
        int argument;
        std::istringstream ss( line );
        ss >> operation >> argument;
        Instruction instruct {operation, argument, false};
        boot_code.push_back( instruct );
    }
    return boot_code;
}

Results run_program( std::vector<Instruction> program )
{
    int accumulator {0}, instruction_pointer{0};
    while( true )
    {
        try
        {
            auto instruction = program.at( instruction_pointer );
            program.at( instruction_pointer ).executed = true;
            if( instruction.executed )
            {
                return Results{-1, accumulator};
            }
            if( instruction.operation == "jmp" )
            {
                instruction_pointer += instruction.argument;
            }
            else if( instruction.operation == "acc" )
            {
                accumulator += instruction.argument;
                instruction_pointer ++;
            }
            else if( instruction.operation == "nop" )
            {
                instruction_pointer++;
            }

        }
        catch( const std::out_of_range &oor )
        {
            std::cout << "Program Completed...\t" << accumulator << std::endl;
            return Results{0, accumulator};
        }

    }

}
