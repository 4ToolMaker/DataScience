# Recommender Systems

## Overview

This is the code for the Recommender System challenge for 'Learn Python for Data Science #3' by @Sirajology on YouTube. The code uses the lightfm recommender system library to train a hybrid content-based + collaborative algorithm that uses the WARP loss function on the movielens dataset. The movielens dataset contains movies and ratings from over 1700 users. Once trained, our script prints out recommended movies for whatever users from the dataset that we choose to terminal.

## Dependencies

   - [numpy](http://www.numpy.org/)
   - [scipy](https://www.scipy.org/)
   - [lightfm](https://github.com/lyst/lightfm)

Install missing dependencies using pip

## Usage

Once you have your dependencies installed via pip, run the script in terminal via

python demo.py

Note If the lightfm dependency doesn't work for you via pip, just install it from source by running these two commands.

git clone git@github.com:lyst/lightfm.git

cd lightfm && pip install -e .

If you still have dependency version issues, use virtualenv.

## Challenge

    Instead of using the built-in fetch_movielens method, create your own method to fetch and parse a recommendation dataset of your choice. You can find some good dataset options here. Make sure to look at the fetch_movielens method to see how it works.

    Use 3 different loss functions (so 3 different models), compare their results, and then only print the recommendations (products, songs, tv shows, etc.) for the best one. You'll find the available loss functions here.

## Credits

Credit goes to the lightfm team. Thank you.
