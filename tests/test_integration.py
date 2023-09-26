from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
Given I add two diary entires
I see them reflected in the list
"""
def test_adds_and_lists_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My Contents 1")
    entry_2 = DiaryEntry("My Title 2", "My Contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
Given I add two diary entires
And I call #count_words
I get the sum of all words in the contents of the diary entries
"""
def test_count_words_returns_sum_of_words_in_all_entry_contents():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My Contents")
    entry_2 = DiaryEntry("My Title 2", "One Two Three")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 5

"""
Given I add two diary entires with a #count_words of 5
#reading_time with a wpm of 2 will return 3
"""
def test_reading_time_return_time_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My Contents")
    entry_2 = DiaryEntry("My Title 2", "One Two Three")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3

"""
Given I add a diary entry
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I can read that entry
Then #find_best_entry_for_reading_time returns that entry
"""
def test_find_best_entry_returns_single_entry_that_fits_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1  

"""
Given I add a diary entry
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I cannot read that entry
Then #find_best_entry_for_reading_time returns None
"""
def test_find_best_entry_returns_none_if_single_entry_donesnt_fit_time():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three four five six seven")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None

"""
Given I add two diary entries, one long and one short
And given wpm and minutes that mean I can only read the short entry
#find_best_entry_for_reading_time returns short entry
"""
def test_find_best_entry_returns_entry_that_fits_time_and_wpm():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three")
    entry_2 = DiaryEntry("My Title 2", "one two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1

"""
Given I add two diary entries
And I call #find_best_entry_for_reading_time
With a wpm and minutes that mean I could read either entry
Then #find_best_entry_for_reading_time returns the longer entry
"""
def test_find_best_entry_returns_longest_readable_entry():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three")
    entry_2 = DiaryEntry("My Title 2", "one two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry_2