import sys
from stats import get_histogram, get_num_words

def get_book_text(path):
  try:
    with open(path) as f:
      file_contents = f.read()
      return file_contents
  except FileNotFoundError:
    print(f"Error: File '{path}' was not found")
  except PermissionError:
    print(f"Error Permission denied when trying to read from '{path}'")
  except UnicodeDecodeError:
    print(f"Error: Could not decode file '{path}'")
  except Exception as e:
    print(f"An unexpected error occurred while reading '{path}': {e}")

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  book_text = get_book_text(book_path)
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  
  print("----------- Word Count ----------")
  num_words = get_num_words(book_text)
  print(f"Found {num_words} total words")
  
  print("--------- Character Count -------")
  hist = get_histogram(book_text, sort=True)
  for char, count in hist.items():
    print(f"{char}: {count}")
  
  print("============= END ===============")

main()
