nums←⍎¨','(≠⊆⊢)¯1↓⊃⎕NGET 'Z:\projects\Advent-of-Code\2021\06\input'
tick←{nn←⍵-1⋄negs←⍸0>nn ⋄ ⍬≡negs:nn ⋄ ((6@negs)nn,(⍴negs)⍴8)}
⍴0{⍺=80:⍵ ⋄ (⍺+1)∇tick ⍵}nums