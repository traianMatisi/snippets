# Flip coin - 100 days of python - day 4
# Author: Traian 11-6-24

from random import randint
def heads():
    print('''
        _.-'~~`~~'-._
     .'`  B   E   R  `'.
  /` I     .-'~"-.    T `\\
 ; L      / `-    \\     Y ;
;        />  `.  -.|       ;
|       /_     '-.__)      |
|        |-  _.' \ |       |
;   INGOWE`~~;     \\\\     ;
  \  TRUST '.___.-'`"    /
     '._   1 9 9 7   _.'
        `'-..,,,..-'`
''')

def tails():
    print('''
        _.-'~~`~~'-._
     .'`  B   E   R  `'.
    / I       _       T \\
  ; L  .---.  / > .---, Y ;
  |     <_  `'  `'  _>    |
  |       <_/\  /\_>      |
  |          /`'\         | 
   \        ".__."  ;    /
     '._   1 9 9 7    _.'
        `'-..,,,,..-'`
''')

coin = randint(0, 1)

if coin == 0:
    heads()
    print("HEADS")
else:
    tails()
    print("TAILS")
