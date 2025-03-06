def sort(width, height, length, mass):
  
  is_bulky = (width * height * length >= 1000000) or (width >= 150 or height >= 150 or length >= 150)
  is_heavy = mass >= 20

  if is_bulky and is_heavy:
      return "REJECTED"
  elif is_bulky or is_heavy:
      return "SPECIAL"
  else:
      return "STANDARD"

# Example test cases:
def run_tests():
  # Test Case 1: Not bulky and not heavy -> STANDARD
  print(sort(100, 50, 60, 10))

  # Test Case 2: Bulky (due to one dimension >= 150) but not heavy -> SPECIAL
  print(sort(100, 100, 150, 10)) 

  # Test Case 3: Heavy (mass >= 20) but not bulky -> SPECIAL
  print(sort(50, 50, 50, 25)) 

  # Test Case 4: Both bulky and heavy -> REJECTED
  print(sort(150, 150, 150, 25))
