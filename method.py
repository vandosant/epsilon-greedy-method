def choose():
  if math.random() < 0.1:
    # exploration!
    # choose a random lever 10% of the time.
  else:
    # exploitation!
    # for each lever,
      # calculate the expectation of reward.
      # This is the number of trials of the lever divided by the total reward
      # given by that lever.
    # choose the lever with the greatest expectation of reward.
    # increment the number of times the chosen lever has been played.
    # store test data in redis, choice in session key, etc..
def reward(choice, amount):
  # add the reward to the total for the given lever.
