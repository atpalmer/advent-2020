from lib import maintools
from . import main


args = maintools.parse_args()
path = maintools.get_datapath(__file__, args.file)
func = getattr(main, f'part{args.part}')
result = func(filepath=path)
print(result)
