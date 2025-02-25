# Recursion : 
### Definition : Recursion is a programming technique where a function calls itself to solve a problem.
![alt text](https://www.codesansar.com/storage/app/media/c-programming/recursion.png)

### Thumb Rules : 
* Define a Base Case (Stopping Condition) -> Without a base case, the recursion will continue indefinitely, leading to a stack overflow.
* Ensure Progress Towards the Base Case -> Modify parameters in each recursive call so that it moves closer to the base case.
* Avoid Redundant Computation (Memoization) -> If a recursive function is solving overlapping subproblems (like in Fibonacci), store already computed values to avoid recalculations.
* Local Variables in Recursion -> Every recursive call gets its own copy of local variables.
* Global Variables in Recursion -> Global variables persist but may cause unwanted side effects.


### Multiple Recursion Call : fibonacci of 4 => 3
![alt text](https://www.researchgate.net/publication/278965757/figure/fig1/AS:467532499951616@1488479842204/Cilk-pseudocode-for-a-recursive-program-to-compute-Fibonacci-numbers-main.png)