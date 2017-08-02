
def info():

    order = [114, 115, 36, 37, 114, 100] # 149
    get_words_used = 0
    proof_type = 0
    # 0 is for testing the whole code without printing
    # 1 is for printing all sentences to excel,
    # 2 is for one sentence to terminal
    # 3 is for testing spelling errors
    return proof_type, get_words_used, order


# 8 has a sentence that does not print to terminal correctly, marilyn did not get caught
# 9 has printing errors, so does 27
# improve how we recategorize synonyms
# 65 is reprinting a duplicate attached sentence
# in sentence 35 the instantiation of things only occurs if it obtains a contradiction
# major printing errors in 35
# bind conjunctions in consistent statement
# define 2 such that 1 and 3 are not also defined

# in 140 we get the needed attached sentence but we need to infer the antecedent as a conjunct
# in 2 is not a number we have to use indefinite instantiation
# 33 substitutes incorrectly type 1

# himanshu always place the order to [0, 0, 2] and proof_type to 1