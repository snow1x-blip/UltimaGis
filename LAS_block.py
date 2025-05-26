import logging
import lasio
import pandas as pd

logging.basicConfig(level=logging.INFO)


class LasToAsciiConverter:
    def convert(self, file_name):
        las = lasio.read(file_name)
        data = las.data
        df = pd.DataFrame(data)
        ascii_file_name = file_name.replace('.las', '.ascii')
        df.to_csv(ascii_file_name, sep='\t', index=False)
