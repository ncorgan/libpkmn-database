#
# Copyright (c) 2015-2016 Nicholas Corgan (n.corgan@gmail.com)
#
# Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
# or copy at http://opensource.org/licenses/MIT)
#

# Build SQLite database
SET(LIBPKMN_DATABASE_SCRIPT ${DATABASE_TOPLEVEL_DIR}/scripts/generate-libpkmn-db-dump.py)
SET(LIBPKMN_DATABASE_DUMP   ${CMAKE_CURRENT_BINARY_DIR}/libpkmn_db_dump)
SET(LIBPKMN_DATABASE        ${CMAKE_CURRENT_BINARY_DIR}/libpkmn.db)

SET(LIBPKMN_DATABASE_SOURCES
    ${CMAKE_CURRENT_SOURCE_DIR}/veekun-pokedex
    ${CMAKE_CURRENT_SOURCE_DIR}/libpkmn-additions
    ${CMAKE_CURRENT_SOURCE_DIR}/libpkmn-form-names
    ${CMAKE_CURRENT_SOURCE_DIR}/libpkmn-compat-num
)

ADD_CUSTOM_COMMAND(
    OUTPUT  ${LIBPKMN_DATABASE}
    DEPENDS ${LIBPKMN_DATABASE_SOURCES}
    COMMAND ${CMAKE_COMMAND} -E remove ${LIBPKMN_DATABASE}
    COMMAND ${PYTHON_EXECUTABLE} ${LIBPKMN_DATABASE_SCRIPT} --repo-dir=${CMAKE_CURRENT_SOURCE_DIR} --output=${LIBPKMN_DATABASE_DUMP}
    COMMAND sqlite3-shell ${LIBPKMN_DATABASE} ".read ${LIBPKMN_DATABASE_DUMP}"
    COMMENT "Compiling LibPKMN database"
)
ADD_CUSTOM_TARGET(
    libpkmn.db ALL
    DEPENDS ${LIBPKMN_DATABASE}
)
INSTALL(FILES
    ${LIBPKMN_DATABASE}
    DESTINATION share/libpkmn
    COMPONENT "Database"
)
