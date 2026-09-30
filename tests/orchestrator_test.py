from weather_pipeline.pipeline import run_pipeline
import pandas as pd

def test_run_pipeline():
    result = run_pipeline()

    assert result is not None

result = test_run_pipeline()

print(result)
print("Hello")