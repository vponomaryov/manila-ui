# Copyright 2017 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from manila_ui import features


PANEL_DASHBOARD = 'admin'
PANEL_GROUP = 'share'
PANEL = 'share_groups'

if features.is_share_groups_enabled():
    ADD_PANEL = 'manila_ui.dashboards.admin.share_groups.panel.ShareGroups'
else:
    REMOVE_PANEL = not features.is_share_groups_enabled()
