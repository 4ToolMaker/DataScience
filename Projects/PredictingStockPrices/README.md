# Predicting Stock Prices 

## Overview

This is the code for the Stock Price Prediction challenge for 'Learn Python for Data Science #3' by @Sirajology on YouTube. The code uses the scikit-learn machine learning library to train a support vector regression on a stock price dataset from Google Finance to predict a future price. In the video, I use scikit-learn to build an ML model, but for the challenge you'll use the Keras library.

There are two scripts. demo.py is the code in the video and challenge.py is a template for the coding challenge you will complete.

## Dependencies

   - [numpy](http://www.numpy.org/)
   - [tweepy](http://www.tweepy.org)
   - [Fast CSV Parser](https://pypi.python.org/pypi/csv)
   - [textblob](https://textblob.readthedocs.io/en/dev/)
   - [keras](https://keras.io)

Install missing dependencies using pip

## Demo Usage

Once you have your dependencies installed via pip, run the demo script in terminal via

python demo.py

## Challenge

You'll find the challenge template in this repo labeled challenge.py. The instructions are

    Use the Tweepy library to retrieve tweets about a company stock from twitter
    Use the TextBlob library to classify those tweets as either positive or negative given a threshold you define.
    If the majority of tweets are positive, then use the Keras library to build a neural network that predicts the next stock price given a dataset of past stock prices that you pull from Google Finance. This tutorial may be useful to you.

If you want to use your own template, that's fine too. Submit your code in the comments section and I'll announce the winner in the next video. Good luck!

## Credits 

Thank you Siraj.
