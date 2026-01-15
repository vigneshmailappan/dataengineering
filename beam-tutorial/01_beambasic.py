# Importing beam python sdk ( pip install apache_beam)
import apache_beam as beam

i= 0

def print_it(element):
    print (f"{element }")

with beam.Pipeline() as pipeline: # Creates a pipeline object. Its a context manager which runs pipeline for us. Otherwise we need run() function to execute.
    (
        pipeline
        | 'create'>> beam.Create (['hello','beam']) # Initializing PCollection
        | 'print'>> beam.Map(print_it)
    )
    
    
    # Mental model - Beam Basic
    # Arch : SDK ( coding ) -> SDK Worker ( converting to language agnostic ) -> Runner ( execution engine; such as dataflow, spark)
    # Pipeline - PCollection - Transform
    
    # Pipeline - Container for the workflow
    # PCollection - Distributed Dataset ( bounded for batch and unbounded for stream)
    # Transform - Changes applied on PCollection 
    #           - Pipe(|) operator chains the transforms 
    
    # SQL ANALOGY
    # -----------
    
    # Beam - Query Engine 
    # Runner - Execution Engine
    
    
    # Internals 
    # Lazy Execution - builds dag of transforms first and executes. Means doesn't run until the pipeline finalized
    