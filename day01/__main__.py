from lib import maintools
from . import main


args = maintools.parse_args()
func = getattr(main, f'part{args.part}')
func(filepath=maintools.get_datapath(__file__, args.file))
