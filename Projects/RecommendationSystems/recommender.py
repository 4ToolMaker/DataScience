"""recommendation systems Project:

- CHALLENGE part 1 of 3 - write your own fetch and format method for a
- different recommendation dataset. Here a good few,
- (https://gist.github.com/entaroadun/1653794)  and take a look at the
- fetch_movielens method to see what it's doing"""


# importing our dependencies
import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM


# fetch data and format it optional parameter min_rating of 4.0 or higher
data = fetch_movielens(min_rating=4.0)

# print training and testing data
print(repr(data['train']))
print(repr(data['test']))


# CHALLENGE part 2 of 3 - use 3 different loss functions (so 3 different
# models), compare results, print results for the best one.
# Available loss functions are warp, logistic, bpr, and warp-kos.

# create our model with a single parameter loss == model prediction and our
# desired output: we want to minimize it during trainning so our model
# will get more accurate over time.
# the loss we will choose is warp == weigthed approximae rank pairwise
# it uses the gradient descent algorithm to iteratively find the weigths that
# improve our decision over time
# it takes in consideration both the user past ratings, content based and
# similarly users ratings
model = LightFM(loss='warp')
# train model with 30 epochs and 2 parallel computations
model.fit(data['train'], epochs=30, num_threads=2)


# CHALLENGE part 3 of 3 - Modify this function so that it parses your dataset
# correctly to retrieve the necessary variables (products, songs, tv shows,
#  etc.) then print out the recommended results

def sample_recommendation(model, data, user_ids):

    # number of users and movies in training data
    n_users, n_items = data['train'].shape

    # generate recommendations for each user we input
    for user_id in user_ids:

        # movies they already like
        known_positives = data['item_labels'][data['train'].tocsr()[
            user_id].indices]

        # movies our model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))
        # rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        # print out the results
        print("User %s" % user_id)
        print("     Known positives:")

        for x in known_positives[:3]:
            print("        %s" % x)

        print("     Recommended:")

        for x in top_items[:3]:
            print("        %s" % x)


# calling our model data and three random user's id as the parameters
sample_recommendation(model, data, [3, 25, 450])
