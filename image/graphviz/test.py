# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:31:30 2018

@author: kevin
"""

from graphviz import Digraph

dot = Digraph(comment="The round table")
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.render('round-table.gv', view=True)