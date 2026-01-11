import os
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
        | "Print" >> beam.Map(print)
        
    )
