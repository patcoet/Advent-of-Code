input←(⎕UCS 3⊃input)(≠⊆⊢)1⊃input←⎕NGET 'Z:\projects\Advent-of-Code\2021\03\input'
mcb←(.5×⍴input)<¨+/¨{⍎¨⍵⊃¨input}¨⍳⍴⊃input
lcb←1-mcb
(2⊥mcb)×(2⊥lcb)