from pyspark.sql.functions import monotonically_increasing_id

from sparklanes import Task, conn


@Task('extract_data')
class ExtractIrisCSVData(object):
    """Load the iris data set from a CSV file"""
    def __init__(self, iris_csv_path):
        self.iris_csv_path = iris_csv_path

    def extract_data(self):
        # Read the csv
        iris_df = conn.spark.read.csv(path=self.iris_csv_path,
                                      sep=',',
                                      header=True,
                                      inferSchema=True)

        # Make it available to tasks that follow
        self.cache('iris_df', iris_df)


@Task('add_index')
class AddRowIndex(object):
    """Add a index to each row in the data set"""
    def add_index(self):
        # Add id column
        self.iris_df = self.iris_df.withColumn('id', monotonically_increasing_id())

        # Update cache
        self.cache('iris_df', self.iris_df)


@Task('normalize')
class NormalizeColumns(object):
    """Normalize all numerical columns"""
    def normalize(self):
        # Add normalized columns
        columns = self.iris_df.columns
        columns.remove('species')
        for col in columns:
            col_min = float(self.iris_df.agg({col: "min"}).collect()[0]['min(%s)' % col])
            col_max = float(self.iris_df.agg({col: "max"}).collect()[0]['max(%s)' % col])
            self.iris_df = self.iris_df.withColumn(
                col + '_norm', (self.iris_df[col] - col_min) / (col_max - col_min)
            )

        # Update Cache
        self.cache('iris_df', self.iris_df)


@Task('write_to_json')
class SaveAsJSON(object):
    """Dump the data set as JSON to disk"""
    def __init__(self, output_folder):
        self.output_folder = output_folder

    def write_to_json(self):
        self.iris_df.write.format('json').save(self.output_folder)

        # Clear cache
        self.uncache('iris_df')
