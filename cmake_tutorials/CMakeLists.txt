#
# this is an example only, and is not intended to cmake any files:
#

cmake_minimum_required(VERSION 3.0)        # tells (cmake) the minimum version to use to produce the (make) file

set(CMAKE_BUILD_TYPE Debug)             # set() : a function used to set variables with their corresponding libraries
set(CMAKE_CXX_FLAGS "-std=c++14")       #       : tells the compiler that my code uses c++ 14 standard syntax
# OR
#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")       # : here I only append the (-std=c++14) flag on top the values (CMAKE_CXX_FLAGS) had

project(sample)         # project name

add_executable(
    sample                  # name of the executable that we want to produce
    src/main.cpp                # source files
    src/source1.cpp             # source files
    src/source2.cpp             # source files
)       
# OR: we can recursively add all .cpp files inside a directory:
            # file (GLOB_RECURSE SRC_FILES src/*.cpp)         # creates a variable (SRC_FILES) that has all (.cpp) files in the (src) in it
            # add_executable(
            #     sample
            #     ${SRC_FILES}
            # )

