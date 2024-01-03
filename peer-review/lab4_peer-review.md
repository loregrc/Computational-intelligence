# Lab4: Peer-review
These are my peer-reviews for the fourth lab.

**To Thomas Baracco (s308722):**
Hi Thomas,

First of all, I want to tell you that I appreciated the idea of using a q-learning algorithm to train the agents.

The code itself is very clear and readable. The q-learning algorithm does its job, and it's appropriately commented.  
Perhaps I would have preferred a greater separation between the game logic and the training logic, with comments in specific sections rather than inside the code, but these are personal preferences.

You have certainly fulfilled the requirements of the lab.  
Maybe to make things more interesting, you could have done an analysis on the training parameters behaviour.  
For example, how many games are needed to train your agent optimally, how positive and negative rewards influence the q-table, improving or worsening the training outcome.  
It would have been interesting to see such a study with the appropriate results presented and explained clearly, perhaps with your reflection on the achieved results.  
At the end of training, your agent has a winning rate of 90.88% against a random player; are the remaining games losses or draws? What would happen if it played second? What if two intelligent agents faced each other?...  
These questions would be other good examples of analysis that you could have done.

That being said, this doesn't take away from the fact that you've done an excellent job. You've implemented a good algorithm and achieved a satisfactory result. Congratulations!

I wish you the best for the exam, and good luck! Let's not give up now that we're almost at the finish line!


**To Silvio Chito (s309619):**  
Hi Silvio,

I want to start by saying that I appreciate your choice of using a q-learning algorithm.

The code overall is readable and clear, well-commented where necessary, with a clear distinction between different sections and phases of the algorithm – good job!  
I also appreciate the fact that there is a clear and concise README.  
The decision to use a fixed probability for choosing actions at each state by exploiting the epsilon-greedy strategy makes sense and is commendable.

One feature I particularly appreciate is the reward management system. Many, including myself, have relied on simple scores based on whether the player wins, draws, or loses. I find your implementation of rewards clever and original, compliments!

The algorithm is implemented correctly, and for this reason, a more in-depth analysis of the results obtained would have been interesting.

From the code, it's evident that the agent can be trained with both X and O. I appreciate the idea, but a comparison between the two cases would have been useful.  
I've already mentioned that I find the reward management system original, but is it genuinely better than a more simplified version? Your agent achieves a 71% win rate against a random player; how many games does it lose or draw? It would have been interesting to analyze these aspects as well.

In conclusion, the lab has been completed, and there is evident effort on your part to customize and improve a generic q-learning algorithm, well done!

I wish you good luck for the exam and your future exams!
