# Wordle Searcher

Searches the word list in Wordle based on search pattern. Warning: like all forms of cheating, it trivializes the game, and robs you of your enjoyment of it. Use sparingly, or better yet not at all.

Example usage:
```
wordle-searcher % ./searcher.py

Input search pattern. (enter '?' or 'help' for help)
Simple: lowercase for yellows, uppercase for greens, dashes for grays
eg: af---   Ta--k
> r--Et

pattern = [^r][a-z][a-z]e[^t]   contains = (r,t)   excludes = ()
tiger, other, cater, inter, threw, deter, tamer, hater, eater, later, outer, 
taper, enter, otter, tuber, ether, timer, three, ester, after, alter, utter, 
water, voter, tried, tower, truer, taker, meter, steer
30 found in answers list
apter, artel, aster, biter, citer, cuter, dater, doter, gater, ither, kiter, 
liter, luter, mater, miter, muter, niter, noter, oater, ofter, opter, oxter, 
pater, peter, strep, strew, taber, taler, tared, tares, taser, tater, taver, 
tawer, taxer, terek, teres, tiler, tired, tires, titer, toker, toner, toper, 
tores, toter, toyer, treed, treen, trees, trier, tries, trued, trues, tryer, 
tuner, tuyer, tweer, twier, twoer, twyer, tyler, tyred, tyres, upter
65 found in accepted list

Input search pattern. (enter '?' or 'help' for help)
> ?
Simple: lowercase for yellows, uppercase for greens, dashes for grays
eg: af---   Ta--k
Advanced: use pipe (|) to seperate slots, alowing for multiple yellows per slot
eg: -|at|-|R|-      y|at||R|        re|re|re||ta,swk
Advanced: use comma then list of letters to indicate gray (excluded) letters
eg: ---Ay,l         S||||,aeiou     re|re|re|ta,swk

Input search pattern. (enter '?' or 'help' for help)
> ra|||E|t

pattern = [^ra][a-z][a-z]e[^t]   contains = (r,a,t)   excludes = ()
cater, tamer, hater, eater, later, taper, water, taker
8 found in answers list
dater, gater, mater, oater, pater, taber, taler, tared, tares, taser, tater, 
taver, tawer, taxer
14 found in accepted list

Input search pattern. (enter '?' or 'help' for help)
> ra|||E|t,shw

pattern = [^ra][a-z][a-z]e[^t]   contains = (r,a,t)   excludes = (s,h,w)
cater, tamer, eater, later, taper, taker
6 found in answers list
dater, gater, mater, oater, pater, taber, taler, tared, tater, taver, taxer
11 found in accepted list

Input search pattern. (enter '?' or 'help' for help)
> ^C
wordle-searcher % 
```
