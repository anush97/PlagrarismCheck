import sys
def longest_common_seq(l1,l2):
    s1= l1.split(" ")
    s2= l2.split(" ")
    # storing the dp values 
    comb = [[None]*(len(s1)+1) for i in range(len(s2)+1)] 
  
    for i in range(len(s2)+1): 
        for j in range(len(s1)+1): 
            if i == 0 or j == 0: 
                comb[i][j] = 0
            elif s2[i-1] == s1[j-1]: 
                comb[i][j] = comb[i-1][j-1]+1
            else: 
                comb[i][j] = max(comb[i-1][j] , comb[i][j-1]) 
    num = (comb[len(s2)][len(s1)] * 100)
    similarity = num/min(len(s1), len(s2))
    return 1 if (similarity >= 40) else 0
def files(file1,file2):
    file_name1=open(file1,"r" ,encoding="utf8")
    main=file_name1.read().replace("\n"," ")
    file_name1.close()

    file_name2=open(file2,"r",  encoding="utf8")
    check=file_name2.read().replace("\n"," ")
    file_name2.close()
    return (main , check)
main , check = files(sys.argv[1],sys.argv[2])
#main , check = files(r"C:/Users/ANUSHKA SHARMA/Desktop/Concordia/sem4/Algo/Project/40159259/40159259_detector.py",r"C:/Users/ANUSHKA SHARMA/Desktop/iConnect/new_dlib_victoria.py")
words_main = main.split(" ")
words_check = check.split(" ")
words_main = [token.lower() for token in words_main]
words_check = [token.lower() for token in words_check]
ignore_words = ['off', 'from', 'all', 'after', 'once', "hasn't", 'these', 'while', 'than', 'at', 'myself', 'your', 'she', "should've", 've', 'will', "aren't", 'hasn', 'such', 'yours', 'ourselves', 'won', 'y', 'weren', 's', 'was', 'if', 'hers', 'has', 'been', 'more', 'my', 'further', 'because', 'both', 'm', 'who', 'too', "haven't", 'the', 'wouldn', 'do', 'some', 'under', 'am', "don't", 'itself', 'his', 'but', 'out', 'shouldn', "wasn't", 'what', 'himself', 'aren', "you'd", 'did', 'can', 'hadn', 'our', 'about', "hadn't", "that'll", 'up', 'shan', 'those', 'only', 'didn', 'nor', 'to', 'o', 'an', 'i', 'any', 'themselves', "won't", "you'll", 'why', 'most', 'this', 'or', 'between', 'over', 'couldn', 'few', 'where', 'haven', 'mustn', 'when', 'so', 'you', 'me', 'we', 'then', 'and', 'a', "wouldn't", 'not', "she's", 'doing', 'against', 'its', "you're", 'being', 'through', "needn't", 'during', 'no', 'same', 'isn', "it's", 'before', 'll', 'whom', 'had', "isn't", 'just', 'by', 'have', 'doesn', "doesn't", 'be', 'wasn', 'there', 'it', 'again', 'they', 'very', 'don', 'on', 'that', 'are', 'as', 'of', 'yourselves', 'yourself', 'having', 'for', 'in', 't', "shan't", 'now', 'him', 'is', 're', 'ma', "didn't", 'theirs', 'which', 'how', 'were', 'mightn', 'herself', 'into', 'above', 'each', "weren't", 'ours', 'here', 'should', "shouldn't", 'own', 'does', 'down', "mustn't", 'ain', 'her', 'needn', "mightn't", "couldn't", 'until', "you've", 'he', 'their', 'with', 'd', 'other', 'them', 'below']
punctuations=['"','.','(',')',',','?',';',':',"''",'``']
filtered_words_main = [w for w in words_main if not w in ignore_words and not w in punctuations]
filtered_words_check = [w for w in words_check if not w in ignore_words and not w in punctuations]
l=longest_common_seq(main,check)
print(l)