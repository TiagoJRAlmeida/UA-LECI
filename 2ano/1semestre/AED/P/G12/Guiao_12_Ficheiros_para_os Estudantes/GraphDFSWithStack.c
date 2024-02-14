//
// Algoritmos e Estruturas de Dados --- 2023/2024
//
// Joaquim Madeira, Joao Manuel Rodrigues - June 2021, Nov 2023
//
// GraphDFS - STACK-based Depth-First Search
//

#include "GraphDFSWithStack.h"

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "Graph.h"
#include "IntegersStack.h"

struct _GraphDFSWithStack {
  int* marked;       // To mark vertices when reached for the first time
  int* predecessor;  // The predecessor vertex, when a vertex was reached
  Graph* graph;
  unsigned int startVertex;
};


static void _dfsWithStack(GraphDFSWithStack* traversal, unsigned int vertex) {
	unsigned int* neighbors;
  Stack* s = StackCreate(GraphGetNumVertices(traversal->graph));
	
	StackPush(s, vertex);
	traversal->marked[vertex] = 1;
	
  // Enquanto a stack não estiver vazia
	while(StackIsEmpty(s) == 0){ 
    
		// StackPop devolve o ultimo e decrementa o argumento cur_size da stack;
    int LastVertex = StackPop(s);
    
    // neighbors é a lista dos vertices adjacentes(ligados) ao vertix escolhido;
    // Nota: neighbors[0] é o numero de vertices adjancentes;
    neighbors = GraphGetAdjacentsTo(traversal->graph, LastVertex); 
		
    for (unsigned int i = 1; i <= neighbors[0]; i++){
			unsigned int w = neighbors[i];
			if(traversal->marked[w] == 0){
				StackPush(s, w);
				traversal->marked[w] = 1;
        traversal->predecessor[w] = LastVertex;
			}
		}
	}
	
	free(neighbors);
}


GraphDFSWithStack* GraphDFSWithStackExecute(Graph* g, unsigned int startVertex) {
  assert(g != NULL);
  assert(startVertex < GraphGetNumVertices(g));

  // Inicia um instancia da estrutura GraphDFSWithStack com o nome 'traversal';
  GraphDFSWithStack* traversal = (GraphDFSWithStack*)malloc(sizeof(struct _GraphDFSWithStack));
  assert(traversal != NULL);

  unsigned int numVertices = GraphGetNumVertices(g);

  // Inicia a variavel 'marked' de 'traversal', que é uma array de inteiros positivos, com todos os valores = 0;
  traversal->marked = (int*)calloc(numVertices, sizeof(unsigned int));
  assert(traversal->marked != NULL);

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

  // CARRY OUT THE TRAVERSAL

  _dfsWithStack(traversal, startVertex);

  return traversal;
}

void GraphDFSWithStackDestroy(GraphDFSWithStack** p) {
  assert(*p != NULL);

  GraphDFSWithStack* aux = *p;

  free(aux->marked);
  free(aux->predecessor);

  free(*p);
  *p = NULL;
}

// Getting the result

int GraphDFSWithStackHasPathTo(const GraphDFSWithStack* p, unsigned int v) {
  assert(p != NULL);
  assert(v < GraphGetNumVertices(p->graph));

  return p->marked[v];
}

Stack* GraphDFSWithStackPathTo(const GraphDFSWithStack* p, unsigned int v) {
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

void GraphDFSWithStackShowPath(const GraphDFSWithStack* p, unsigned int v) {
  assert(p != NULL);
  assert(v < GraphGetNumVertices(p->graph));

  Stack* s = GraphDFSWithStackPathTo(p, v);

  while (StackIsEmpty(s) == 0) {
    printf("%d ", StackPop(s));
  }

  StackDestroy(&s);
}

void GraphDFSWithStackDisplay(const GraphDFSWithStack* p) {
  assert(p != NULL);

  // TO BE COMPLETED !!
}
