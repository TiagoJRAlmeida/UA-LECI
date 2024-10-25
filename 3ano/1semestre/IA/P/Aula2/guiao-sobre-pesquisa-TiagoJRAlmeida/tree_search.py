# Module: tree_search
# 
# This module provides a set o classes for automated
# problem solving through tree search:
#    SearchDomain  - problem domains
#    SearchProblem - concrete problems to be solved
#    SearchNode    - search tree nodes
#    SearchTree    - search tree with the necessary methods for searhing
#
#  (c) Luis Seabra Lopes
#  Introducao a Inteligencia Artificial, 2012-2020,
#  Inteligência Artificial, 2014-2023

from abc import ABC, abstractmethod

# Dominios de pesquisa
# Permitem calcular
# as accoes possiveis em cada estado, etc
class SearchDomain(ABC):

    # construtor
    @abstractmethod
    def __init__(self):
        pass

    # lista de accoes possiveis num estado
    @abstractmethod
    def actions(self, state):
        pass

    # resultado de uma accao num estado, ou seja, o estado seguinte
    @abstractmethod
    def result(self, state, action):
        pass

    # custo de uma accao num estado
    @abstractmethod
    def cost(self, state, action):
        pass

    # custo estimado de chegar de um estado a outro
    @abstractmethod
    def heuristic(self, state, goal):
        pass

    # test if the given "goal" is satisfied in "state"
    @abstractmethod
    def satisfies(self, state, goal):
        pass


# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
    def __init__(self, domain, initial, goal):
        self.domain = domain
        self.initial = initial
        self.goal = goal
    def goal_test(self, state):
        return self.domain.satisfies(state,self.goal)

# Nos de uma arvore de pesquisa
class SearchNode:
    def __init__(self, state, parent, depth, cost, heuristic, action): 
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.heuristic = heuristic
        self.action = action
        
    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + ")"
    
    def __repr__(self):
        return str(self)
    
    def in_parent(self, newstate):
        if(self.parent == None):
            return False
        if(self.parent.state == newstate):
            return True
        return self.parent.in_parent(newstate)

# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='breadth'): 
        self.problem = problem
        initial_heuristic = problem.domain.heuristic(problem.initial, problem.goal)
        root = SearchNode(problem.initial, None, 0, 0, initial_heuristic, None)
        self.open_nodes = [root]
        self.strategy = strategy
        self.solution = None
        self.non_terminals = 0
        self.terminals = 0
        self.highest_cost_nodes = [root]
        self.average_depth = 0
        self.plan = []

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self,node):
        if node.parent == None:
            return [node.state]
        path = self.get_path(node.parent)
        path += [node.state]
        return(path)
    
    @property
    def length(self):
        if self.solution:
            return self.solution.depth
        return 0

    @property
    def avg_branching(self):
        return (self.terminals + self.non_terminals - 1) / self.non_terminals
    
    @property 
    def cost(self):
        if self.solution is not None:
            return self.solution.cost
        return None

    # procurar a solucao
    def search(self, limit=None):
        
        total_depth = 0
        # Enquanto houver folhas (nós finais da arvore)
        while self.open_nodes != []:
            
            # Grava na variavel node o nó atual e ao mesmo tempo apaga-o da lista para passar 
            # para o proximo (se houver) na proxima iteração
            node = self.open_nodes.pop(0)
            newdepth = node.depth + 1
            
            # Se o nó atual no loop for o nó que se está á procura, dá return ao caminho guardado até então
            if self.problem.goal_test(node.state):
                auxnode = node
                while auxnode.parent is not None:
                    self.plan.insert(0, auxnode.action)
                    auxnode = auxnode.parent
                self.terminals = len(self.open_nodes) + 1
                self.average_depth = total_depth/(self.non_terminals + self.terminals)
                self.solution = node
                return self.get_path(node)
            
            self.non_terminals += 1
            
            if limit is not None and node.depth >= limit:
                continue
                        
            # Itera por todas as cidades adjacentes, cria novos nós com os valores da cidade original e as 
            # cidades adjacentes encontradas e por fim adiciona esses novos nós á nova lista "lnewnodes"
            lnewnodes = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)
                if not node.in_parent(newstate):
                    cost = node.cost + self.problem.domain.cost(node.state, (node.state, newstate))
                    new_heuristic = self.problem.domain.heuristic(newstate, self.problem.goal)
                    newnode = SearchNode(newstate,node, newdepth, cost, new_heuristic, a)
                    if(newnode.cost > self.highest_cost_nodes[0].cost):
                            self.highest_cost_nodes = [newnode]
                    elif(newnode.cost == self.highest_cost_nodes[0].cost):
                            self.highest_cost_nodes.append(newnode)
                    lnewnodes.append(newnode)
                    total_depth += newnode.depth
                
            # Adiciona novos nós ao open_nodes
            self.add_to_open(lnewnodes)
        return None

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.open_nodes[:0] = lnewnodes
        elif self.strategy == 'uniform':
            self.open_nodes.extend(lnewnodes)
            self.open_nodes.sort(key = lambda node: node.cost)
        elif self.strategy == 'greedy':
            self.open_nodes.extend(lnewnodes)
            self.open_nodes.sort(key = lambda node: node.heuristic)
        elif self.strategy == 'a*':
            self.open_nodes.extend(lnewnodes)
            self.open_nodes.sort(key = lambda node: node.heuristic + node.cost)