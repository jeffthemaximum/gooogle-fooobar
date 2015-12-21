'''
Minion interrogation
====================

You think you have Professor Boolean's password to the control center. All you need is confirmation, 
so that you can use it without being detected. You have managed to capture some minions so you can 
interrogate them to confirm.

You also have in your possession Professor Boolean's minion interrogation machine (yes, he interrogates 
    his own minions). Its usage is simple: you ask the minion a question and put him in the machine. 
After some time (specific to the minion), you stop the machine and ask the minion for the answer. 
With certain probability (again, specific to the minion) you either get the truthful answer or the 
minion remains silent. Once you have subjected a minion to the machine, you cannot use it on the minion 
again for a long period.

The machine also has a 'guarantee' setting, which will guarantee that the minion will answer the question 
truthfully. Unfortunately, that has the potential to cause the minion some irreversible brain damage, 
so you vow to only use it as a last resort: on the last minion you interrogate.

Since Professor Boolean's password is periodically changed, you would like to know the answer as soon as 
possible. So you decide to interrogate the minions in an order which will take the least expected time 
(you can only use the machine on one minion at a time).

For example, you have captured two minions: minion A taking 10 minutes, and giving the answer with 
probability 1/2, and minion B taking 5 minutes, but giving the answer with probability 1/5.

If you interrogate A first, then you expect to take 12.5 minutes.
If you interrogate B first, then you expect to take 13 minutes and thus must interrogate 
A first for the shortest expected time for getting the answer.

Write a function answer(minions) which given a list of the characteristics of each minion, 
returns the lexicographically smallest ordering of minions, which gives you the smallest expected 
time of confirming the password.

The minions are numbered starting from 0.

The minions parameter will be a list of lists. 

minions[i] will be a list containing exactly three elements, corresponding to the i^th minion. 

The first element of minion[i] will be a positive integer representing the time the machine takes 
for that minion. 

The ratio of the second and third elements will be the probability of that minion giving you the answer: 
the second element, a positive integer will be the numerator of the ratio and the third element, also a 
positive integer will be the denominator of the ratio. The denominator will always be greater than the 
numerator. That is, [time, numerator, denominator].

The return value must be a list of minion numbers (which are integers), depicting the optimal order in 
which to interrogate the minions. Since there could be multiple optimal orderings, return the lexicographically 
first optimal list.

There will be at-least two and no more than 50 minions.
All the integers in the input will be positive integers, no more than 1024.
'''

def answer(x):
    ratios = {}
    # create dictionary where key=index_of_minion_in_x and value=ratio_of_minion_values
    for i, minion in enumerate(x):
        # forces ratio to be floating point num
        ratio = minion[2] * (float(minion[0]) / minion[1])
        ratios[i] = ratio
    foo = []
    # iterates through dictionary and finds minimum ratio
    # adds index of minimum values to foo array
    # foo array so named because of my enjoyment of google foobar,
    # and not cuz I'm bad at naming variables :)
    for j in range(len(x)):
        minimum = min(ratios, key=ratios.get)
        foo.append(minimum)
        del(ratios[minimum])
    return foo

# ##
# unfortunately, this tricky solution only came about through trial-and-error
# of multiplying denominator * (time / numerator)
# not sure why it works...
# but sometimes the greatest discoveries are by accident, right?
# I just figured there must be some 'ratio' that involed some
# operations performed on the thre given numbers in the minion
# list. So I wrote the above code, which found 'ratios', then
# trial-and-erroed various formulas for ratio.
# I think it's pretty sweet since it gives O(n) runtimes, as opposed to
# following plan described in problem prompt, which would probably give
# O(n^2) runtime.
