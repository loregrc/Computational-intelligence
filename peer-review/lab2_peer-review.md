# Lab2: Peer-review
These are my peer-reviews for the second lab.

**To Alessandro De Marco (s317626):**  
Hello Alessandro,
I find your idea of characterizing the genome very clever. By leveraging nimsum as a spectrum of possible choices, your strategy, regardless of the number of wins per generation (which, however, increases significantly over generations), has great evolutionary potential, as evidenced by the collected data, where the population initially randomly targeting all nimsum values tends to concentrate in a specific range as it evolves.  
I also appreciate providing two methods of parent selection because it provides a more in-depth view of the problem, highlighting aspects that often take a back seat, such as convergence speed and population diversity.  
Regarding the crossover function, I appreciate the idea of having a bias that influences the result (with the check if total_fitness > 0).  
The mutation is standard but efficient.  
Overall, the code is well-structured and very readable. The efforts to plot all the results to make them clear are commendable, and the report is simple but effective, containing everything one needs to know and providing an excellent guide to understanding your code.  
Well done, and good luck with the upcoming labs!

**To Antonio Ferrigno (s316467):**  
Hi Antonio,
Your evolutionary strategy consists of choosing moves based on those that lead to a safe condition, exploiting knowledge of the ideal nimsum. If this is not possible or we are already in a safe condition, you call a function that chooses the move based on the individual's genome.  
In my opinion, what is not good about this approach is that the choice is based on the best possible move at the moment.  
This is incorrect because in evolutionary strategies, in theory, the best move or the optimal strategy is not known. This is precisely why evolutionary strategies are used because the goal is to approach the optimal without knowing it, through the evolution of generations.  
In your case, the strategy is the optimal one with the exception of when it is not possible, and then the genome intervenes, making a pseudo-random choice. Overall, it is therefore an optimal strategy that leaves little room for evolution.  
Furthermore, during the population evaluation phase, they play against themselves. In a more realistic context, this would lead to little evolution in the species and a local minimum.  
That being said, I appreciate the idea of ​​valuing quick wins.
It is also commendable the effort to plot various graphs and statistics.  
Overall, the code, regardless of its correctness or not, is well-readable.  
Good luck with the next labs!