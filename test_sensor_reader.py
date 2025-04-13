import subprocess

def test_output():
    result = subprocess.run(["./sensor_reader"], capture_output=True, text=True)
    output = result.stdout.strip()
    assert output.startswith("Current temperature:"), "Output format is incorrect"
    print("✅ Python test passed.")
