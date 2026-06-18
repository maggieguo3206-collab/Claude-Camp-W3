"""
test_string_utils.py
=====================
使用 pytest 对 string_utils.py 中的三个函数进行单元测试。

运行方法（在 VS Code 终端中）：
    pip install pytest
    pytest
"""

import pytest

from string_utils import reverse_words, count_vowels, is_palindrome


# ---------------------------------------------------------------------------
# reverse_words
# ---------------------------------------------------------------------------

class TestReverseWords:

    def test_normal_case(self):
        """正常情况：多个单词按空格反转顺序"""
        assert reverse_words("hello world") == "world hello"

    def test_multiple_words_with_extra_spaces(self):
        """边界情况：单词间有多个空格，应被规整为单个空格分隔"""
        assert reverse_words("  hello   world  foo  ") == "foo world hello"

    def test_empty_string(self):
        """边界情况：空字符串应返回空字符串"""
        assert reverse_words("") == ""

    def test_single_word(self):
        """边界情况：只有一个单词时，反转后应与原单词相同"""
        assert reverse_words("hello") == "hello"

    def test_non_string_input_raises_type_error(self):
        """异常情况：非字符串输入应抛出 TypeError"""
        with pytest.raises(TypeError):
            reverse_words(12345)


# ---------------------------------------------------------------------------
# count_vowels
# ---------------------------------------------------------------------------

class TestCountVowels:

    def test_normal_case(self):
        """正常情况：混合大小写元音字母都应被统计"""
        assert count_vowels("Hello World") == 3  # e, o, o

    def test_no_vowels(self):
        """边界情况：完全没有元音字母"""
        assert count_vowels("xyz") == 0

    def test_empty_string(self):
        """边界情况：空字符串应返回 0"""
        assert count_vowels("") == 0

    def test_all_vowels_uppercase(self):
        """边界情况：全大写元音字母也应正确统计"""
        assert count_vowels("AEIOU") == 5

    def test_non_string_input_raises_type_error(self):
        """异常情况：非字符串输入应抛出 TypeError"""
        with pytest.raises(TypeError):
            count_vowels(None)


# ---------------------------------------------------------------------------
# is_palindrome
# ---------------------------------------------------------------------------

class TestIsPalindrome:

    def test_normal_case_true(self):
        """正常情况：简单回文应返回 True"""
        assert is_palindrome("racecar") is True

    def test_normal_case_false(self):
        """正常情况：非回文应返回 False"""
        assert is_palindrome("hello") is False

    def test_ignores_case_and_punctuation(self):
        """边界情况：忽略大小写、空格和标点后仍判断为回文"""
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_empty_string_is_palindrome(self):
        """边界情况：空字符串视为回文（反转后仍是空）"""
        assert is_palindrome("") is True

    def test_single_character_is_palindrome(self):
        """边界情况：单个字符必然是回文"""
        assert is_palindrome("a") is True

    def test_non_string_input_raises_type_error(self):
        """异常情况：非字符串输入应抛出 TypeError"""
        with pytest.raises(TypeError):
            is_palindrome(3.14)
