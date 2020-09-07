# PacManAI
this project is an AI project which can be ran through the command line ulizing the following commands below. 

pacman.py is just a pacman game maze that you can control with the arrow pad
testMaze and tinyMaze pacman GoWestAgent show the pacman agent going west on its own.
pacman.py -h is a help menu that will help you start
the remaining commands will allow you to see the result of the pacman AI


python pacman.py </br>
python pacman.py --layout testMaze --pacman GoWestAgent </br>
python pacman.py --layout tinyMaze --pacman GoWestAgent </br>
python pacman.py -h </br>
python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch </br>
python pacman.py -l tinyMaze -p SearchAgent </br>
python pacman.py -l mediumMaze -p SearchAgent </br>
python pacman.py -l bigMaze -z .5 -p SearchAgent </br>
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs </br>
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5 </br>
python eightpuzzle.py </br>
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs </br>
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent </br>
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent </br>
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic  </br>
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem </br>
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem </br>
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5 </br>
python pacman.py -l testSearch -p AStarFoodSearchAgent </br>
python pacman.py -l trickySearch -p AStarFoodSearchAgent </br>
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 </br>
python pacman.py -l bigSearch -p ApproximateSearchAgent -z .5 -q </br>
</br>
This project uses AI principles in BFS Breadth First Search, and DFS Depth First Search as well as others. </br>
