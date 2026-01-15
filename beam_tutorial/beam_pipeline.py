
"""

SQL Analogy:
------------
- Beam = Query Engine ( parses code and builds dag )
- Runner = Execution Engine ( executes dag in given infra)
    Types : DirectRunner , DataFlowRunner and so on. 

Internals:
----------
- Lazy Execution: Builds DAG of transforms first, executes later
- SDK -> SDK Worker -> Runner (e.g., Dataflow, Spark)

class Transform(beam.DoFn):
    def process(self, element):
        msg = json.loads(element.decode())
        msg["score"] *= 2
        yield json.dumps(msg)


"""

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json


options = PipelineOptions(
    runner="DirectRunner",
    project="local-project",
    streaming=True,
)

class Transform(beam.DoFn):
    def process(self, element):
        print ( element)

with beam.Pipeline(options=options) as p:
    (
        p
        | "ReadPubSub" >> beam.io.ReadFromPubSub(
            subscription="projects/local-project/subscriptions/test-sub", with_attributes=False   )
        | "Transform" >> beam.ParDo(Transform())
        | "Print" >> beam.Map(print)
        
    )
