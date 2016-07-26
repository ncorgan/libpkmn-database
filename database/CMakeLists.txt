#
# Copyright (c) 2015-2016 Nicholas Corgan (n.corgan@gmail.com)
#
# Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
# or copy at http://opensource.org/licenses/MIT)
#

# Build SQLite database
SET(libpkmn_DATABASE_SCRIPT ${DATABASE_TOPLEVEL_DIR}/scripts/generate-libpkmn-db-dump.py)
SET(libpkmn_DATABASE_DUMP   ${CMAKE_CURRENT_BINARY_DIR}/libpkmn_db_dump)
SET(libpkmn_DATABASE        ${CMAKE_CURRENT_BINARY_DIR}/libpkmn.db)

SET(libpkmn_DATABASE_SOURCES
    ${CMAKE_CURRENT_SOURCE_DIR}/veekun-pokedex
    ${CMAKE_CURRENT_SOURCE_DIR}/libpkmn-additions
    ${CMAKE_CURRENT_SOURCE_DIR}/libpkmn-form-names
    ${CMAKE_CURRENT_SOURCE_DIR}/libpkmn-compat-num
)

ADD_CUSTOM_COMMAND(
    OUTPUT  ${libpkmn_DATABASE}
    DEPENDS ${libpkmn_DATABASE_SOURCES}
    COMMAND ${CMAKE_COMMAND} -E remove ${libpkmn_DATABASE}
    COMMAND ${PYTHON_EXECUTABLE} ${libpkmn_DATABASE_SCRIPT} --repo-dir=${CMAKE_CURRENT_SOURCE_DIR} --output=${libpkmn_DATABASE_DUMP}
    COMMAND sqlite3-shell ${libpkmn_DATABASE} ".read ${libpkmn_DATABASE_DUMP}"
    COMMENT "Compiling LibPKMN database"
)
ADD_CUSTOM_TARGET(
    libpkmn.db ALL
    DEPENDS ${libpkmn_DATABASE}
)
INSTALL(FILES
    ${libpkmn_DATABASE}
    DESTINATION share/libpkmn
    COMPONENT "Database"
)
