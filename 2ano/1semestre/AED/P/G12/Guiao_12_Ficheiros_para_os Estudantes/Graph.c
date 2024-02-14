//
// Algoritmos e Estruturas de Dados --- 2023/2024
//
// Joaquim Madeira, Joao Manuel Rodrigues - June 2021, Nov 2023
//
// Graph - Using a list of adjacency lists representation
//

#include "Graph.h"

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "SortedList.h"

struct _Vertex {
  unsigned int id;
  unsigned int inDegree;
  unsigned int outDegree;
  List* edgesList;
};

struct _Edge {
  unsigned int adjVertex;
  double weight;
};

struct _GraphHeader {
  int isDigraph;
  int isComplete;
  int isWeighted;
  unsigned int numVertices;
  unsigned int numEdges;
  List* verticesList;
};

// The comparator for the VERTICES LIST
// Nota: Esta função retorna o tipo compFunc (Definido em SortedList.h);
int graphVerticesComparator(const void* p1, const void* p2) { 
  unsigned int v1 = ((struct _Vertex*)p1)->id;
  unsigned int v2 = ((struct _Vertex*)p2)->id;
  int d = v1 - v2;
  return (d > 0) - (d < 0);
}

// The comparator for the EDGES LISTS
// Nota: Esta função retorna o tipo compFunc (Definido em SortedList.h);
int graphEdgesComparator(const void* p1, const void* p2) {
  unsigned int v1 = ((struct _Edge*)p1)->adjVertex;
  unsigned int v2 = ((struct _Edge*)p2)->adjVertex;
  int d = v1 - v2;
  return (d > 0) - (d < 0);
}

Graph* GraphCreate(unsigned int numVertices, int isDigraph, int isWeighted) {
  Graph* g = (Graph*)malloc(sizeof(struct _GraphHeader));
  if (g == NULL) abort();

  g->isDigraph = isDigraph;
  g->isComplete = 0;
  g->isWeighted = isWeighted;

  g->numVertices = numVertices;
  g->numEdges = 0;

  g->verticesList = ListCreate(graphVerticesComparator);

  for (unsigned int i = 0; i < numVertices; i++) {
    struct _Vertex* v = (struct _Vertex*)malloc(sizeof(struct _Vertex));
    if (v == NULL) abort();

    v->id = i;
    v->inDegree = 0;
    v->outDegree = 0;

    v->edgesList = ListCreate(graphEdgesComparator);

    ListInsert(g->verticesList, v);
  }

  assert(g->numVertices == ListGetSize(g->verticesList));

  return g;
}

Graph* GraphCreateComplete(unsigned int numVertices, int isDigraph) {
  Graph* g = GraphCreate(numVertices, isDigraph, 0);

  g->isComplete = 1;

  List* vertices = g->verticesList;
  ListMoveToHead(vertices);
  
  for (unsigned int i = 0; i < g->numVertices; ListMoveToNext(vertices), i++) {
    struct _Vertex* v = ListGetCurrentItem(vertices);
    List* edges = v->edgesList;
    for (unsigned int j = 0; j < g->numVertices; j++) {
      if (i == j) {
        continue;
      }
      struct _Edge* new = (struct _Edge*)malloc(sizeof(struct _Edge));
      if (new == NULL) abort();
      new->adjVertex = j;
      new->weight = 1;

      ListInsert(edges, new);
    }
    if (g->isDigraph) {
      v->inDegree = g->numVertices - 1;
      v->outDegree = g->numVertices - 1;
    } else {
      v->outDegree = g->numVertices - 1;
    }
  }
  if (g->isDigraph) {
    g->numEdges = numVertices * (numVertices - 1);
  } else {
    g->numEdges = numVertices * (numVertices - 1) / 2;
  }

  return g;
}

void GraphDestroy(Graph** p) {
  assert(*p != NULL);
  Graph* g = *p;

  List* vertices = g->verticesList;
  if (ListIsEmpty(vertices) == 0) {
    ListMoveToHead(vertices);
    unsigned int i = 0;
    for (; i < g->numVertices; ListMoveToNext(vertices), i++) {
      struct _Vertex* v = ListGetCurrentItem(vertices);

      List* edges = v->edgesList;
      if (ListIsEmpty(edges) == 0) {
        unsigned int i = 0;
        ListMoveToHead(edges);
        for (; i < ListGetSize(edges); ListMoveToNext(edges), i++) {
          struct _Edge* e = ListGetCurrentItem(edges);
          free(e);
        }
      }
      ListDestroy(&(v->edgesList));
      free(v);
    }
  }

  ListDestroy(&(g->verticesList));
  free(g);

  *p = NULL;
}

