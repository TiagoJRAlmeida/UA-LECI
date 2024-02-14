//
// Algoritmos e Estruturas de Dados --- 2023/2024
//
// Joaquim Madeira, Joao Manuel Rodrigues - June 2021, Nov 2023
//
// GraphBFS - QUEUE-based Breadth-First Search
//

#include "GraphBFSWithQueue.h"

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "Graph.h"
#include "IntegersQueue.h"
#include "IntegersStack.h"

struct _GraphBFSWithQueue {
  int* marked;       // To mark vertices when reached for the first time
  int* distance;     // The number of edges on the path from the start vertex
  int* predecessor;  // The predecessor vertex, when a vertex was reached
  Graph* graph;
  unsigned int startVertex;
};


static void _bfsWithQueue(GraphBFSWithQueue* traversal, unsigned int vertex) {
	unsigned int* neighbors;
  Queue* q = QueueCreate(GraphGetNumVertices(traversal->graph));
	
	QueueEnqueue(q, vertex);
	traversal->marked[vertex] = 1;
  traversal->distance[vertex] = 0;
	
  // Enquanto a queue não estiver vazia
	while(QueueIsEmpty(q) == 0){ 
    
		// QueueDequeue devolve o vertice da queue no indice da head, e incrementa a head;
    int NewVertex = QueueDequeue(q);
    
    // neighbors é a lista dos vertices adjacentes(ligados) ao vertix escolhido;
    // Nota: neighbors[0] é o numero de vertices adjancentes;
    neighbors = GraphGetAdjacentsTo(traversal->graph, NewVertex); 
		
    for (unsigned int i = 1; i <= neighbors[0]; i++){
			unsigned int w = neighbors[i];
			if(traversal->marked[w] == 0){
				QueueEnqueue(q, w);
				traversal->marked[w] = 1;
        traversal->predecessor[w] = NewVertex;
        traversal->distance[w] = traversal->distance[NewVertex] + 1;
			}
		}
	}
	
	free(neighbors);
}

GraphBFSWithQueue* GraphBFSWithQueueExecute(Graph* g, unsigned int startVertex) {
  assert(g != NULL);
  assert(startVertex < GraphGetNumVertices(g));

  GraphBFSWithQueue* traversal = (GraphBFSWithQueue*)malloc(sizeof(struct _GraphBFSWithQueue));
  assert(traversal != NULL);

  unsigned int numVertices = GraphGetNumVertices(g);

  // Inicia a variavel 'marked' de 'traversal', que é uma array de inteiros positivos, com todos os valores = 0;
  traversal->marked = (int*)calloc(numVertices, sizeof(unsigned int));
  assert(traversal->marked != NULL);

  // Inicia a variavel 'distance' de 'traversal', que é uma array de inteiros, com os valores não iniciados;
  traversal->distance = (int*)malloc(numVertices * sizeof(int));
  assert(traversal->distance != NULL);

  // Inicia a variavel 'predecessor' de 'traversal', que é uma array de inteiros, com todos os valores = -1;
  traversal->predecessor = (int*)malloc(numVertices * sizeof(int));
  assert(traversal->predecessor != NULL);
  for (unsigned int i = 0; i < numVertices; i++) {
    traversal->predecessor[i] = -1;
  }

  traversal->predecessor[startVertex] = 0;

  // Inicia as variaveis 'graph' e 'startVertex' de 'traversal';
  traversal->graph = g;
  traversal->startVertex = startVertex;

  traversal->graph = g;
  traversal->startVertex = startVertex;

  // CARRY OUT THE TRAVERSAL
  _bfsWithQueue(traversal, startVertex);

  return traversal;
}

void GraphBFSWithQueueDestroy(GraphBFSWithQueue** p) {
  assert(*p != NULL);

  GraphBFSWithQueue* aux = *p;

  free(aux->marked);
  free(aux->predecessor);

  free(*p);
  *p = NULL;
}

// Getting the result

int GraphBFSWithQueueHasPathTo(const GraphBFSWithQueue* p, unsigned int v) {
  assert(p != NULL);
  assert(v < GraphGetNumVertices(p->graph));

  return p->marked[v];
}

Stack* GraphBFSWithQueuePathTo(const GraphBFSWithQueue* p, unsigned int v) {
  assert(p != NULL);
  assert(v < GraphGetNumVertices(p->graph));

  Stack* s = StackCreate(GraphGetNumVertices(p->graph));

  if (p->marked[v] == 0) {
    return s;
  }

  // Store the path
  for (unsigned int current = v; current != p->startVertex;
       current = p->predecessor[current]) {
    StackPush(s, current);
  }

  StackPush(s, p->startVertex);

  return s;
}

// DISPLAYING on the console

void GraphBFSWithQueueShowPath(const GraphBFSWithQueue* p, unsigned int v) {
  assert(p != NULL);
  assert(v < GraphGetNumVertices(p->graph));

  Stack* s = GraphBFSWithQueuePathTo(p, v);

  while (StackIsEmpty(s) == 0) {
    printf("%d ", StackPop(s));
  }

  StackDestroy(&s);
}

void GraphBFSWithQueueDisplay(const GraphBFSWithQueue* p) {
  assert(p != NULL);

  // TO BE COMPLETED !!
}
