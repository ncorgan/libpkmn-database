#
# Copyright (c) 2016-2017 Nicholas Corgan (n.corgan@gmail.com)
#
# Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
# or copy at http://opensource.org/licenses/MIT)
#

########################################################################
# CMake configuration
########################################################################
CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT(libpkmn-database C)

IF(NOT CMAKE_BUILD_TYPE)
    SET(CMAKE_BUILD_TYPE "Release" CACHE STRING "Build type")
ENDIF()

SET(DATABASE_TOPLEVEL_DIR ${CMAKE_CURRENT_SOURCE_DIR})
IF(NOT ${DATABASE_TOPLEVEL_DIR} STREQUAL ${CMAKE_SOURCE_DIR})
    MESSAGE(STATUS "")
    MESSAGE(STATUS "Building database as submodule of ${CMAKE_PROJECT_NAME}.")
    MESSAGE(STATUS "")
ENDIF()

SET(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake/Modules;${CMAKE_MODULE_PATH}")

########################################################################
# Find dependencies
########################################################################
FIND_PACKAGE(PythonInterp REQUIRED)

ADD_SUBDIRECTORY(sqlite3)
ADD_SUBDIRECTORY(database)
