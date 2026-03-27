from redfish import RedfishClient


def create_rest_client(host: str, login: str, password: str) -> RedfishClient:
    client = RedfishClient(base_url=host, username=login, password=password)
    client.login(auth="session")
    return client


def restart_ilo(rest_client: RedfishClient) -> bool:
    response = rest_client.post(
            "/redfish/v1/Managers/1/Actions/Manager.Reset/",
            {
                # 'Action': '#Manager.Reset',
            }
        )

    return response.status in [200, 201]
    

def actions(rest_client: RedfishClient) -> (int, dict):
    response = rest_client.get(
            "/redfish/v1/Managers/1"
        )
    return response.status, response.dict
