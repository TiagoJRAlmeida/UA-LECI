import asyncio
import getpass
import json
import os
import websockets
import random

#########################################################################
#                                                                       #
#   MEMBROS DO GRUPO:                                                   #
#       - TIAGO ALMEIDA - NMEC: 113106                                  #
#       - TIAGO COSTA - NMEC: 114629                                    #
#                                                                       #
#   AJUDAMOS COM IDEIAS O GRUPO CONSTITUIDO PELO SEGUINTES MEMBROS:     #
#       - GABRIEL BOIA - NMEC: 113167                                   #
#       - RAFAEL DIAS - NMEC: 114258                                    #
#       - GUILHERME MATOS - NMEC: 114252                                #
#                                                                       #
#########################################################################



# import logging
# import time

# Configuração básica do logger
# logging.basicConfig(
#     level=logging.DEBUG,  # Altere para DEBUG, INFO, WARNING, etc., conforme necessário
#     format="%(levelname)s - %(message)s"
# )
# logger = logging.getLogger(__name__)

# NOTAS: 
#   - Keys possiveis: "w", "a", "s", "d"
#   - Valores: nada -> 0; pedra -> 1; apple -> 2; super (tensa) -> 3; snake -> 4
#   - Mapa é 47x23 (0 -> 47) (0 -> 23)


def calculate_and_compare(possible_actions, snake_body, collision_map, traverse):
    action_space = {}

    for action in possible_actions:
        x, y = snake_body[0]
        if action == "w":
            start_position = (x, (y - 1) % 24)
        elif action == "a":
            start_position = ((x - 1) % 48, y)
        elif action == "s":
            start_position = (x, (y + 1) % 24)
        else:
            start_position = ((x + 1) % 48, y)
        
        x, y = start_position
        if not traverse and ([x, y] in snake_body or (x, y) in collision_map):
            action_space[action] = 0
        elif traverse and [x, y] in snake_body:
            action_space[action] = 0
        else:
            action_space[action] = flood_fill(start_position, snake_body, collision_map, traverse)

    # Encontra o maior valor de espaço disponível
    max_space = max(action_space.values())

    # Retorna todas as ações com o valor máximo
    best_actions = [action for action, space in action_space.items() if space == max_space]
    return best_actions


def flood_fill(start, snake_body, collision_map, traverse):
    visited = set()
    queue = [start]

    while queue:
        x, y = queue.pop(0)
        if (x, y) in visited:
            continue

        visited.add((x, y))

        # Procurar as coordenadas vizinhas ao square atual
        # Que não sejam a cobra e que não tenham sido visitados já
        # E adicionar à queue
        neighbors = get_neighbors((x, y))
        for neighbor in neighbors:
            x, y = neighbor
            if (x, y) not in queue and (x, y) not in visited and not out_of_bounds((x, y)):
                if not traverse and [x, y] not in snake_body and (x, y) not in collision_map:
                    queue.append((x, y))
                elif traverse and [x, y] not in snake_body:
                    queue.append((x, y))
            
    return len(visited)


def out_of_bounds(position):
    x, y = position
    return x < 0 or x > 47 or y < 0 or y > 23


def get_neighbors(position):
    x, y = position
    return [
        (x + 1, y), (x - 1, y), 
        (x, y + 1), (x, y - 1)
    ]


# Simula onde a cabeça da cobra estaria ao realizar uma ação, e devolve as coordenadas
# Util para verificar colisões
def move_snake_head(snake_head, action):
    x, y = snake_head
    return {
        "w": (x, (y - 1) % 24),
        "s": (x, (y + 1) % 24),
        "a": ((x - 1) % 48, y),
        "d": ((x + 1) % 48, y),
    }[action]


# Verifica se o proximo movimento leva a game over devido a colisão com pedra
def hits_rock_test(sight, snake_head, action):
    x, y = move_snake_head(snake_head, action)
    if sight[str(x)][str(y)] == 1:
        return True
    return False


# Verifica se o proximo movimento leva a game over devido a colisão com pedra
# Ainda não descobri como encortar esta função
def hits_border_test(snake_head, action):
    x, y = snake_head
    if action == "d" and x + 1 > 47:
        return True
    elif action == "a" and x - 1 < 0:
        return True
    elif action == "w" and y - 1 < 0:
        return True
    elif action == "s" and y + 1 > 23:
        return True
    return False


# Verifica se o proximo movimento leva a game over devido a colisão com snake
def hits_snake_test(sight, snake_head, action):
    x, y = move_snake_head(snake_head, action)
    if sight[str(x)][str(y)] == 4:
        return True
    return False


def will_hit_test(sight, snake_head, action, traverse):
    if traverse:
        return hits_snake_test(sight, snake_head, action) 
    
    return (hits_border_test(snake_head, action) or 
    hits_rock_test(sight, snake_head, action) or 
    hits_snake_test(sight, snake_head, action)) 


# Devolve o numero de maças na visão da cobra no momento
def find_apples(sight):
    apples = 0
    apple_tensa = 0

    for x_coord in sight:
        for y_coord in sight[x_coord]:
            if sight[x_coord][y_coord] == 2:
                apples += 1
            if sight[x_coord][y_coord] == 3:
                apple_tensa += 1
                
    return apples, apple_tensa


