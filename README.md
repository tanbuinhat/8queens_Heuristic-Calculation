# 8queens_Heuristic-Calculation


Given an 8x8 chess board, on which 8 queens are available in any 8 positions with the constraint that each column has at least one queen. For example, as shown below.






<img width="514" alt="Screen Shot 2021-03-17 at 20 35 15" src="https://user-images.githubusercontent.com/60350737/111476640-ed227280-8760-11eb-9262-26cce7f2e759.png">


Heuristic function h (x) is defined as the number of queens that can attack each other, directly or indirectly. For example, the upper left state h (x) = 17, the right state has h (x) = 1. 



Requirements: With the given state as above of the chess board. Calculate the value of the function h (x) in the cells of the matrix when moving the queens to that position. Know that in any state of the board, queens can be moved vertically from the position where they are standing. 
