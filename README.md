# 8-puzzle_python



# Input : 
1. There are four input files input_bfs,input_dfs,input_ucs,input_bds.
2. For new testcases remove the existing text case in the respective file and add the new one (single test case in a file ).

# Output :
1. The output is shown on the commandline.

#How to run 
1. `python ` <filename (input_bfs,input_dfs,input_ucs,input_bds)>


#standard deviation :

After running the program, these were our observations (on 4 experiments):
                                                     
							        costs:
		      MEAN of BFS = 6.5 steps or cost          5,16,2,3
                      MEAN of DFS = 10.25 steps or cost        2,3,33,3
                      MEAN of bidirectional = 4 steps or cost  2,4,4,6
                      MEAN of uniform_cost ~ > 3.25 cost       5,3,3,2

                      S.D of BFS = 6.45497
                      S.D of DFS = 15.17399
                      S.D of bidirectional = 1.63299
                      S.D of uniform_cost = 1.25831
