# PlagrarismCheck
The goal of this algorithm is to find whether a document or a source code has been plagiarised or not. 
We are taking two text files one is considered to be original and other one is considered to be the one to be compared or the to be checked file. 
I have used Longest Common Subsequence (LCS) approach to check the plagiarism percent.
I have used this because, as its name suggests LCS finds the longest subsequence common to all sequences in a set of sequences. 
Another benefit is that it saves the outcomes of each function call, eliminating the need for repeated calls in the future.
Before checking the text, I have first applied pre-processing techniques to the text. 
This improves the accuracy of the plagiarism detection approach used. 
The pre-processing of both the texts is done. 
Files are read from the path provided during the execution command.
Files’s lines are initially split as per the new line’s distinguisher and then the sentences into words. 
The words are then converted into lower case to provide unbiased comparison. 
The last step I have done in pre-processing is to filter the basic words used in files generally that doesn’t change the meaning of the statements as such and hence can be overlooked. 
LCS is applied at the sentence level, that is, we computed the longest common subsequence for all pairs of sentences in both texts. 
The plagiarism content is found by normalizing the sum of LCS for all sentences in the suspicious text by the number of tokens in that text. 
Once the pre processing is done, LCS approach takes over, lopping one set of files containing the words, all the Dynamic programming(dp) values are stored in a variable. 
Then lopping through the length of both the files, I have first checked if the dp value is 0 or not. 
Then another condition is checked if the previous element of to be checked file is same as the previous element of original file.
If this condition holds true then in the set of dp values, the diagonal element ie of index [i-1] [j-1] is incremented (count). 
If none of the above-mentioned conditions hold true, then maximum is checked among the previous on x axis and y axis that is i-1 or j-1. 
Then in the end, I take up the last element of the dp values and calculate the similarity index. 
The similarity index is calculated and if the measure percentage is greater than 40. 
If it is greater than 40 then 1 that is True, is returned as output else 0.
How to execute -
make FILE1 FILE2 run
Version of python used is - python3
