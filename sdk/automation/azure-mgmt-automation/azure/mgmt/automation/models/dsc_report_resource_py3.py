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


class DscReportResource(Model):
    """Definition of the DSC Report Resource.

    :param resource_id: Gets or sets the ID of the resource.
    :type resource_id: str
    :param source_info: Gets or sets the source info of the resource.
    :type source_info: str
    :param depends_on: Gets or sets the Resource Navigation values for
     resources the resource depends on.
    :type depends_on:
     list[~azure.mgmt.automation.models.DscReportResourceNavigation]
    :param module_name: Gets or sets the module name of the resource.
    :type module_name: str
    :param module_version: Gets or sets the module version of the resource.
    :type module_version: str
    :param resource_name: Gets or sets the name of the resource.
    :type resource_name: str
    :param error: Gets or sets the error of the resource.
    :type error: str
    :param status: Gets or sets the status of the resource.
    :type status: str
    :param duration_in_seconds: Gets or sets the duration in seconds for the
     resource.
    :type duration_in_seconds: float
    :param start_date: Gets or sets the start date of the resource.
    :type start_date: datetime
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'source_info': {'key': 'sourceInfo', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[DscReportResourceNavigation]'},
        'module_name': {'key': 'moduleName', 'type': 'str'},
        'module_version': {'key': 'moduleVersion', 'type': 'str'},
        'resource_name': {'key': 'resourceName', 'type': 'str'},
        'error': {'key': 'error', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'duration_in_seconds': {'key': 'durationInSeconds', 'type': 'float'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
    }

    def __init__(self, *, resource_id: str=None, source_info: str=None, depends_on=None, module_name: str=None, module_version: str=None, resource_name: str=None, error: str=None, status: str=None, duration_in_seconds: float=None, start_date=None, **kwargs) -> None:
        super(DscReportResource, self).__init__(**kwargs)
        self.resource_id = resource_id
        self.source_info = source_info
        self.depends_on = depends_on
        self.module_name = module_name
        self.module_version = module_version
        self.resource_name = resource_name
        self.error = error
        self.status = status
        self.duration_in_seconds = duration_in_seconds
        self.start_date = start_date
