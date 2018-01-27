# Put this file to ~/.zipline/
# this file serves as reading external files as bundles
# see more discussion at https://github.com/quantopian/zipline/issues/2060
# and https://github.com/quantopian/zipline/blob/master/docs/source/bundles.rst

import pandas as pd

from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities

start_session = pd.Timestamp('2017-1-1', tz='utc')
end_session = pd.Timestamp('2018-1-1', tz='utc')

register(
    'alt_coin_bundle',
    csvdir_equities(
        ['minute'],
        '/path/to/your/csvs',
    ),
    calendar_name='CALENDERNAME', # US equities
    start_session=start_session,
    end_session=end_session
)