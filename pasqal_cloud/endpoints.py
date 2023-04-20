# Copyright 2020 Pasqal Cloud Services development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sys import version_info

from dataclasses import dataclass

if version_info[:2] >= (3, 8):
    from typing import Final
else:
    from typing_extensions import Final  # type: ignore


CORE_API_URL: Final[str] = "https://apis.pasqal.cloud/core-fast"


@dataclass
class Endpoints:
    core: str = CORE_API_URL


AUTH0_DOMAIN: Final[str] = "pasqal.eu.auth0.com"
PUBLIC_CLIENT_ID: Final[str] = "PeZvo7Atx7IVv3iel59asJSb4Ig7vuSB"
AUDIENCE: Final[str] = "https://apis.pasqal.cloud/account/api/v1"
REALM: Final[str] = "pcs-users"


@dataclass
class Auth0Conf:
    domain: str = AUTH0_DOMAIN
    public_client_id: str = PUBLIC_CLIENT_ID
    audience: str = AUDIENCE
    realm: str = REALM