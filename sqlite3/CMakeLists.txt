#
# Copyright (c) 2015,2017 Nicholas Corgan (n.corgan@gmail.com)
#
# Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
# or copy at http://opensource.org/licenses/MIT)
#

IF(NOT USE_INTERNAL_SQLITE3)
    FIND_PACKAGE(SQLite3)
ENDIF()

IF(NOT SQLITE3_FOUND)
    ADD_LIBRARY(sqlite3 STATIC sqlite3.c)
    TARGET_LINK_LIBRARIES(sqlite3 ${CMAKE_THREAD_LIBS_INIT})

    IF(UNIX)
        TARGET_LINK_LIBRARIES(sqlite3 dl)
        SET_TARGET_PROPERTIES(sqlite3 PROPERTIES
            COMPILE_FLAGS "-DSQLITE_THREADSAFE=0 -DSQLITE_ENABLE_COLUMN_METADATA -fPIC"
        )
    ELSE()
        SET_TARGET_PROPERTIES(sqlite3 PROPERTIES
            COMPILE_FLAGS "-DSQLITE_THREADSAFE=0 -DSQLITE_ENABLE_COLUMN_METADATA"
        )
    ENDIF(UNIX)

    ADD_EXECUTABLE(sqlite3-shell shell.c)
    TARGET_LINK_LIBRARIES(sqlite3-shell sqlite3)

    # Set the CMake variables FIND_PACKAGE would populate.
    SET(SQLITE3_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR} CACHE STRING "SQLite3 include dir")
    SET(SQLITE3_LIBRARY_RELEASE sqlite3 CACHE STRING "SQLite3 library")
    SET(SQLITE3_EXECUTABLE sqlite3-shell CACHE STRING "SQLite3 executable")
ENDIF()
