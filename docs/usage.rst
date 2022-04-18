=====
Usage
=====

To use Microsoft Service Wrapper in a project you first need to instantiate an application instance from `msal <https://github.com/AzureAD/microsoft-authentication-library-for-python>`_ lib like the example below

.. code-block:: python

    import msal

    credentials = {
        "authority": "<YOUR_AUTHORITY_URL>",
        "client_id": "<YOUR_CLIENT_ID>",
        "client_credential": "<YOUR_CLIENT_CREDENTIAL>"
    }

    app = msal.ConfidentialClientApplication(**credentials)


Now you just need to pick the service you want and start to use the API

.. code-block:: python

    # MS GRAPH example
    from microsoft_service_wrapper.ms_graph.client import MsGraphClient

    graph_client = MsGraphClient(app)

    # Add user to security group
    graph_client.add_users_to_group(<group_name>, [<user_principal_names>])

    # Remove user from security group
    graph_client.remove_users_from_group(<group_name>, [<user_principal_names>])

