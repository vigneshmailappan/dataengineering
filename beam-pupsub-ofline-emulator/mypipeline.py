
import os

os.environ["PUBSUB_EMULATOR_HOST"] = "localhost:8085"
#os.environ["STORAGE_EMULATOR_HOST"] = "http://localhost:4443"
os.environ["GOOGLE_CLOUD_PROJECT"] = "local-project"

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json

class Transform(beam.DoFn):
    def process(self, element):
        msg = json.loads(element.decode())
        msg["score"] *= 2
        yield json.dumps(msg)

options = PipelineOptions(
    runner="DirectRunner",
    project="local-project",
    streaming=True,
)

with beam.Pipeline(options=options) as p:
    (
        p
        | "ReadPubSub" >> beam.io.ReadFromPubSub(
            subscription="projects/local-project/subscriptions/test-sub", with_attributes=False   )
        | "Transform" >> beam.ParDo(Transform())
        | "printMyMsg" >> beam.Map(print)
        
      # """| "WriteGCS" >> beam.io.WriteToText(
      #     "results/output",
      #     file_name_suffix=".json",
      #     num_shards=1,
      #     shard_name_template="-SS-of-NN",
      #     header=None,
      #     append_trailing_newlines=True,
      #     # 👇 This is the important part
      #     triggering_frequency=10  # write every 10 seconds

      # )"""
    )
