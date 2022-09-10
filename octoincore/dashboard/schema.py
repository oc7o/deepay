
import datetime
import decimal
import platform
from typing import List

import strawberry


@strawberry.type
class SystemStatus:
    system: str
    release: str
    version: str
    machine: str
    processor: str

def resolve_system_status():
    return SystemStatus(
        system=platform.system(),
        release=platform.release(),
        version=platform.version(),
        machine=platform.machine(),
        processor=platform.processor(),
    )


### QUERY
@strawberry.type
class DashboardQuery:
   system_status: SystemStatus = strawberry.field(resolver=resolve_system_status)
