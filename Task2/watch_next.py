########################################################################
# Compulsory Task 2
# Let us build a system that will tell you what to watch next based on the word
# vector similarity of the description of movies.
# Create a file called watch_next.py
# Read in the movies.txt file. Each separate line is a description of a different
# movie.
# Your task is to create a function to return which movies a user would watch
# next if they have watched Planet Hulk with the description “Will he save
# their world or destroy it? When the Hulk becomes too dangerous for the
# Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
# planet where the Hulk can live in peace. Unfortunately, Hulk land on the
# planet Sakaar where he is sold into slavery and trained as a gladiator.”
# The function should take in the description as a parameter and return the
# title of the most similar movie.
# Host your solution on a Git host such as GitLab or GitHub.
# Remember to exclude any venv or virtualenv files from your repo.
# Add the link for your remote Git repo to your semantic_similarity.txt file.
########################################################################

import spacy
nlp = spacy.load("en_core_web_md")

# Open movies.txt for reading
myfile = open("movies.txt", "r")
data = myfile.read()

# Store each line into a list. Newline is the delimiter
data_into_list = data.split("\n")
#print(data_into_list)
myfile.close()

sentence_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"

model_sentence = nlp(sentence_to_compare)

next_movie = []

for sentence in data_into_list:
    similarity = nlp(sentence).similarity(model_sentence)
    next_movie.append(sentence.split(':')[0] + ":" + str(similarity)) # Append each result of the similarity to a list 
    next_movie.sort(key = lambda i: i.split(':')[1]) # Sort the list in ascending order on the second element (the similarity score)

print("The next recommended movie for you to watch next is: " + next_movie[-1].split(':')[0])