from typing import Optional

def sort_key(item: tuple[str, int]) -> int:
  return item[1] if item[0].isalpha() else 0

def get_num_words(text: Optional[str]) -> int:
  """Count the number of words in the given text."""
  if text is None:
    return 0
  return len(text.split())

def get_histogram(text: Optional[str], sort: bool = False) -> dict[str, int]:
  """Create a histogram of the word frequencies in the given text."""
  if text is None:
    return {}
  chars = list(text.lower())
  hist: dict[str, int] = {}
  for char in chars:
    if char in hist:
      hist[char] += 1
    else:
      hist[char] = 1
  if not sort:
    return hist
  else:
    sorted_hist = sorted(hist.items(), key=sort_key, reverse=True)
    return {k: v for k, v in sorted_hist if k.isalpha()}
