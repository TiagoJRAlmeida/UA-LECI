//
// Joaquim Madeira, AlgC, June 2021
// João Manuel Rodrigues, AlgC, June 2021
//
// Graph EXAMPLE : The different traversals
//

#include "Graph.h"
#include "GraphBFSWithQueue.h"
#include "GraphDFSRec.h"
#include "GraphDFSWithStack.h"

int main(void) {
  Graph* g01 = GraphCreate(6, 0, 0);

  GraphAddEdge(g01, 0, 5);
  GraphAddEdge(g01, 2, 4);
  GraphAddEdge(g01, 2, 3);
  GraphAddEdge(g01, 1, 2);
  GraphAddEdge(g01, 0, 1);
  GraphAddEdge(g01, 3, 4);
  GraphAddEdge(g01, 3, 5);
  GraphAddEdge(g01, 0, 2);

  GraphDisplay(g01);

  // Recursive DFS traversal

  printf("RECURSIVE DFS traversal\n");
  GraphDFSRec* traversalRec = GraphDFSRecExecute(g01, 0);

  printf("Path from 0 to 5: ");
  GraphDFSRecShowPath(traversalRec, 5);
  printf("\n");

  GraphDFSRecDestroy(&traversalRec);

  // STACK-based DFS traversal

  printf("DFS traversal with STACK\n");
  GraphDFSWithStack* traversalWithStack = GraphDFSWithStackExecute(g01, 0);

  printf("Path from 0 to 5: ");
  GraphDFSWithStackShowPath(traversalWithStack, 5);
  printf("\n");

  GraphDFSWithStackDestroy(&traversalWithStack);

  // QUEUE-based BFS traversal
  /*
  printf("BFS traversal with QUEUE\n");
  GraphBFSWithQueue* traversalWithQueue = GraphBFSWithQueueExecute(g01, 0);

  printf("Path from 0 to 5: ");
  GraphBFSWithQueueShowPath(traversalWithQueue, 5);
  printf("\n");

  GraphBFSWithQueueDestroy(&traversalWithQueue);

  GraphDestroy(&g01); 
  */
  return 0;
}
