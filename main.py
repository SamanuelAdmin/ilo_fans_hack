import time
from paramiko.client import SSHClient
from typing import Optional
import sys

from config_reader import *
from ilo_manager import *

TIMEOUT = 10


def process(client: SSHClient, command: str) -> str:
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.read().decode()


def create_client() -> SSHClient:
    client = SSHClient()
    client.load_system_host_keys()
    client.connect(
            ILO_IP,
            username=ILO_LOGIN,
            password=ILO_PASSWORD,
            port=int(ILO_SSH_PORT),
            timeout=TIMEOUT,
            disabled_algorithms=dict(pubkeys=["rsa-sha2-512", "rsa-sha2-256"])
        )
    return client

def main():
    # restart ILO
    rest_cl = create_rest_client(
            ILO_WEB_PANEL, ILO_LOGIN, ILO_PASSWORD
    )
    print("REST client has been created.")
    
    actions_status, aval_actions = actions(rest_cl)
    if actions_status not in [200, 201]: 
        print("Cannot find any available actions, status: ", actions_status)

    print("Available actions: ", aval_actions)
    print("Restarting ILO...   ", end="")
    print(restart_ilo(rest_cl))

    print("Waiting 60 seconds for ILO restarting...")
    time.sleep(60);
    cl = create_client()

    print("Setting min PID values...")
    for pid in JSON_DATA["pid_to_fix"]:
        print(f"Setting min={JSON_DATA['min_pid']} {pid}... ", process(cl, f"fan pid {pid} lo {JSON_DATA['min_pid']}"))

    for ds in JSON_DATA["disabled_sensors"]:
        print(f"Disabling sensor {ds}... ", process(cl, f"fan t {ds} off"))

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: sys.exit(0)
