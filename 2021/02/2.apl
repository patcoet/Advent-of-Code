input←{(⊃⊃⍵) (⍎2⊃⍵)}¨' '(≠⊆⊢)¨(⎕UCS 3⊃input)(≠⊆⊢)1⊃input←⎕NGET 'Z:\projects\Advent-of-Code\2021\02\input'
ps←{⊃⍵='f':2⊃⍵⋄1:0}¨input
ds←+\{⊃⍵='d':2⊃⍵⋄⊃⍵='u':0-(2⊃⍵)⋄1:0}¨input
(+/ps)×+/{(⊃⍵⊃input)='f':(⍵⊃ds)×(⍵⊃ps)⋄1:0}¨⍳⍴input