//
// Algoritmos e Estruturas de Dados --- 2023/2024
//
// Joaquim Madeira, Joao Manuel Rodrigues - June 2021, Nov 2023
//
// GraphDFSRec - RECURSIVE Depth-First Search
//

#include "GraphDFSRec.h"

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "Graph.h"
#include "IntegersStack.h"

struct _GraphDFSRec { // marked e predecessor são arrays, por isso é que são pointers
  unsigned int* marked;  // To mark vertices when reached for the first time
  int* predecessor;      // The predecessor vertex, when a vertex was reached
  Graph* graph;
  unsigned int startVertex;
};


//
// Notas: Esta é a função principal e mais importante; dfs = Depth First;
// Função recursiva, que passa por todos os vertices de um grafo, começando por um escolhido;
// Esta função tem dois objetivos:
// 1) Registar os vertices pelos quais se passam são marcados (traversal->marked[v] = 1) para que não haja ações repetidas;
// 2) Registar os 'predecessor' de cada vertice (vertice imediatamente antes de chegar a cada vertice);
//
static void _dfs(GraphDFSRec* traversal, unsigned int vertex) { // Recebe o pointer para um GraphDFSRec e o valor do vertice
  traversal->marked[vertex] = 1; // Indica que já passou pelo vertice indicado nos argumentos

  unsigned int* neighbors = GraphGetAdjacentsTo(traversal->graph, vertex); // neighbors é a lista dos vertices adjacentes(ligados) ao vertix escolhido
  for (unsigned int i = 1; i <= neighbors[0]; i++) {                      // Nota: neighbors[0] é o numero de vertices adjancentes
    unsigned int w = neighbors[i];
    if (traversal->marked[w] == 0) { // Verifica se já passou pelo vertice em loop ou não
      traversal->predecessor[w] = vertex; 
      _dfs(traversal, w); // chama-se o metodo novamente, desta vez no vertice em loop
    }
  }

  free(neighbors);
}

//
// Cria uma variavel do tipo struct GraphDFSRec, inicia os seus valores,
// chama a função recursiva anterior (_dfs) para passar por todos os vertices
// e registar os antecessores de cada um, e retorna a variavel;
//
GraphDFSRec* GraphDFSRecExecute(Graph* g, unsigned int startVertex) {
  assert(g != NULL);
  assert(startVertex < GraphGetNumVertices(g));

  GraphDFSRec* result = (GraphDFSRec*)malloc(sizeof(struct _GraphDFSRec)); 
  assert(result != NULL);

  unsigned int numVertices = GraphGetNumVertices(g);

  result->marked = (unsigned int*)calloc(numVertices, sizeof(unsigned int));
  assert(result->marked != NULL);

  result->predecessor = (int*)malloc(numVertices * sizeof(int));
  assert(result->predecessor != NULL);
  for (unsigned int i = 0; i < numVertices; i++) {
    result->predecessor[i] = -1;
  }

  result->predecessor[startVertex] = 0;

  result->graph = g;
  result->startVertex = startVertex; // Tudo até agora serviu para iniciar a struct result;

  // START THE RECURSIVE TRAVERSAL

  _dfs(result, startVertex); // Chama a função recursiva anterior para passar por todos os vertices  
                            // e marcar o antecessor de cada um;
  return result;
}

//
// Nada demais sobre esta função.
// Apenas apaga uma instancia da strutura.
//
void GraphDFSRecDestroy(GraphDFSRec** p) {
  assert(*p != NULL);

  GraphDFSRec* aux = *p;

  free(aux->marked);
  free(aux->predecessor);

  free(*p);
  *p = NULL;
}


// Getting the result

//
// Apenas verifica se a função recursiva depth-first chegou a um vertice escolhido ou não; 
// 1 = chegou ao vertice; 0 = não chegou ao vertice;
//
unsigned int GraphDFSRecHasPathTo(const GraphDFSRec* p, unsigned int v) {
  assert(p != NULL);
  assert(v < GraphGetNumVertices(p->graph));

  return p->marked[v];
}

//
// Cria e devolve uma stack onde se guarda o caminho por ordem desde  
// o vertice escolhido(primeiro elemento da stack) até chegar ao vertice inicial(ultimo elemento da stack);
//
Stack* GraphDFSRecPathTo(const GraphDFSRec* p, unsigned int v) {
  assert(p != NULL);
  assert(v < GraphGetNumVertices(p->graph));

  Stack* s = StackCreate(GraphGetNumVertices(p->graph)); // Cria uma stack de tamanho = Numero de vertices;

  if (p->marked[v] == 0) { // Se o vertice não estiver marcado, significa que não há 
    return s;             // caminho para ele, logo devolve-se a stack vazia;
  }

  // Store the path
  for (unsigned int current = v; current != p->startVertex; current = p->predecessor[current]) {
    StackPush(s, current); // Anda-se de forma recursiva, começando no vertice escolhido e acabando no vertice inicial
  }                       // e indo inserindo os vertices pelo caminhona stack;

  StackPush(s, p->startVertex); // O ultimo vertice a ser inserido na stack é o vertice inicial, completando assim o caminho

  return s;
}


// DISPLAYING on the console

//
// Dá print aos valores da stack, gerado pela função GraphDFSRecPathTo;
// Ou seja, dá print ao caminho, desde o vertice escolhido, até ao vertice inicial;
//
void GraphDFSRecShowPath(const GraphDFSRec* p, unsigned int v) {
  assert(p != NULL);
  assert(v < GraphGetNumVertices(p->graph));

  Stack* s = GraphDFSRecPathTo(p, v);

  while (StackIsEmpty(s) == 0) {
    printf("%d ", StackPop(s));
  }

  StackDestroy(&s);
}

void GraphDFSRecDisplay(const GraphDFSRec* p) {
  assert(p != NULL);

  // TO BE COMPLETED !!
}
