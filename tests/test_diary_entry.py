from lib.diary_entry import DiaryEntry
"""
When I initialise with a title and contents
I can get that title and contents back
"""
def test_constructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry("My Title", "My Contents")
    assert diary_entry.title == "My Title"
    assert diary_entry.contents == "My Contents"

"""
When I initialise with a five-word contents
#count_words returns 5
"""
def test_count_words_returns_word_count_of_contents():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    assert diary_entry.count_words() == 5

"""
When I initialise with a five-word contents
#reading_time with a wpm of 2 should return 3
"""
def test_reading_time():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    assert diary_entry.reading_time(2) == 3

"""
When I initiallise with a five-word contents
At first #reading_chunk returns the first chunk readable in the time
"""
def test_readable_chunk_returns_first_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    assert diary_entry.reading_chunk(2, 1) == "one two"

"""
When I initiallise with a five-word contents
On the second call #reading_chunk returns the second chunk readable in the time
"""
def test_readable_chunk_returns_second_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "three four"

"""
When I initiallise with a five-word contents
On the third call #reading_chunk returns the third chunk readable in the time
"""
def test_readable_chunk_returns_third_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "five"

"""
When I initiallise with a five-word contents
On the fourth call #reading_chunk should start again from the beginning
"""
def test_readable_chunk_returns_beginning_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "one two"

"""
When I initiallise with a six-word contents
On the fourth call #reading_chunk should start again from the beginning
"""
def test_readable_chunk_fourth_chuck_with_exact_chunks():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "one two"
