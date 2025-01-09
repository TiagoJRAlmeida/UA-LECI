

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = rel
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=None):
        self.declarations = [] if ldecl==None else ldecl
    
    def __str__(self):
        idk = ""
        for a in self.declarations:
            idk += f"{str(a)}\n"
        return idk
    
    def insert(self,decl):
        self.declarations.append(decl)
    
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result
    
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))


    # Ex1
    def list_associations(self):
        return set([d.relation.name for d in self.declarations if isinstance(d.relation, Association)])


    # Ex2
    def list_objects(self):
        return set([d.relation.entity1 for d in self.declarations if isinstance(d.relation, Member)])


    # Ex3
    def list_users(self):
        return set([d.user for d in self.declarations])


    # Ex4
    def list_types(self):
        return set([d.relation.entity2 for d in self.declarations if isinstance(d.relation, Subtype) or isinstance(d.relation, Member)])
    

    # Ex5
    def list_local_associations(self, entity):
        return set([d.relation.name for d in self.query_local(e1=entity) if isinstance(d.relation, Association)])
    

    # Ex6
    def list_relations_by_user(self, user):
        return set([d.relation.name for d in self.query_local(user=user) if isinstance(d.relation, Relation)])
    

    # Ex7
    def associations_by_user(self, user):
        return len(set([d.relation.name  for d in self.query_local(user=user) if isinstance(d.relation, Association)]))
    

    # Ex8
    def list_local_associations_by_entity(self, entity):
        return set([(d.relation.name, d.user) for d in self.query_local(e1=entity) if isinstance(d.relation, Association)])
    

    # Ex9
    def predecessor(self, e1, e2):
        if e1 == e2:
            return True
        for d in self.declarations:
            if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and d.relation.entity2 == e1:
                if self.predecessor(d.relation.entity1, e2):
                    return True
        return False
    

    # Ex10
    def predecessor_path(self, e1, e2):
        if e1 == e2:
            return [e1]
        for d in self.declarations:
            if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and d.relation.entity2 == e1:
                if self.predecessor(d.relation.entity1, e2):
                    return [e1] + self.predecessor_path(d.relation.entity1, e2)
        return None
        
    
    # Ex11 (a)
    def query (self, entity, assoc = None):
        # Itera por todas as declarações, e adiciona aquelas em que a entity1 é igual á entity especificada, que a associação é igual á associação introduzida
        # e que não seja nem um membro nem um subtipo, ou seja, só pode ser association.
        # Resumindo: Busca todas as declarações de associações locais. 
        local_lst = []
        for d in self.declarations:
            if d.relation.entity1 == entity and (assoc == None or d.relation.name == assoc) and not isinstance(d.relation, Member) and not isinstance(d.relation, Subtype):
                local_lst.append(d)

        # Itera por todas as declarações, e adiciona aquelas em que a entity1 é igual á entity especificada e em que a relação é de membro ou subtipo
        # Resumindo: vai procurar todas as heranças da entidade para depois procurar associações herdadas
        lstent = []
        for d in self.declarations:
            if d.relation.entity1 == entity and (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)):
                lstent.append(d.relation.entity2)


        # Se não tiver encontrado herdança, devolve apenas as associações locais, caso contrário, itera pelas heranças á procura de mais associações.
        if lstent == []:
            return local_lst
        else:
            cumul = []
            for l in lstent:
                cumul = cumul + self.query(l , assoc)
            return local_lst + cumul


    # Ex11 (b)
    def query2(self, entity, rel = None):   
        
        # Trata de encontrar as relações de member e subtype locais  
        local_lst = []
        for d in self.declarations:
            if d.relation.entity1 == entity and (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)):
                local_lst.append(d)
        
        # Trata de encontrar as relações de associação locais e herdadas
        inhert_list = self.query(entity,rel)
    
        return inhert_list + local_lst
    

    # Ex12
    def query_cancel(self, e1, assoc_name = None):
        pai = ""
        for d in self.declarations:
            if isinstance(d.relation, Member) and d.relation.entity1 == e1:
                pai = d.relation.entity2
                break
        
        return_list = []
        for d in self.declarations:
            if isinstance(d.relation, Association) and d.relation.entity1 == pai and d.relation.name == assoc_name:
                return_list.append(d)
        
        return return_list
    
    
    # Ex13
    def query_down(self, type, assoc_name):
        stunf = []
        for d in self.declarations:
            if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and type == d.relation.entity2: # if is predecessor
                for dec in self.declarations: # append own associations (with assoc_name), then go to next child
                    if isinstance(dec.relation, Association) and dec.relation.name == assoc_name and dec.relation.entity1 == d.relation.entity1:
                        stunf.append(dec)
                return stunf + self.query_down(d.relation.entity1, assoc_name)
        return stunf
    

    # ex 14
    def query_induce(self, e1: str, assoc_name: str):
        lst = [dec.relation.entity2 for dec in self.query_down(e1, assoc_name)]
        # get most common
        return max(set(lst), key=lst.count)