// Como fazer a copia de um grafo: fazer um grafo novo e ir ao grafo original e copiar as ligações + vertices 
Graph* GraphCopy(const Graph* g) {
  assert(g != NULL);
  printf("\n\n\n --- GRAPH COPY ----\n\n\n");
  // Criar um grafo novo;
  Graph* newGraph = GraphCreate(g->numVertices, g->isDigraph, g->isWeighted);
  assert(newGraph != NULL);

  // Copiar o numero de arestas;
  newGraph->numEdges = g->numEdges;

  //
  // Iniciar o processo de copiar vertices;
  //
  // Loop por todos os vertices, e dar valor a cada um;
  for (unsigned int i = 0; i < newGraph->numVertices; i++) {

    // Buscar o vertice original;
    ListMove(g->verticesList, i);
    struct _Vertex* originalVertex = (struct _Vertex*)ListGetCurrentItem(g->verticesList);

    //
    // Iniciar o processo de copiar as arestas;
    //
    unsigned int numOfEdges = ListGetSize(originalVertex->edgesList);
    for (unsigned int i = 0; i < numOfEdges; i++){
      ListMove(originalVertex->edgesList, i);
      struct _Edge* originalEdge = (struct _Edge*)ListGetCurrentItem(originalVertex->edgesList);

      if(g->isWeighted)
        GraphAddWeightedEdge(newGraph, originalVertex->id, originalEdge->adjVertex, originalEdge->weight);
      else  
        GraphAddEdge(newGraph, originalVertex->id, originalEdge->adjVertex);
    }
  }

  assert(newGraph->numVertices == ListGetSize(newGraph->verticesList));

  return newGraph;
}


//FORMATO:
//0 / 1 É grafo orientado ?
//0 / 1 Há pesos associados às arestas ?
//Número de vértices
//Número de arestas
//vértice inicial vértice final (peso, se existir)
//....
Graph* GraphFromFile(FILE* f) {
  assert(f != NULL);

  int isDigraph, isWeighted, numVertices, numEdges, vertex1, vertex2;
  double weight;

  // Ler se o grafo é orientado;
  if (fscanf(f, "%d", &isDigraph) != 1) {
      perror("Error reading graph type");
      fclose(f);
      return NULL;
  }

  // Ler se o grafo tem pesos;
  if (fscanf(f, "%d", &isWeighted) != 1) {
      perror("Error reading graph type");
      fclose(f);
      return NULL;
  }
  
  // Ler o numero de vertices;
  if (fscanf(f, "%d", &numVertices) != 1) {
      perror("Error reading number of vertices");
      fclose(f);
      return NULL;
  }

  // Ler o numero de arestas;
  if (fscanf(f, "%d", &numEdges) != 1) {
      perror("Error reading number of edges");
      fclose(f);
      return NULL;
  }
  
  // Cria o grafo com os valores lidos;
  Graph* g = GraphCreate(numVertices, isDigraph, isWeighted);

  // Ler os vértices nas restantes linhas e adicionar a aresta;
  if(isWeighted){
    while (fscanf(f, "%d %d %lf", &vertex1, &vertex2, &weight) == 3) {
      GraphAddWeightedEdge(g, vertex1, vertex2, weight);
    }
  }
  else{
    while (fscanf(f, "%d %d", &vertex1, &vertex2) == 2) {    
      GraphAddEdge(g, vertex1, vertex2);
    }
  }

  // Fechar o ficheiro;
  fclose(f);

  return g;
}

// Graph

int GraphIsDigraph(const Graph* g) { return g->isDigraph; }

int GraphIsComplete(const Graph* g) { return g->isComplete; }

int GraphIsWeighted(const Graph* g) { return g->isWeighted; }

unsigned int GraphGetNumVertices(const Graph* g) { return g->numVertices; }

unsigned int GraphGetNumEdges(const Graph* g) { return g->numEdges; }

