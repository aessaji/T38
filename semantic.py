########################################################################
# Compulsory Task 1
# Follow these steps:
# Create a file called semantic.py and run all the code extracts above.
# Write a note about what you found interesting about the similarities
# between cat, monkey and banana and think of an example of your own.
# Run the example file with the simpler language model ‘en_core_web_sm’
# and write a note on what you notice is different from the model
# 'en_core_web_md'.
# Host your solution on a Git host such as GitLab or GitHub.
# Remember to exclude any venv or virtualenv files from your repo.
# Add the link for your remote Git repo to a text file named
# semantic_similarity.txt
########################################################################

import spacy
nlp = spacy.load('en_core_web_sm')

#########################################################
# Example 1
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
#########################################################


#########################################################
# Example 2
tokens = nlp('cat apple monkey banana car green')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
#########################################################


#########################################################
# Example 3
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
#########################################################

# In example 2 I found it interesting that the monkey and banana have a higher similarity than monkey/apple. The model predicts that
# monkeys eat bananas so it gives them a higher similarity. But I think that is a stereo type. We are used to seeing monkeys depicted
# with bananas, but in nature monkeys dont really have a preference over bananas/apples. Both are seen as a food source.
# I added car and green and also was surprised to see green car has a lower similarity than green apple. Ideally both should be in the same
# range as a car is equally green as a green apple. Also not all apples are green. You get red apples too.

# Running the above examples with the sm model I noticed the similarities were lower. Im assuming this is because sm is the small package and md is the 
# medium package. 