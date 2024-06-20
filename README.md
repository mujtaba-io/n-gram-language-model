# N-Gram Language Model in Python
[Stanford university text for understanding model](http://web.stanford.edu/~jurafsky/slp3/3.pdf).    
This is my summer vacation june 2024 ML practice in which I aimed to make a words auto-complete program that is similar to how your mobile keyboard suggests word based on already typed part of message.

# How it works?
This is based on conditional probability where probability of next word given already typed words is calculated and the highest probability word is predicted. For example:


```p(time | a person who thinks all the) = probability of 'time' given 'a person who thinks all the'```

We know that in data, there is only one this absurd quote so the pribability of 'time' is highest given existing string.

# Usage
I rebuilt the entire model every iteration, which results in slow compute. If you only build model once, it will be extremely fast (but I believe it would be inaccurate).

# Personalizing it
To personalize it for your friends group, make sure to extract all group-chat messages and put them in a .txt file and feed the file to this model. Currently it uses shakespeare and alice in wonderland text so it gives weird results.