//
// For a graph
//
double GraphGetAverageDegree(const Graph* g) {
  assert(g->isDigraph == 0);
  return 2.0 * (double)g->numEdges / (double)g->numVertices;
}

static unsigned int _GetMaxDegree(const Graph* g) {
  List* vertices = g->verticesList;
  if (ListIsEmpty(vertices)) return 0;

  unsigned int maxDegree = 0;
  ListMoveToHead(vertices);
  unsigned int i = 0;
  for (; i < g->numVertices; ListMoveToNext(vertices), i++) {
    struct _Vertex* v = ListGetCurrentItem(vertices);
    if (v->outDegree > maxDegree) {
      maxDegree = v->outDegree;
    }
  }
  return maxDegree;
}

//
// For a graph
//
unsigned int GraphGetMaxDegree(const Graph* g) {
  assert(g->isDigraph == 0);
  return _GetMaxDegree(g);
}

//
// For a digraph
//
unsigned int GraphGetMaxOutDegree(const Graph* g) {
  assert(g->isDigraph == 1);
  return _GetMaxDegree(g);
}

// Vertices

//
// returns an array of size (outDegree + 1)                     |
// element 0, stores the number of adjacent vertices            } Isto explica tudo o que é preciso saber
// and is followed by indices of the adjacent vertices          |
//
unsigned int* GraphGetAdjacentsTo(const Graph* g, unsigned int v) {
  assert(v < g->numVertices);

  // Node in the list of vertices
  List* vertices = g->verticesList;
  ListMove(vertices, v); // Move lista de forma a estar a apontar para o vertice v(vertices->currentPos = v);
  struct _Vertex* vPointer = ListGetCurrentItem(vertices); 
  unsigned int numAdjVertices = vPointer->outDegree; // Numero de vertices adjacente = Grau(quantidade de arestas) a sair do vertice em estudo

  unsigned int* adjacent = (unsigned int*)calloc(1 + numAdjVertices, sizeof(unsigned int)); //adjancent é uma array de ints com size = numAdjVertices + 1

  if (numAdjVertices > 0) { 
    adjacent[0] = numAdjVertices;
    List* adjList = vPointer->edgesList; 
    ListMoveToHead(adjList);
    for (unsigned int i = 0; i < numAdjVertices; ListMoveToNext(adjList), i++) {
      struct _Edge* ePointer = ListGetCurrentItem(adjList);
      adjacent[i + 1] = ePointer->adjVertex;
    }
  }

  return adjacent;
}

//
// returns an array of size (outDegree + 1)
// element 0, stores the number of adjacent vertices
// and is followed by the distances to the adjacent vertices
//
double* GraphGetDistancesToAdjacents(const Graph* g, unsigned int v) {
  assert(v < g->numVertices);

  // Node in the list of vertices
  List* vertices = g->verticesList;
  ListMove(vertices, v);
  struct _Vertex* vPointer = ListGetCurrentItem(vertices);
  unsigned int numAdjVertices = vPointer->outDegree;

  double* distance = (double*)calloc(1 + numAdjVertices, sizeof(double));

  if (numAdjVertices > 0) {
    distance[0] = numAdjVertices;
    List* adjList = vPointer->edgesList;
    ListMoveToHead(adjList);
    for (unsigned int i = 0; i < numAdjVertices; ListMoveToNext(adjList), i++) {
      struct _Edge* ePointer = ListGetCurrentItem(adjList);
      distance[i + 1] = ePointer->weight;
    }
  }

  return distance;
}

//
// For a graph
//
unsigned int GraphGetVertexDegree(Graph* g, unsigned int v) {
  assert(g->isDigraph == 0);
  assert(v < g->numVertices);

  ListMove(g->verticesList, v);
  struct _Vertex* p = ListGetCurrentItem(g->verticesList);

  return p->outDegree;
}

//
// For a digraph
//
unsigned int GraphGetVertexOutDegree(Graph* g, unsigned int v) {
  assert(g->isDigraph == 1);
  assert(v < g->numVertices);

  ListMove(g->verticesList, v);
  struct _Vertex* p = ListGetCurrentItem(g->verticesList);

  return p->outDegree;
}

