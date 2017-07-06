def pop_sent(str1):
    sent = [[[ 1,"no mind thinks something|a",None,'co']],\
[[ 1,"Every part|p of the large house is|a white",None,'co'],[ 2,"The door is|g a|r part|p of the large house",None,'j'],[ 3,"The door is|a not white",None,'j']],\
[[ 1,"I saw everyone who drank something in the van",None,'co'],[ 2,"Leibniz drank something in the van",None,'j'],[ 3,"I did not see Leibniz",None,'j']],\
[[ 1,"I love nothing which is|r about murder",None,'co'],[ 2,"Hamlet is|r about murder",None,'j'],[ 3,"I love Hamlet",None,'j']],\
[[ 1,"I love anything which is|r about logic",None,'co'],[ 2,"Set Theory is|r about logic",None,'j'],[ 3,"I do not love set theory",None,'j']],\
[[ 1,"no green man from|b cold mars, lives on|r Earth",None,'co'],[ 2,"Jim is|g a|r green man born on|r Mars",None,'j'],[ 3,"Jim lives on|r Earth",None,'j']],\
[[ 1,"Every green man from|b Mars drinks",None,'co'],[ 2,"Jim is|g a|r green man born on|r Mars",None,'j'],[ 3,"Jim does not drink",None,'j']],\
[[ 1,"Everyone who spies on Leibniz, will|r be|a rewarded",None,'co'],[ 2,"Russell spied on Leibniz",None,'j'],[ 3,"Russell was|a not rewarded",None,'j']],\
[[ 1,"Everyone who spies on a|a nazi in Munich, will|r be|a rewarded",None,'co'],[ 2,"Russell spied on a nazi in Munich",None,'j'],[ 3,"Russell was|a not rewarded",None,'j']],\
[[ 1,"Anyone who breaks the speed limit, will|r be|a caught",None,'co'],[ 2,"Marilyn broke the speed limit",None,'j'],[ 3,"Marilyn was|a not caught",None,'j']],\
[[ 1,"I did not shed a tear",None,'co'],[ 2,"I shed some|p tears",None,'j']],\
[[ 1,"Every woman at|p the party drank",None,'co'],[ 2,"Jessica was|r at|p the party",None,'j'],[ 3,"Jessica is|g a|r woman",None,'j'],[ 4,"Jessica did not drink",None,'j']],\
[[ 1,"Every woman at|p the party drank",None,'co'],[ 2,"Jessica was|g a|r woman at|p the party",None,'j'],[ 3,"Jessica did not drink",None,'j']],\
[[ 1,"no part|p of the large house is|a white",None,'co'],[ 2,"The door is|g a|r part|p of the large house",None,'j'],[ 3,"The door is|a white",None,'j']],\
[[ 1,"I love everyone who reads Leibniz",None,'co'],[ 2,"Russell reads Leibniz",None,'j'],[ 3,"I do not love Russell",None,'j']],\
[[ 1,"There is|e a moment which does not exist in|b time",None,'co']],\
[[ 1,"There is|e a whole|c which is|g an|r individual",None,'co']],\
[[ 1,"There is|e a whole which is|g an|r individual",None,'ta']],\
[[ 1,"my dog drank some water",None,'co'],[ 2,"I do not own a dog",None,'j']],\
[[ 1,"I saw my dog",None,'co'],[ 2,"I do not own a dog",None,'j']],\
[[ 1,"I saw your dog",None,'co'],[ 2,"you do not own a dog",None,'j']],\
[[ 1,"your dog drank some water",None,'co'],[ 2,"you do not own a dog",None,'j']],\
[[ 1,"I saw his dog",None,'co'],[ 2,"he does not own a dog",None,'j']],\
[[ 1,"his dog drank some water",None,'co'],[ 2,"he does not own a dog",None,'j']],\
[[ 1,"I took the dog's ball",None,'co'],[ 2,"the dog does not own a ball",None,'j']],\
[[ 1,"the dog's ball is|a red",None,'co'],[ 2,"the dog does not own a ball",None,'j']],\
[[ 1,"Ada's ball is|a red",None,'co'],[ 2,"Ada does not own a ball",None,'j']],\
[[ 1,"I took Ada's ball",None,'co'],[ 2,"Ada does not own a ball",None,'j']],\
[[ 1,"The|r property|n redness is|a red",None,'co']],\
[[ 1,"Plato has|t the same teacher as Xenothon",None,'co'],[ 2,"Xenothon does not have|t a teacher",None,'j']],\
[[ 1,"I did not shed any|n tears",None,'co'],[ 2,"I shed a tear",None,'j']],\
[[ 1,"There is|e a thought which smells",None,'co']],\
[[ 1,"There is|e a thought which desires something",None,'co']],\
[[ 1,"There is|e a mind which is|a not mental",None,'co']],\
[[ 1,"There is|e a thought which is|g a|r group",None,'ta']],\
[[ 1,"There is|e a number|i which is|a physical",None,'co']],\
[[ 1,"There is|e a mind which smells",None,'co']],\
[[ 1,"There is|e a point which smells",None,'co']],\
[[ 1,"There is|e a thought which is|a physical",None,'co']],\
[[ 1,"There is|e a moment which is|a physical",None,'co']],\
[[ 1,"JFK is|g a|r kennedy",None,'co'],[ 2,"JFK is|g not part|f of the kennedy|a family",None,'j']],\
[[ 1,"Something is|g a|r b",None,'co'],[ 2,"b is|g not a|r class",None,'j']],\
[[ 1,"There is|e a point which thinks some|p thoughts",None,'co']],\
[[ 1,"I saw the man who drank some|p beers at|p the party",None,'co'],[ 2,"no one|p drank some|p beers at|p the party",None,'j']],\
[[ 1,"Some|p minds smell",None,'co']],\
[[ 1,"Some|p points smell",None,'co']],\
[[ 1,"Some|p numbers|i are|a physical",None,'co']],\
[[ 1,"Some|p points think something",None,'co']],\
[[ 1,"Some|p points have|w members",None,'co']],\
[[ 1,"Some|p points are|a physical",None,'co']],\
[[ 1,"Some|p numbers|i smell",None,'co']],\
[[ 1,"Some|p thoughts are|a not mental",None,'co']],\
[[ 1,"Some|p thoughts are|g moments",None,'co']],\
[[ 1,"Some|p thoughts think something",None,'co']],\
[[ 1,"Some|p thoughts smell",None,'co']],\
[[ 1,"Some|p thoughts desire something",None,'co']],\
[[ 1,"b has|c|r causal role c",None,'co'],[ 2,"Causal role c is|g not a|r property|n",None,'j']],\
[[ 1,"A universal is|r not distinct from its|a instance",None,'co']],\
[[ 1,"There is|e a universal which is|r not distinct from its|a instances",None,'co']],\
[[ 1,"The concept|n cat is|g itself|r a|r cat",None,'co']],\
[[ 1,"Dog is|g not a|r concept|n",None,'co']],\
[[ 1,"Point is|g a|r partially material|a concept|n",None,'co']],\
[[ 1,"This dog is|g a|r concept|n",None,'co']],\
[[ 1,"Thought is|g a|r partially material|a concept|n",None,'co']],\
[[ 1,"There is|e a point which is|a physical",None,'co']],\
[[ 1,"There is|e a number|i which smells",None,'co']],\
[[ 1,"There is|e a thought which is|a not mental|b",None,'co']],\
[[ 1,"There is|e a thought which is|g a|r moment",None,'co']],\
[[ 1,"There is|e a thought which thinks something",None,'co']],\
[[ 1,"There is|e a mind which does not think anything|a",None,'co']],\
[[ 1,"I have a point",None,'co']],\
[[ 1,"Plato has|t the same teacher as Xenothon",None,'co'],[ 2,"That|d teacher is Socrates",None,'j'],[ 3,"Socrates does not teach Xenothon",None,'j']],\
[[ 1,"I saw the same movie as you",None,'co'],[ 2,"That|d movie was Casablanca",None,'j'],[ 3,"I did not see Casablanca",None,'j']],\
[[ 1,"Leibniz and|c aristotle ate from the same cake",None,'co'],[ 2,"This|n was that|d cake",None,'j'],[ 3,"Leibniz did not eat from this|n",None,'j']],\
[[ 1,"The door is|a not large",None,'co'],[ 2,"The door which is|a green is|a large",None,'j']],\
[[ 1,"Leibniz and|c Aristotle studied logic ",None,'co'],[ 2,"Leibniz did not study logic",None,'j']],\
[[ 1,"Russell is|g not a|r man",None,'co']],\
[[ 1,"Russell has the|r property courage ",None,'co'],[ 2,"Russell is|a not courageous",None,'j']],\
[[ 1,"Russell has courage ",None,'co'],[ 2,"Russell is|a not courageous",None,'j']],\
[[ 1,"I think that|c it|p is|a true that|c you are|a smart",None,'co'],[ 2,"I do not believe that|c you are|a smart",None,'j']],\
[[ 1,"JFK is|g not a|r kennedy",None,'co'],[ 2,"JFK is|g part|f of the kennedy|a family",None,'j']]]
    return sent
