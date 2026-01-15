
"""
Apache Beam Basics Tutorial

Concepts:
---------
- Pipeline: Container for the workflow
- PCollection: Distributed dataset (bounded for batch, unbounded for streaming)
- Transform: Operations applied on PCollections
    - Pipe (|) operator chains transforms


"""


# Import Apache Beam SDK
# Install via: pip install apache-beam
import apache_beam as beam

def print_it(element):
    """Prints each element in the PCollection."""
    print (f"{element }")

# Creates a pipeline object.
# Using context manager so pipeline auto-runs without explicit run()
with beam.Pipeline() as pipeline: 
    (
        pipeline
        | 'create'>> beam.Create (['hello','beam']) # Initializing PCollection with two elements
        | 'print'>> beam.Map(print_it)
    )