//
// For a digraph
//
unsigned int GraphGetVertexInDegree(Graph* g, unsigned int v) {
  assert(g->isDigraph == 1);
  assert(v < g->numVertices);

  ListMove(g->verticesList, v);
  struct _Vertex* p = ListGetCurrentItem(g->verticesList);

  return p->inDegree;
}

// Edges

static int _addEdge(Graph* g, unsigned int v, unsigned int w, double weight) {
  // Adicionar a aresta na direção v->w;
  struct _Edge* edge = (struct _Edge*)malloc(sizeof(struct _Edge));
  edge->adjVertex = w;
  edge->weight = weight;

  ListMove(g->verticesList, v);
  struct _Vertex* vertex = ListGetCurrentItem(g->verticesList);
  int result = ListInsert(vertex->edgesList, edge);

  if (result == -1) {
    return 0;
  } else {
    g->numEdges++;
    vertex->outDegree++;

    ListMove(g->verticesList, w);
    struct _Vertex* destVertex = ListGetCurrentItem(g->verticesList);
    destVertex->inDegree++;
  }

  // Se não for orientado, adicionar a aresta novamente, mas desta vez na direção w->v;
  if (g->isDigraph == 0) {
    // Bidirectional edge
    struct _Edge* edge = (struct _Edge*)malloc(sizeof(struct _Edge));
    edge->adjVertex = v;
    edge->weight = weight;

    ListMove(g->verticesList, w);
    struct _Vertex* vertex = ListGetCurrentItem(g->verticesList);
    result = ListInsert(vertex->edgesList, edge);

    if (result == -1) {
      return 0;
    } else {
      // g->numEdges++; // Do not count the same edge twice on a undirected
      // graph !!
      vertex->outDegree++;
    }
  }

  return 1;
}

int GraphAddEdge(Graph* g, unsigned int v, unsigned int w) {
  assert(g->isWeighted == 0);
  assert(v != w);
  assert(v < g->numVertices);
  assert(w < g->numVertices);

  return _addEdge(g, v, w, 1.0);
}

int GraphAddWeightedEdge(Graph* g, unsigned int v, unsigned int w, double weight) {
  assert(g->isWeighted == 1);
  assert(v != w);
  assert(v < g->numVertices);
  assert(w < g->numVertices);

  return _addEdge(g, v, w, weight);
}

static int _removeEdge(Graph* g, unsigned int v, unsigned int w){
  // Buscar o vertice indicado a partir do seu id dado;
  ListMove(g->verticesList, v);
  struct _Vertex* vertex = (struct _Vertex*)ListGetCurrentItem(g->verticesList);
  unsigned int numEdges = ListGetSize(vertex->edgesList); 

  // Loop por cada aresta ligada ao vertice;
  for(unsigned int i = 0; i < numEdges; i++){
    ListMove(vertex->edgesList, i);
    struct _Edge* edge = (struct _Edge*)ListGetCurrentItem(vertex->edgesList);

    // Verificar se a aresta em loop é a que queremos apagar (verifica-mos através do vertice adjacente);
    if(edge->adjVertex == w){
      ListRemoveCurrent(vertex->edgesList);
      return 1;
    }
  }

  // Se não for apagado nenhuma aresta, retorna-se 0, para indicar que não houve efeito nenhum no grafo;
  return 0;
}

int GraphRemoveEdge(Graph* g, unsigned int v, unsigned int w) {
  assert(g != NULL);
  assert(v < GraphGetNumVertices(g));

  // Remover a aresta na direção v->w
  if(_removeEdge(g, v, w) == 0){ return 0; }

  // Buscar o vertice indicado a partir do seu id dado;
  ListMove(g->verticesList, v);
  struct _Vertex* vertex = (struct _Vertex*)ListGetCurrentItem(g->verticesList);

  // Buscar o vertice destino a partir do seu id dado;
  ListMove(g->verticesList, w);
  struct _Vertex* destVertex = (struct _Vertex*)ListGetCurrentItem(g->verticesList);

  // Decrementar o numero de arestas, o grau de saida do vertice inicial e o grau de entrada do vertice destino;
  g->numEdges--;
  vertex->outDegree--;
  destVertex->inDegree--;

  // Se o grafo não for orientado, tem de se remover a aresta no sentido contrário (w->v);
  if(g->isDigraph == 0){
    destVertex->outDegree--;
    return _removeEdge(g, w, v);
  }

  // Retorna 1 se tiver corrido tudo bem;
  return 1;
}