def go_to_apple(sight, snake_head):
    x, y = snake_head
    apple_actions = []
    for x_coord in sight:
        for y_coord in sight[x_coord]:
            if sight[x_coord][y_coord] == 2 or sight[x_coord][y_coord] == 3:
                
                potential_actions = [a for a in basic_actions if a != opposite_actions.get(last_action)]
                
                if x < int(x_coord) and y == int(y_coord) and "d" in potential_actions:
                    apple_actions.append("d")
                
                elif x > int(x_coord) and y == int(y_coord) and "a" in potential_actions:
                    apple_actions.append("a")
                
                elif x == int(x_coord) and y > int(y_coord) and "w" in potential_actions:
                    apple_actions.append("w")
                
                elif x == int(x_coord) and y < int(y_coord) and "s" in potential_actions:
                    apple_actions.append("s")

    return apple_actions if apple_actions else None


def update_action_count(action_count, action):
    action_count[action] -= 1
    if action_count[action] == 0:
        if action == "w":
            action_count["d"] = 40
        else:
            action_count["w"] = 7


def get_best_action(potential_actions, action_count):
    if "d" in potential_actions and action_count["w"] == 0:
        best_action = "d"
        update_action_count(action_count, "d")

    elif "w" in potential_actions and action_count["d"] == 0:
        best_action = "w"
        update_action_count(action_count, "w")

    else:
        best_action = random.choice(potential_actions)

    return best_action


def determine_action(state):
    global last_action
    global collision_map
    global action_count
    global counter

    snake_head = state['body'][0]
    snake_body = state['body']
    sight = state['sight']
    traverse = state['traverse']
    apple_normal, apple_tensa = find_apples(sight)
    best_action = None
    apple_actions = None
                
    if apple_normal > 0 or apple_tensa > 0:
        apple_actions = go_to_apple(sight, snake_head)

    # Lista com as ações posiveis, tirando a oposta á ultima, uma vez que isso leva sempre a game over
    potential_actions = [a for a in basic_actions if a != opposite_actions.get(last_action)]

    # Iterar pelas 3 ações restantes, e retirar aquelas que leva a um hit, isto é, game over
    valid_actions = []
    for action in potential_actions:
        if not will_hit_test(sight, snake_head, action, traverse):
            valid_actions.append(action)
    potential_actions = valid_actions
    
    if not potential_actions:
        return opposite_actions.get(last_action)
    
    elif len(potential_actions) == 1:
        counter = 12
        return potential_actions[0]
    
    potential_actions = calculate_and_compare(potential_actions, snake_body, collision_map, traverse)

    if len(potential_actions) == 1:
        counter = 12
        return potential_actions[0]

    # Iterar pelas restantes ações, que devem todas ser boas e filtrar por ordem de prioridade:
    # 1- action == apple_action
    # 2- action viewed_nodes count menor
    # Verificar se existe apple_action nas ações potenciais
    if apple_actions:
        matching_actions = [action for action in potential_actions if action in apple_actions]
        if matching_actions:
            best_action = random.choice(matching_actions)
            counter = 12
        
        else:
            if traverse: 
                best_action = get_best_action(potential_actions, action_count)
                counter = 12
            else: 
                if counter > 0 and last_action in potential_actions:
                    counter -= 1
                    return last_action
                else:
                    counter = 12
                    potential_actions = [a for a in potential_actions if a != last_action]
                    return random.choice(potential_actions)
    else:
        if traverse: 
            best_action = get_best_action(potential_actions, action_count)
            counter = 12
        else: 
            if counter > 0 and last_action in potential_actions:
                counter -= 1
                return last_action
            else:
                counter = 12
                potential_actions = [a for a in potential_actions if a != last_action]
                return random.choice(potential_actions)

    return best_action

# Valores iniciais das variaveis relacionadas a keys 
action = "d"
last_action = "d"

# Valor inicial do counter
counter = 12

# Ações possiveis
basic_actions = ["w", "s", "a", "d"]

# Ações opostas para o agente saber que não pode andar diretamente para tras
opposite_actions = {
    "w": "s",
    "s": "w",
    "a": "d", 
    "d": "a"
}

# Mapa com as coordenadas das paredes e eventualmente as paredes. Util para evitar loops.
collision_map = []

action_count = {
    "d": 40,
    "w": 0
}

async def agent_loop(server_address="localhost:8000", agent_name="student"):
    async with websockets.connect(f"ws://{server_address}/player") as websocket:

        # Receive information about static game properties
        await websocket.send(json.dumps({"cmd": "join", "name": agent_name}))

        while True:
            try:
                # receive game update, this must be called timely or your game will get out of sync with the server
                state = json.loads(await websocket.recv())

                # Variaveis globais porque vao ser alteradas dentro da funcao, mas foram inicializadas fora
                global action
                global last_action 
                global collision_map

                # Para skippar o primeiro json que recebe informação diferente (sobre o mapa e assim)
                if 'body' in state:
                    action = determine_action(state)

                    last_action = action

                    await websocket.send(json.dumps({"cmd": "key", "key": action}))
                
                elif 'map' in state:
                    game_map = state['map']
                    for x, column in enumerate(game_map):
                        for y, value in enumerate(column):
                            if value == 1:
                                collision_map.append((x, y))

            except websockets.exceptions.ConnectionClosedOK:
                print("Server has cleanly disconnected us")
                return


# DO NOT CHANGE THE LINES BELLOW
# You can change the default values using the command line, example:
# $ NAME='arrumador' python3 client.py
loop = asyncio.get_event_loop()
SERVER = os.environ.get("SERVER", "localhost")
PORT = os.environ.get("PORT", "8000")
NAME = os.environ.get("NAME", getpass.getuser())
loop.run_until_complete(agent_loop(f"{SERVER}:{PORT}", NAME))
