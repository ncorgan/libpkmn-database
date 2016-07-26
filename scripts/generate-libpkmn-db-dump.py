#!/usr/bin/env python
#
# Copyright (c) 2015 Nicholas-2016 Corgan (n.corgan@gmail.com)
#
# Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
# or copy at http://opensource.org/licenses/MIT)
#

import codecs
from optparse import OptionParser
import os

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("--repo-dir", type="string", help="libpkmn-database repository")
    parser.add_option("--output", type="string", help="output file")
    (options,args) = parser.parse_args()

    f = codecs.open(os.path.join(options.repo_dir, "veekun-pokedex"), 'r', encoding='utf-8')
    g = codecs.open(os.path.join(options.repo_dir, "libpkmn-additions"), 'r', encoding='utf-8')
    h = codecs.open(os.path.join(options.repo_dir, "libpkmn-form-names"), 'r', encoding='utf-8')
    i = codecs.open(os.path.join(options.repo_dir, "libpkmn-compat-num"), 'r', encoding='utf-8')
    j = codecs.open(options.output, 'w', encoding='utf-8')

    flines = '\n'.join(f.read().split('\n')[:-2]) # Skip original "COMMIT;" line
    glines = g.read()
    hlines = h.read()
    compat_num = int(i.read().strip())

    compat_num_table = '''CREATE TABLE compat_num (
    compat_num INTEGER NOT NULL
);
INSERT INTO "compat_num" VALUES({0});
'''.format(compat_num)

    j.write(flines)
    j.write(glines)
    j.write(hlines)
    j.write(compat_num_table)
    j.write("COMMIT;\n")

    f.close()
    g.close()
    h.close()
    i.close()
    j.close()
