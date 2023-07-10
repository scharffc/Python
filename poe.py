#References: 
#https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given-text-file/
#https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/

import string

count = 0

text = open("texts/poecat.txt", "r")

# Create an empty dictionary
d = dict()
  
# Loop through each line of the file

for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
  
    # Lowercase the text
    line = line.lower()
  
    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))
  
    # Split the line into words
    words = line.split(" ")
  
    # Iterate over each word in line
    for word in words:
        # Count the number of words
        count = count +1 

        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
 
# Print the number of words
print("There are", count, "words in this text")
       
# Print the contents of dictionary - words of more than 4 characters only
#for key in list(d.keys()):
#    if len(key) >=4:
#        print(key, " ", d[key])

# Print the content of dictionary with highest number first

newd = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))

# Print the contents of dictionary
#for key in list(newd.keys()):
#    if len(key) >=4 and newd[key] >= 6:
#        print(key, " ", newd[key])

# Print the contents of dictionary removing uninteresting words

def toberemoved(pair):
    (k,v) = pair
    return k not in ["that", "this", "these", "those", "which", "what", "been", "being", "have", "from", "with",
                     "into", "they", "them", "there", "where", "whom", "were", "upon", "more", "than",
                     "within", "only", "were", "down", "away", "before", "more", "their", "whose", "have",
                     "while", "about", "very", "about", "most", "when", "such", "would", "even", "some", "made", "could", "once"]


newdd = dict(filter(toberemoved, newd.items()))

#print(newdd)

for key in newdd:
    if len(key) >= 4 and newdd[key] >= 6:
        print(key, " ", newdd[key])

text.close()
