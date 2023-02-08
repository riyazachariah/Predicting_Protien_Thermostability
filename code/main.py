import logging
import sys

from src.manipulate_data.DataCleaner import DataCleaner

def main():
    # Set up logging
    logging.basicConfig(filename='Thermostability_Prediction.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('Starting Data Cleaning process...')

    try:
        # Initialize the DataCleaner object
        data_cleaner = DataCleaner("../Thermostability_Prediction/data/raw/train.csv", 
                                    "../Thermostability_Prediction/data/external/train_updates.csv")
        # Call the clean_data method
        train_df = data_cleaner.clean_data()

        logging.info('Data Cleaning process completed successfully.')

        # Save the cleaned data to a CSV file
        train_df.to_csv("../Thermostability_Prediction/data/interim/updated_train.csv", index=False)

        logging.info('Cleaned data written to "../Thermostability_Prediction/data/interim" successfully.')

    except Exception as e:
        # Log the error message
        logging.error(f'Data Cleaning process failed due to error: {str(e)}')
        # Exit the program with a non-zero exit code to indicate failure
        sys.exit(1)

if __name__ == '__main__':
    main()
