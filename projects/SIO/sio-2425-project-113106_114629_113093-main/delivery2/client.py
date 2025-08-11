import os
import sys
import argparse
import logging
import json
import requests
from local_commands import *
from anonymous_api_commands import *
from authenticated_api_commands import *
from authorized_api_commands import *

logging.basicConfig(format='%(levelname)s\t- %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Carrega o state do ficheiro state.json se existir e devolve. (Devolve um dicionário vazio se não existir)
def load_state():
    state = {}
    state_dir = os.path.join(os.getcwd(), '.sio')
    state_file = os.path.join(state_dir, 'state.json')

    logger.debug('State folder: ' + state_dir)
    logger.debug('State file: ' + state_file)

    if os.path.exists(state_file):
        logger.debug('Loading state')
        with open(state_file,'r') as f:
            state = json.loads(f.read())

    if state is None:
        state = {}

    return state

# Guarda as environmental variables 'REP_ADDRESS' e 'REP_PUB_KEY' no state 
def parse_env(state):
    if 'REP_ADDRESS' in os.environ:
        state['REP_ADDRESS'] = os.getenv('REP_ADDRESS')
        logger.debug('Setting REP_ADDRESS from Environment to: ' + state['REP_ADDRESS'])

    if 'REP_PUB_KEY' in os.environ:
        rep_pub_key = os.getenv('REP_PUB_KEY')
        logger.debug('Loading REP_PUB_KEY fron: ' + state['REP_PUB_KEY'])
        if os.path.exists(rep_pub_key):
            with open(rep_pub_key, 'r') as f:
                state['REP_PUB_KEY'] = f.read()
                logger.debug('Loaded REP_PUB_KEY from Environment')
    return state

# Define os argumentos opcionais
def parse_args(state):
    parser = argparse.ArgumentParser()

    # Optional arguments
    parser.add_argument("-k", '--key', nargs=1, help="Path to the key file")
    parser.add_argument("-r", '--repo', nargs=1, help="Address:Port of the repository")
    parser.add_argument("-v", '--verbose', help="Increase verbosity", action="store_true")
    parser.add_argument("-c", "--command", help="Command to execute")
    parser.add_argument("-s", "--username", nargs=1, default=None, help="Select username in rep_list_docs")
    parser.add_argument("-d", "--date", nargs=2, default=None, help="Select format of and date for rep_list_docs")
    parser.add_argument('arg0', nargs='?', default=None)
    parser.add_argument('arg1', nargs='?', default=None)
    parser.add_argument('arg2', nargs='?', default=None)
    parser.add_argument('arg3', nargs='?', default=None)
    parser.add_argument('arg4', nargs='?', default=None)
    parser.add_argument('arg5', nargs='?', default=None)


    args = parser.parse_args()
    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.info('Setting log level to DEBUG')
        
    if args.key:
        if not os.path.exists(args.key[0]) or not os.path.isfile(args.key[0]):
            logger.error(f'Key file not found or invalid: {args.key[0]}')
            sys.exit(-1)

        with open(args.key[0], 'r') as f:
            state['REP_PUB_KEY'] = f.read()
            logger.info('Overriding REP_PUB_KEY from command line')

    if args.repo:
        state['REP_ADDRESS'] = args.repo[0]
        logger.info('Overriding REP_ADDRESS from command line')

    if args.command:
        logger.info("Command: " + args.command)

    parsed_args = {
        'command': args.command,
        'arg0': args.arg0,
        'arg1': args.arg1,
        'arg2': args.arg2,
        'arg3': args.arg3,
        'arg4': args.arg4,
        'arg5': args.arg5,
        'username': args.username[0] if args.username else None,
        'date_relation': args.date[0] if args.date else None,
        'date': args.date[1] if args.date else None
    }

    return state, parsed_args

# Guarda o state atual no ficheiro state.json
def save(state):
    state_dir = os.path.join(os.getcwd(), '.sio')
    state_file = os.path.join(state_dir, 'state.json')

    if not os.path.exists(state_dir):
      logger.debug('Creating state folder')
      os.mkdir(state_dir)

    with open(state_file, 'w') as f:
        f.write(json.dumps(state, indent=4))


def is_local_command(args):
    return args["command"] == "rep_subject_credentials" or \
        args["command"] == "rep_decrypt_file"


state = load_state()
state = parse_env(state)
state, args = parse_args(state)

if 'REP_ADDRESS' not in state and not is_local_command(args):
  logger.error("Must define Repository Address")
  sys.exit(-1)

if 'REP_PUB_KEY' not in state and not is_local_command(args):
  logger.error("Must set the Repository Public Key")
  sys.exit(-1)

save(state)

# <--- Local commands ---> #
if args["command"] == "rep_subject_credentials":
    if not args["arg0"] or not args["arg1"]:
        logger.error("Missing arguments for 'rep_subject_credentials'. Requires password and credentials_file.")
        sys.exit(1)
    rep_subject_credentials(args["arg0"], args["arg1"])

elif args["command"] == "rep_decrypt_file":
    if not args["arg0"] or not args["arg1"]:
        logger.error("Missing arguments for 'rep_decrypt_file'. Requires encrypted_file and metadata.")
        sys.exit(1)
    rep_decrypt_file(args["arg0"], args["arg1"])
# <--- End of local commands ---> #

# <--- Anonymous API commands ---> #
elif args["command"] == "rep_create_org":
    if not all([args["arg0"], args["arg1"], args["arg2"], args["arg3"], args["arg4"]]):
        logger.error("Missing arguments for 'rep_create_org'. Requires organization, username, name, email, and public_key_file.")
        sys.exit(1)
    rep_create_org(state, args["arg0"], args["arg1"], args["arg2"], args["arg3"], args["arg4"])

elif args["command"] == "rep_list_orgs":
    rep_list_orgs(state)

elif args["command"] == "rep_create_session":
    if not all([args["arg0"], args["arg1"], args["arg2"], args["arg3"], args["arg4"]]):
        logger.error("Missing arguments for 'rep_create_session'. Requires organization, username, password, credentials_file, and session_file.")
        sys.exit(1)
    rep_create_session(state, args["arg0"], args["arg1"], args["arg2"], args["arg3"], args["arg4"])

elif args["command"] == "rep_get_file":
    file_handle = args["arg0"]
    output_file = args["arg1"]
    if not file_handle:
        logger.error("Missing file_handle for 'rep_get_file'.")
        sys.exit(1)
    rep_get_file(state, file_handle, output_file)
# <--- End of anonymous API commands ---> #

# <--- Authenticated API commands ---> #
elif args["command"] == "rep_assume_role":
    if not all([args["arg0"], args["arg1"]]):
        logger.error("Missing arguments for 'rep_assume_role'. Requires session_file and role.")
        sys.exit(1)
    rep_assume_role(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_drop_role":
    if not all([args["arg0"], args["arg1"]]):
        logger.error("Missing arguments for 'rep_drop_role'. Requires session_file and role.")
        sys.exit(1)
    rep_drop_role(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_list_roles":
    if not args["arg0"]:
        logger.error("Missing arguments for 'rep_list_roles'. Requires session_file.")
        sys.exit(1)
    rep_list_roles(state, args["arg0"])

elif args["command"] == "rep_list_subjects":
    if not args["arg0"]:
        logger.error("Missing session_file for 'rep_list_subjects'.")
        sys.exit(1)
    rep_list_subjects(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_list_role_subjects":
    if not all(args["arg0"], args["arg1"]):
        logger.error("Missing arguments for 'rep_list_role_subjects'. Requires session_file and role.")
        sys.exit(1)
    rep_list_role_subjects(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_list_subject_roles":
    if not all([args["arg0"], args["arg1"]]):
        logger.error("Missing arguments for 'rep_list_subject_roles'. Requires session_file and username.")
        sys.exit(1)
    rep_list_subject_roles(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_list_role_permissions":
    if not all([args["arg0"], args["arg1"]]):
        logger.error("Missing arguments for 'rep_list_role_permissions'. Requires session_file and role.")
        sys.exit(1)
    rep_list_role_permissions(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_list_permission_roles":
    if not all([args["arg0"], args["arg1"]]):
        logger.error("Missing arguments for 'rep_list_permission_roles'. Requires session_file and permission.")
        sys.exit(1)
    rep_list_permission_roles(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_list_docs":
    if not args["arg0"]:
        logger.error("Missing session_file for 'rep_list_docs'.")
        sys.exit(1)
    if not any([args["username"], args["date_relation"], args["date"]]):
        rep_list_docs(state, args["arg0"])
    elif args["username"] and not all([args["date_relation"], args["date"]]):
        rep_list_docs(state, args["arg0"], args["username"])
    else:
        rep_list_docs(state, args["arg0"], args["username"], args["date_relation"], args["date"])
# <--- End of authenticated API commands ---> #

# <--- Authorized API commands ---> #
elif args["command"] == "rep_add_subject":
    if not all([args["arg0"], args["arg1"], args["arg2"], args["arg3"], args["arg4"]]):
        logger.error("Missing arguments for 'rep_add_subject'. Requires session_file, username, name, email, and credentials_file.")
        sys.exit(1)
    rep_add_subject(state, args["arg0"], args["arg1"], args["arg2"], args["arg3"], args["arg4"])

elif args["command"] == "rep_suspend_subject":
    if not args["arg0"] or not args["arg1"]:
        logger.error("Missing arguments for 'rep_suspend_subject'. Requires session_file and username.")
        sys.exit(1)
    rep_suspend_subject(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_activate_subject":
    if not all([args["arg0"], args["arg1"]]):
        logger.error("Missing arguments for 'rep_activate_subject'. Requires session_file and username.")
        sys.exit(1)
    rep_activate_subject(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_add_role":
    if not all([args["arg0"], args["arg1"]]):
        logger.error("Missing arguments for 'rep_add_role'. Requires session_file and role.")
        sys.exit(1)
    rep_add_role(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_suspend_role":
    if not args["arg0"] or not args["arg1"]:
        logger.error("Missing arguments for 'rep_suspend_role'. Requires session_file and role.")
        sys.exit(1)
    rep_suspend_role(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_reactivate_role":
    if not args["arg0"] or not args["arg1"]:
        logger.error("Missing arguments for 'rep_reactivate_role'. Requires session_file and role.")
        sys.exit(1)
    rep_reactivate_role(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_add_permission":
    if not all([args["arg0"], args["arg1"], args["arg2"]]):
        logger.error("Missing arguments for 'rep_add_permission'. Requires session_file, role and username or permission.")
        sys.exit(1)
    rep_add_permission(state, args["arg0"], args["arg1"], args["arg2"])

elif args["command"] == "rep_remove_permission":
    if not all([args["arg0"], args["arg1"], args["arg2"]]):
        logger.error("Missing arguments for 'rep_remove_permission'. Requires session_file, role and username or permission.")
        sys.exit(1)
    rep_remove_permission(state, args["arg0"], args["arg1"], args["arg2"])
    
elif args["command"] == "rep_add_doc":
    if not all([args["arg0"], args["arg1"], args["arg2"]]):
        logger.error("Missing arguments for 'rep_add_doc'. Requires session_file, document_name, and file.")
        sys.exit(1)
    rep_add_doc(state, args["arg0"], args["arg1"], args["arg2"])

elif args["command"] == "rep_get_doc_metadata":
    if not args["arg0"] or not args["arg1"]:
        logger.error("Missing arguments for 'rep_get_doc_metadata'. Requires session_file and document_name.")
        sys.exit(1)
    rep_get_doc_metadata(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_get_doc_file":
    if not args["arg0"] or not args["arg1"]:
        logger.error("Missing arguments for 'rep_get_doc_file'. Requires session_file and document_name.")
        sys.exit(1)
    rep_get_doc_file(state, args["arg0"], args["arg1"], args["arg2"])

elif args["command"] == "rep_delete_doc":
    if not all([args["arg0"], args["arg1"]]):
        logger.error("Missing arguments for 'rep_delete_doc'. Requires session_file and document_name.")
        sys.exit(1)
    rep_delete_doc(state, args["arg0"], args["arg1"])

elif args["command"] == "rep_acl_doc":
    if not all([args["arg0"], args["arg1"], args["arg2"], args["arg3"], args["arg4"]]):
        logger.error("Missing arguments for 'rep_acl_doc'. Requires session_file, document name, operation(+ or -), role and permission.")
        sys.exit(1)
    rep_acl_doc(state, args["arg0"], args["arg1"], args["arg2"], args["arg3"], args["arg4"])
# <--- End of authorized API commands ---> #

else:
    logger.error(f"Invalid command: {args['command']}")
    sys.exit(1)

