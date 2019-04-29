# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApplicationGatewayBackendHealth(Model):
    """Response for ApplicationGatewayBackendHealth API service call.

    :param backend_address_pools: A list of
     ApplicationGatewayBackendHealthPool resources.
    :type backend_address_pools:
     list[~azure.mgmt.network.v2019_02_01.models.ApplicationGatewayBackendHealthPool]
    """

    _attribute_map = {
        'backend_address_pools': {'key': 'backendAddressPools', 'type': '[ApplicationGatewayBackendHealthPool]'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGatewayBackendHealth, self).__init__(**kwargs)
        self.backend_address_pools = kwargs.get('backend_address_pools', None)