// CHECKING

// Função auxiliar que dá o numero de vertices de cada função completa, dependendo do numero de vertices;
static unsigned int GraphCompleteNumEdges(unsigned int numVertices){ return (numVertices * (numVertices - 1)) / 2; }

int GraphCheckInvariants(const Graph* g) {
  assert(g != NULL);
  ListMoveToHead(g->verticesList);
  
  // Verificar se o numero de arestas está correto (para o caso em que o grafo é completo e quando não o é);
  if(g->isComplete == 1 && GraphGetNumEdges(g) != GraphCompleteNumEdges(GraphGetNumVertices(g)))
    return -1;
  else if(g->isComplete == 0 && GraphGetNumEdges(g) >= GraphCompleteNumEdges(GraphGetNumVertices(g)))
    return -1;
  
  // Loop por cada vertice;
  for(unsigned int i = 0; i < GraphGetNumVertices(g); i++){
    struct _Vertex* v = (struct _Vertex*)ListGetCurrentItem(g->verticesList);
    ListMoveToHead(v->edgesList);

    // Verificar se o outDegree é igual ao numero de arestas do vertice;
    if(v->outDegree != ListGetSize(v->edgesList))
      return -1;

    // Loop por cada aresta do vertice atualmente em loop;  
    for(unsigned int j = 0; j < ListGetSize(v->edgesList); j++){
      struct _Edge* edge = (struct _Edge*)ListGetCurrentItem(v->edgesList);

      // verificar se nenhuma aresta tem peso negativo no caso do grafo ser pesado;
      if(g->isWeighted == 1 && edge->weight < 0)
        return -1;

      // verificar se todas as arestas tem peso igual a zero no caso do grafo não ser pesado;
      else if(g->isWeighted == 0 && edge->weight != 0) 
        return -1;
    }
  }

  // Verificar se o numero de vertices que o grafo indica no argumento numVertices e 
  // o tamanho da lista com os vertices do grafo é concistente;
  if(GraphGetNumVertices(g) != ListGetSize(g->verticesList))
    return -1;

  // Se não tiver retornado -1 até agora, significa que passou todos os testes, então retorna 0; 
  return 0;
}

// DISPLAYING on the console

void GraphDisplay(const Graph* g) {
  printf("---\n");
  if (g->isWeighted) {
    printf("Weighted ");
  }
  if (g->isComplete) {
    printf("COMPLETE ");
  }
  if (g->isDigraph) {
    printf("Digraph\n");
    printf("Max Out-Degree = %d\n", GraphGetMaxOutDegree(g));
  } else {
    printf("Graph\n");
    printf("Max Degree = %d\n", GraphGetMaxDegree(g));
  }
  printf("Vertices = %2d | Edges = %2d\n", g->numVertices, g->numEdges);

  List* vertices = g->verticesList;
  ListMoveToHead(vertices);
  unsigned int i = 0;
  for (; i < g->numVertices; ListMoveToNext(vertices), i++) {
    struct _Vertex* v = ListGetCurrentItem(vertices);
    printf("Vertice %d OutDegree - %d\n", i, v->outDegree);
    printf("%2d ->", i);
    if (ListIsEmpty(v->edgesList)) {
      printf("\n");
    } else {
      List* edges = v->edgesList;
      unsigned int i = 0;
      ListMoveToHead(edges);
      for (; i < ListGetSize(edges); ListMoveToNext(edges), i++) {
        struct _Edge* e = ListGetCurrentItem(edges);
        if (g->isWeighted) {
          printf("   %2d(%4.2f)", e->adjVertex, e->weight);
        } else {
          printf("   %2d", e->adjVertex);
        }
      }
      printf("\n");
    }
  }
  printf("---\n");
}

void GraphListAdjacents(const Graph* g, unsigned int v) {
  printf("---\n");

  unsigned int* array = GraphGetAdjacentsTo(g, v);

  printf("Vertex %d has %d adjacent vertices -> ", v, array[0]);

  for (unsigned int i = 1; i <= array[0]; i++) {
    printf("%d ", array[i]);
  }

  printf("\n");

  free(array);

  printf("---\n");
}
