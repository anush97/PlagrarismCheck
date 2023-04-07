## Plagiarism Detection Algorithm

The goal of this algorithm is to determine whether a document or a source code has been plagiarized or not. The algorithm takes two text files, one considered to be original and the other considered to be the one to be compared or the to-be-checked file. The Longest Common Subsequence (LCS) approach is used to check the plagiarism percentage. LCS finds the longest subsequence common to all sequences in a set of sequences and saves the outcomes of each function call, eliminating the need for repeated calls in the future.

Before checking the text, the algorithm applies pre-processing techniques to improve the accuracy of the plagiarism detection approach. Both texts are pre-processed, reading files from the path provided during the execution command. The files' lines are initially split as per the new line's distinguisher and then the sentences into words. The words are then converted into lowercase to provide unbiased comparison. The last step in pre-processing is to filter the basic words used in files generally that do not change the meaning of the statements as such and hence can be overlooked.

LCS is applied at the sentence level, that is, the longest common subsequence is computed for all pairs of sentences in both texts. The plagiarism content is found by normalizing the sum of LCS for all sentences in the suspicious text by the number of tokens in that text.

Once the pre-processing is done, the LCS approach takes over, looping one set of files containing the words, and all the Dynamic Programming (DP) values are stored in a variable. Then looping through the length of both files, the algorithm first checks if the DP value is 0 or not. Then another condition is checked if the previous element of the to-be-checked file is the same as the previous element of the original file. If this condition holds true, then in the set of DP values, the diagonal element of index [i-1][j-1] is incremented (count). If none of the above-mentioned conditions hold true, then the maximum is checked among the previous on x-axis and y-axis, that is i-1 or j-1. 

In the end, the algorithm takes up the last element of the DP values and calculates the similarity index. The similarity index is calculated and if the measure percentage is greater than 40, 1 (True) is returned as output, else 0. 

## Usage

To execute the algorithm, run the following command: 

"python3 make FILE1 FILE2 run"

Please note that the algorithm is written in Python 3.
