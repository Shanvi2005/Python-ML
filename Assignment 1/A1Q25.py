source_file = "abc.txt"
destination_file = "def.txt"

try:
  with open(source_file, 'r') as source:
    with open(destination_file, 'w') as destination:
      contents = source.read()
      destination.write(contents)
  print(f"Successfully copied contents from {source_file} to {destination_file}.")
except FileNotFoundError:
  print(f"Error: One or both files not found. Please check file paths.")
