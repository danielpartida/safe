import requests


def get_counter_origin(address: str = '0xBbA4C8eB57DF16c4CfAbe4e9A3Ab697A3e0C65D8') -> int:
    """
    Calls the endpoint https://safe-transaction-mainnet.safe.global/api/v1/safes/<address>/multisig-transactions/, if no
    address is giving as a parameter, the default address 0xBbA4C8eB57DF16c4CfAbe4e9A3Ab697A3e0C65D8 is called.
    Checks if the response status is 200, if not then breaks the request.
    Fetches the data from the response and loops through all the result elements
    Counts the number of "WalletConnect transactions" made with the Safe
    :param address: str wallet address, default value is 0xBbA4C8eB57DF16c4CfAbe4e9A3Ab697A3e0C65D8
    :return: counter: int value of WalletConnect transactions made with the Safe
    """
    url = 'https://safe-transaction-mainnet.safe.global/api/v1/safes/{0}/multisig-transactions/'.format(address)
    response = requests.get(url=url)

    if response.status_code != 200:
        raise ValueError("Error while fetching the data, status code received {0}".format(response.status_code))

    data = response.json()
    results = data['results']

    counter = 0
    for element in results:
        # Check if dictionary is empty
        if bool(eval(element['origin'])):
            # Check if name origin is WalletConnect
            if eval(element['origin'])['name'] == "WalletConnect":
                counter += 1

    return counter


if __name__ == "__main__":

    result = get_counter_origin()
    print('Number of "WalletConnect transactions" = {0}'.format(result))

