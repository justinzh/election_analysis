# election_analysis
digging out the data conflict on the state-wise election report result

Based on the election result up to Nov 11 from Edison data (https://thedonald.win/p/11Q8O2wesk/happening-calling-every-pede-to-/)

The original json data was ported into csv file by this script (https://pastebin.com/Q6nTP04N) for all states (BallotCountingOnNov4.csv)

The data conflict as pointed by  TrumanBlack (https://thedonald.win/p/11Q8O2wesk/happening-calling-every-pede-to-/) is summarized here again. 

Referring the csv file columns as following, 
state,timestamp,votes,eevp,trumpd,bidenj
alabama,2020-11-04T01:23:07Z,1053,0,0.407,0.585
alabama,2020-11-04T01:29:35Z,3709,0,0.506,0.489
....
where
votes: total vote number as the timestamp
trumpd / bidenj: the voteshare for each one

the consecutive votes change should match or larger than the sum of individual's change. in this case
votes diff = 3709-1053 = 2656
trumpd's votes gain = 3709*0.506 - 1053*0.407 = 1448
bidenj's votes gain = 3709*0.489 - 1053*0.585 = 1198
votes diff of 2656 should equal or bigger the sum of indivitual's (1448 + 1198 = 2646)

through out datasets this statement is no happening consistantly. this python script calculates the minimum missing votes each of canddid needs to 
get to the vote share reported in the file. the result is in the result.csv file.







