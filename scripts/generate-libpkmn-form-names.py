#!/usr/bin/env python
#
# Copyright (c) 2015-2017 Nicholas Corgan (n.corgan@gmail.com)
#
# Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
# or copy at http://opensource.org/licenses/MIT)
#

from optparse import OptionParser
import os
import sqlite3

words_to_remove = ["Forme","Form","Cloak","Type","Drive","Pattern","Flower","Trim",
                   "Sea","Size","Pikachu,","Pikachu","Rotom","Kyurem","Hoopa","Mode"]

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("--veekun-database", type="string", help="Stock Veekun database")
    parser.add_option("--output", type="string", help="Output file")
    (options,args) = parser.parse_args()

    conn = sqlite3.connect(options.veekun_database)
    c = conn.cursor()

    # Get all English form names
    c.execute("SELECT pokemon_form_id,form_name FROM pokemon_form_names WHERE local_language_id=9")
    all_form_names = c.fetchall()

    with open(options.output, 'w') as f:
        f.write('''CREATE TABLE libpkmn_pokemon_form_names (
    form_id INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    image_name VARCHAR(50)
);
''')

        for i,entry in enumerate(all_form_names):
            form_id = entry[0]
            form_name = entry[1]

            for word in words_to_remove:
                form_name = form_name.replace(" {0}".format(word),"").replace("{0} ".format(word),"")

            if "Mega" in form_name:
                if form_name.endswith("X"):
                    form_name = "Mega X"
                elif form_name.endswith("Y"):
                    form_name = "Mega Y"
                else:
                    form_name = "Mega"

            if form_name == "???":
                image_name = "unknown"
            elif form_name == "?":
                image_name = "question"
            elif form_name == "!":
                image_name = "exclamation"
            else:
                image_name = unicode(form_name.lower().replace(" ","-")).replace(u"\u00e9", u"e").encode("utf-8")

            f.write(u"INSERT INTO \"libpkmn_pokemon_form_names\" VALUES({0},\"{1}\",\"{2}\");\n".format(form_id,form_name,image_name).encode("utf-8"))
