from pandas.errors import SettingWithCopyWarning

from milto import run

import warnings
warnings.simplefilter(action='ignore', category=SettingWithCopyWarning)


if __name__ == '__main__':
    run()
