⍝ Character and segments used:
⍝ 0: a b c e f g
⍝ 1: c f
⍝ 2: a c d e g
⍝ 3: a c d f g
⍝ 4: b c d f
⍝ 5: a b d f g
⍝ 6: a b d e f g
⍝ 7: a c f
⍝ 8: a b c d e f g
⍝ 9: a b c d f g

⍝ If we have dab ab eafb:
⍝ We can replace:
⍝ dab with (d (A C F))(a (A C F))(b (A C F)),
⍝ ab with (a (C F))(b (C F)),
⍝ and eafb with (e (B C D F))(a (B C D F))(f (B C D F))(b (B C D F)).
⍝ Then we can replace all the (a)s with disjunctions, so:
⍝ (d ACF)(a CF)(b ACF)
⍝ (a CF)(b CF)
⍝ (e BCDF)(a CF)(f BCDF)(b BCDF)
⍝ and the bs:
⍝ (d ACF)(a CF)(b CF)
⍝ (a CF)(b CF)
⍝ (e BCDF)(a CF)(f BCDF)(b CF)
⍝ CF are known to be ab, so we can remove them from others:
⍝ (d A)(a CF)(b CF)
⍝ (a CF)(b CF)
⍝ (e BD)(a CF)(f BD)(b CF)

⍝ So, start with taking the signal patterns and replacing 

⍝ t←' '(≠⊆⊢)'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb'

⍝ Each line uses each number once, so we can solve all of them in a set order.
⍝ Find the one with 2 segments, then the one with 3 segments. The different segment is A.
⍝ Find the one with 4 segments. The 2 segments we haven't seen are BD.
⍝ Find the one with A, CF, CF, BD, and other. The BD is D and other is G.
⍝ Previous other BD is B.

⍝ t sorted shortest to longest:
st ← t[⍋⍴¨t]

⍝ ┌→────┬─────┬─────┬─────┬─────┬─────┬─────┐
⍝ │┌→┬─┐│┌→┬─┐│┌→┬─┐│┌→┬─┐│┌→┬─┐│┌→┬─┐│┌→┬─┐│
⍝ ││a│ │││b│ │││c│ │││d│ │││e│ │││f│ │││g│ ││
⍝ │└─┴⊖┘│└─┴⊖┘│└─┴⊖┘│└─┴⊖┘│└─┴⊖┘│└─┴⊖┘│└─┴⊖┘│
⍝ └────→┴────→┴────→┴────→┴────→┴────→┴────→┘
known ← {⍵,⊂''}¨'abcdefg'

⍝ 'a' learned 'XYZ'
learned ← {((⊂⍺ ⍵)@(⍺⍳⍨⊃¨known))known}
known←{⍺ learned ⍵}

⍝ known ← 'a' learned 'XYZ'

