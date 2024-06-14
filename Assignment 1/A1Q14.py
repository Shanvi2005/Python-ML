lines =[]
while True:
  line = input("Enter a line (or press Enter to finish): ")
  if not line:
    break
  lines.append(line)
if lines:
  print("\nHere are the lines you entered:")
  for line in lines:
    print(line)
else:
  print("no lines entered")