#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from knowledge_example.crew import DatasetFinder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        "query": "CTV ad performance datasets with user-level metrics",        
        }


    result = DatasetFinder().crew().kickoff(inputs=inputs)
   
