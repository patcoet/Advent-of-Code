input←⍎¨¨(⎕UCS 3⊃input)(≠⊆⊢)1⊃input←⎕NGET 'Z:\projects\Advent-of-Code\2021\03\input'
ogr←{fi←1⊃⍵⋄mc←2⊃⍵⋄n←3⊃⍵ ⋄ fi←((mc=¨n⊃¨fi)/fi) ⋄ 1=⍴fi:2⊥⊃fi ⋄ ∇ fi ((.5×⍴fi)≤+/(n+1)⊃¨fi) (n+1)}input ((.5×⍴input)≤+/1⊃¨input) 1
csr←{fi←1⊃⍵⋄lc←2⊃⍵⋄n←3⊃⍵ ⋄ fi←((lc=¨n⊃¨fi)/fi) ⋄ 1=⍴fi:2⊥⊃fi ⋄ ∇ fi ((.5×⍴fi)>+/(n+1)⊃¨fi) (n+1)}input ((.5×⍴input)>+/1⊃¨input) 1
ogr×csr