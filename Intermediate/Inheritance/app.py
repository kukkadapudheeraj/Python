from chef import Chef
from chinese_chef import Chinese_Chef


Chinese_Chef().make_fried_rice()

Chinese_Chef().make_sald() # even if chinese chef doesnt have this object defined it inherits properties from Chef class

Chinese_Chef().make_spec_dish() # this same object is present in both classes but it gives priority to its own class than inherited class

Chef().make_spec_dish()

