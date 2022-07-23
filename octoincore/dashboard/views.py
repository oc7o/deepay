from django.shortcuts import render
from django.views.generic import TemplateView
import platform
import psutil

# Create your views here.


class DashboardView(TemplateView):
    template_name: str = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        print(psutil.virtual_memory())
        data = super(DashboardView, self).get_context_data(**kwargs)
        data.update(
            {
                "system": platform.system(),
                "release": platform.release(),
                "version": platform.version(),
                "machine": platform.machine(),
                "processor": platform.processor(),
                "memory_usage": psutil.virtual_memory(),
                "cpu_usage": psutil.cpu_percent(),
                "cpu_count": psutil.cpu_count(),
                "cpu_freq": psutil.cpu_freq(),
                "cpu_stats": psutil.cpu_stats(),
                "cpu_times": psutil.cpu_times(),
                # "disk_usage": psutil.disk_usage("/").percent,
                # "net_io_counters": psutil.net_io_counters(),
                # "net_connections": psutil.net_connections(),
                # "net_if_addrs": psutil.net_if_addrs(),
                # "net_if_stats": psutil.net_if_stats(),
            }
        )
        return data
