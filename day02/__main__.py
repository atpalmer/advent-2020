from lib import maintools
from . import core


args = maintools.parse_args()
path = maintools.get_datapath(__file__, args.file)
func = getattr(core, f'part{args.part}')
result = func(filepath=path)
print(result)
