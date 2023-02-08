## The original data contained issues or rather like most real world data, this data was dirty. Some rows had all features marked as NaN. In some rows, the 'tm' and 'ph' feature columns had been swapped.
## This code file takes care of both of those issues.
import logging
import numpy as np
import pandas as pd

class DataCleaner:
    def __init__(self, train_data_path, updates_data_path):
        self.train_df = pd.read_csv(train_data_path)
        self.train_updates_df = pd.read_csv(updates_data_path)
        self.seqid_2_phtm_update_map = self._create_update_map()
        self.bad_seqids = self._get_bad_seqids()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False
        self.handler = logging.FileHandler("DataCleaner.log")
        self.handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def _create_update_map(self):
        return self.train_updates_df[~pd.isna(self.train_updates_df["pH"])].groupby("seq_id")[["pH", "tm"]].first().to_dict("index")
    
    def _get_bad_seqids(self):
        return self.train_updates_df[pd.isna(self.train_updates_df["pH"])]["seq_id"].to_list()

    def _fix_tm_ph(self, row):
        update_vals = self.seqid_2_phtm_update_map.get(row["seq_id"], None)
        if update_vals is not None:
            row["tm"] = update_vals["tm"]
            row["pH"] = update_vals["pH"]
        return row

    def clean_data(self):
        try:
            self.logger.info("Data cleaning in progress...")
            self.train_df = self.train_df[~self.train_df["seq_id"].isin(self.bad_seqids)].reset_index(drop=True)
            self.train_df = self.train_df.apply(self._fix_tm_ph, axis=1).reset_index(drop=True)
            return self.train_df

        except Exception as e:
            self.logger.error(f"Error while cleaning the data: {str(e)}")
            raise e

