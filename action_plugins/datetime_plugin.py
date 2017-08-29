from ansible.plugins.action import ActionBase
from ansible.module_utils.datetime_helper import get_datetime

# Import the global display object or create a new one
try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

# must be named ActionModule or it won't be seen by Ansible
class ActionModule(ActionBase):
    display.v("Running action plugin")

    def run(self, tmp=None, task_vars=None):
        return get_datetime()
