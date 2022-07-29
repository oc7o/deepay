
import strawberry
import datetime
import decimal
from typing import List
import platform
import psutil

@strawberry.type
class SystemStatus:
    system: str
    release: str
    version: str
    machine: str
    processor: str
    memory_total: decimal.Decimal
    memory_available: decimal.Decimal
    cpu_usage: decimal.Decimal
    cpu_count: int
    cpu_freq: str

def resolve_system_status():
    return SystemStatus(
        system=platform.system(),
        release=platform.release(),
        version=platform.version(),
        machine=platform.machine(),
        processor=platform.processor(),
        memory_total=psutil.virtual_memory().total,
        memory_available=psutil.virtual_memory().available,
        cpu_usage=psutil.cpu_percent(),
        cpu_count=psutil.cpu_count(),
        cpu_freq=psutil.cpu_freq()
    )


### QUERY
@strawberry.type
class DashboardQuery:
   system_status: SystemStatus = strawberry.field(resolver=resolve_system_status)
