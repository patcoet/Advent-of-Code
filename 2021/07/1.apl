nums←⍎¨','(≠⊆⊢)¯1↓input←⊃⎕NGET 'Z:\projects\Advent-of-Code\2021\07\input'
⌊/{n←⍵⋄+/{|⍵-n}¨nums}¨⍳(1+⌈/nums)-1