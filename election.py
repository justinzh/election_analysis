import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def get_votes(X, person, total):
    X[person + '_cnt'] = (X[total]*X[person]).astype(int)
    return X

def get_incremental(X, colname): 
    diff=[0] + [X.iloc[i][colname]-X.iloc[i-1][colname] for i in range(1, X.shape[0])]    
    X.insert(len(X.columns), colname+'_diff', diff)    
    return X 

def plotting(X_err):
    X_err[['trumpd_cnt_diff', 'bidenj_cnt_diff']].plot(kind='bar')   
    locs, labs = plt.xticks()    
    plt.xticks(locs, [lab.get_text()[5:16] for lab in labs], rotation='45' )
    plt.subplots_adjust(bottom=0.25)
    plt.legend(['trumpd', 'bidenj']) 
    plt.show()

def calc_gaps(X):
    X.set_index(pd.to_datetime(X.timestamp), inplace=True)
    X.drop('timestamp', axis=1, inplace=True)
    # remove 0-vote row
    #X.drop(X[X.votes==0].index, axis=0, inplace=True)  

    X = get_votes(X, 'trumpd', 'votes')
    X = get_votes(X, 'bidenj', 'votes')  

    X = get_incremental(X, 'trumpd_cnt')
    X = get_incremental(X, 'bidenj_cnt')
    X = get_incremental(X, 'votes')

    X_err = X[(X['trumpd_cnt_diff'] < 0) | (X['bidenj_cnt_diff'] < 0) | (X['votes_diff'] < 0)]    
    # plotting if needed
    # plotting(X_err)  
    
    trumpd_gap = X_err['trumpd_cnt_diff'][X_err['trumpd_cnt_diff']<0].sum()
    bidenj_gap = X_err['bidenj_cnt_diff'][X_err['bidenj_cnt_diff']<0].sum()

    return (trumpd_gap, bidenj_gap)

def plotting_statelist(state_list):
    state_list[['trump', 'biden']].plot(title='vote differences to match the outcoming election ratio', kind='bar') 
    plt.subplots_adjust(bottom=0.3)

    for lab in plt.xticks()[1]:
        color = 'red' if state_list.loc[lab.get_text()]['diff'] > 0 else 'blue'
        lab.set_color(color)

    plt.show()
    return

all_states = pd.read_csv('/Users/justin/Documents/datadrill/BallotCountingOnNov4.csv')
state_list = pd.DataFrame(columns=['trump', 'biden', 'diff'])
state_list.index.name = 'state'

for statename in all_states.state.unique():
    trumpd, bidenj = calc_gaps(all_states[all_states.state == statename])
    state_list.loc[statename] = [trumpd, bidenj, trumpd-bidenj]

state_list.to_csv('result')
 
