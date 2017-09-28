# Hangman
Created : September 2017

This is a quick script I wrote to solve hangman puzzles. The "word" string is declared with known letters and unknown letters (represented by an asterick). There is an array of guessed letters. The script loops through a file of 479,000 known English words, printing out all that match the parameters given. 

This is not a complex script, nor is there an intuitive interface. I wrote this in 10 minutes to solve a hangman contest online. Possible improvements would be a better interface (even just CLI arguments), or more intelligent guessing. Possible interesting implementations could be to use a machine learning algorithm to intelligently guess letters, or be able to give it hints "this is a food" or "this is an animal" and have the program intelligently guess based on those. But I will likely never do that.
