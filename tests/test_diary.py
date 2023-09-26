from lib.diary import Diary
import pytest

"""
Initially
Has an empty list of entries
"""
def test_initially_empty_entries():
    diary = Diary()
    assert diary.all() == []

"""
Initially 
word count is zero
"""
def test_initially_word_count_is_zero():
    diary = Diary()
    assert diary.count_words() == 0

"""
Initially 
#reading_time should raise an error
"""
def test_initially_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(4)
    assert str(e.value) == "No entries added yet"

"""
Initially
#find_best_entry_for_reading_time should raise an error
"""
def test_initially_find_best_entry_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(2, 2)
    assert str(e.value) == "No entries added yet"