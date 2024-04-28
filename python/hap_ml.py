import pandas as pd
import numpy as np

def main():
    # Reads all the information within ess and prints the number of rows and columns
    ess = pd.read_csv('ess.csv')
    print(ess.shape)

    # Prints five rows of the happy and social meet columns
    print(ess.loc[:, 'happy'].head())
    print(ess.loc[:, 'sclmeet'].head())

    # Weeds out incomplete answers for the following variables
    ess = ess.loc[ess['sclmeet'] <= 10, :].copy()
    ess = ess.loc[ess['rlgdgr'] <= 10, :].copy()
    ess = ess.loc[ess['hhmmb'] <= 50, :].copy()
    ess = ess.loc[ess['netusoft'] <= 5, :].copy()
    ess = ess.loc[ess['agea'] <= 200, :].copy()
    ess = ess.loc[ess['health'] <= 5, :].copy()
    ess = ess.loc[ess['happy'] <= 10, :].copy()
    ess = ess.loc[ess['eduyrs'] <= 100, :].copy().reset_index(drop=True)

    # Compares happiness of active and inactive people using binary split
    social = list(ess.loc[:, 'sclmeet'])
    happy = list(ess.loc[:, 'happy'])
    low_social_happiness = [hap for soc, hap in zip(social, happy) if soc <= 5]
    high_social_happiness = [hap for soc, hap in zip(social, happy) if soc > 5]
    meanlower = np.mean(low_social_happiness)
    meanhigher = np.mean(high_social_happiness)
    print(f'The lower mean is {meanlower}')
    print(f'The higher mean is {meanhigher}')

    # Prints the split point for the number of household members
    allvalues = list(ess.loc[:, 'hhmmb'])
    predictedvalues = list(ess.loc[:, 'happy'])
    print(get_splitpoint(allvalues, predictedvalues))

    # Prints a tree with a depth of two
    variables = ['rlgdgr', 'hhmmb', 'netusoft', 'agea', 'eduyrs']
    outcome_variable = 'happy'
    maxdepth = 2
    print(getsplit(0, maxdepth, ess, variables, outcome_variable))

    # Prints a tree with a depth of three
    variables = ['sclmeet', 'rlgdgr', 'hhmmb', 'netusoft', 'agea', 'eduyrs', 'health', 'imprich']
    outcome_variable = 'happy'
    maxdepth = 3
    print(getsplit(0, maxdepth, ess, variables, outcome_variable))

    # Determines the total error rate between predicted and actual happiness values
    predictions = []
    maxdepth = 4
    thetree = getsplit(0, maxdepth, ess, variables, outcome_variable)
    for k in range(0, len(ess.index)):
        observation = ess.loc[k, :]
        predictions.append(get_prediction(observation, thetree))
    ess.loc[:, 'predicted'] = predictions
    errors = abs(ess.loc[:, 'predicted'] - ess.loc[:, 'happy'])
    print(np.mean(errors))

    # Determines the total error rate between predicted and actual happiness values for test data
    np.random.seed(518)
    ess_shuffled = ess.reindex(np.random.permutation(ess.index)).reset_index(drop=True)
    training_data = ess_shuffled.loc[0:37000, :]
    test_data = ess_shuffled.loc[37001:, :].reset_index(drop=True)
    thetree = getsplit(0, maxdepth, training_data, variables, outcome_variable)

    # Make predictions on the test data and calculate errors
    predictions = []
    for k in range(0, len(test_data.index)):
        observation = test_data.loc[k, :]
        predictions.append(get_prediction(observation, thetree))
    test_data.loc[:, 'predicted'] = predictions
    errors = abs(test_data.loc[:, 'predicted'] - test_data.loc[:, 'happy'])
    print(np.mean(errors))

# Finds the best split point for a variable
def get_splitpoint(allvalues,predictedvalues):
  lowest_error = float('inf')
  best_split = None
  best_lowermean = np.mean(predictedvalues)
  best_highermean = np.mean(predictedvalues)
  for pctl in range(0,100):
    split_candidate = np.percentile(allvalues, pctl)
    loweroutcomes = [outcome for value,outcome in zip(allvalues,predictedvalues) if \
    value <= split_candidate]
    higheroutcomes = [outcome for value,outcome in zip(allvalues,predictedvalues) if \
    value > split_candidate]
    if np.min([len(loweroutcomes),len(higheroutcomes)]) > 0:
      meanlower = np.mean(loweroutcomes)
      meanhigher = np.mean(higheroutcomes)
      lowererrors = [abs(outcome - meanlower) for outcome in loweroutcomes]
      highererrors = [abs(outcome - meanhigher) for outcome in higheroutcomes]
      total_error = sum(lowererrors) + sum(highererrors)
      if total_error < lowest_error:
        best_split = split_candidate
        lowest_error = total_error
        best_lowermean = meanlower
        best_highermean = meanhigher
  return(best_split,lowest_error,best_lowermean,best_highermean)

# Generates a tree and adds depth by splitting pairs of variables
def getsplit(depth,maxdepth,data,variables,outcome_variable):
    best_var = ''
    lowest_error = float('inf')
    best_split = None
    predictedvalues = list(data.loc[:,outcome_variable])
    best_lowermean = -1
    best_highermean = -1
    for var in variables:
        allvalues = list(data.loc[:,var])
        splitted = get_splitpoint(allvalues,predictedvalues)
        if(splitted[1] < lowest_error):
            best_split = splitted[0]
            lowest_error = splitted[1]
            best_var = var
            best_lowermean = splitted[2]
            best_highermean = splitted[3]
    generated_tree = [[best_var, float('-inf'), best_split, []], [best_var, \
    best_split, float('inf'), []]]
    if depth < maxdepth:
        splitdata1 = data.loc[data[best_var] <= best_split, :]
        splitdata2 = data.loc[data[best_var] > best_split, :]
        if len(splitdata1.index) > 10 and len(splitdata2.index) > 10:
            generated_tree[0][3] = getsplit(depth + 1, maxdepth, splitdata1, variables, outcome_variable)
            generated_tree[1][3] = getsplit(depth + 1, maxdepth, splitdata2, variables, outcome_variable)
        else:
            depth = maxdepth + 1
            generated_tree[0][3] = best_lowermean
            generated_tree[1][3] = best_highermean
    else:
      generated_tree[0][3] = best_lowermean
      generated_tree[1][3] = best_highermean
    return(generated_tree)

# Predicts happiness level using a decision tree
def get_prediction(observation,tree):
    j = 0
    keepgoing = True
    prediction = - 1
    while(keepgoing):
        j = j + 1
        variable_tocheck = tree[0][0]
        bound1 = tree[0][1]
        bound2 = tree[0][2]
        bound3 = tree[1][2]
        if observation.loc[variable_tocheck] < bound2:
            tree = tree[0][3]
        else:
            tree = tree[1][3]
        if isinstance(tree,float):
            keepgoing = False
            prediction = tree
    return(prediction)

if __name__ == "__main__":
  main()
