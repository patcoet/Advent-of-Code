input←⍎¨(⎕UCS 3⊃input)(≠⊆⊢)1⊃input←⎕NGET 'Z:\projects\Advent-of-Code\2021\04\input'
nums←⊃','(≠⊆⊢)⊃input
boards←{5 5⍴⊃,/⍵}¨(⊃,/{5⍴⍵}¨⍳(⍴1↓input)÷5)⊆1↓input

⍝ Mark a number on a board by adding 100 to it:
mark←{(⊃⍵)∊2⊃⍵:{({100+⍵}@(⊃⍵)(⊃⍵))2⊃⍵}(⍸(2⊃⍵)∊⊃⍵)(2⊃⍵)⋄1:2⊃⍵}

⍝ Rows of b1:
rows←{b←⍵⋄{1↑⍵⊖b}¨¯1+⍳5}
⍝ Cols of b1:
cols←{b←⍵⋄{1↑⍵⊖⍉b}¨¯1+⍳5}
rc←{(rows ⍵),(cols ⍵)}

⍝ Does the list of numbers ⍵ contain a bingo?
bingo←{⊃∨/∧/100≤¨⍵}

⍝ Sum of unmarked numbers in ⍵:
ums←{+/(100>25⍴⍵)/(25⍴⍵)}

⍝ Given a number and a list of boards, mark boards with it and return them:
mbs←{n←⊃⍵⋄boards←2⊃⍵⋄{mark n ⍵}¨boards}

res←{nums←⊃⍵⋄n←⊃nums⋄boards←2⊃⍵⋄bs←∨/¨bingo¨¨rc¨boards⋄pbs←∨/¨bingo¨¨rc¨3⊃⍵ ⋄ ∧/bs:(ums(pbs⍳0)⊃boards)(nums) ⋄ ∇(1↓nums) (mbs n boards) boards}nums boards boards
a←⊃res
b←¯1↑nums~2⊃res
a×b