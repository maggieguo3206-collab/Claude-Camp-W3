"""
string_utils.py
================
一个小型字符串工具库，包含：
    - reverse_words(s)   反转单词顺序
    - count_vowels(s)    统计元音字母数量
    - is_palindrome(s)   判断是否为回文
"""

VOWELS = set("aeiouAEIOU")


def reverse_words(s: str) -> str:
    """
    反转字符串中单词的顺序（按空白分割），单词内部字符顺序不变。

    示例：
        "hello world" -> "world hello"

    参数：
        s: 输入字符串

    返回：
        单词顺序反转后的字符串

    异常：
        TypeError: 当 s 不是字符串时抛出
    """
    if not isinstance(s, str):
        raise TypeError("输入必须是字符串")

    words = s.split()
    return " ".join(reversed(words))


def count_vowels(s: str) -> int:
    """
    统计字符串中元音字母（a, e, i, o, u，不区分大小写）的数量。

    参数：
        s: 输入字符串

    返回：
        元音字母的个数

    异常：
        TypeError: 当 s 不是字符串时抛出
    """
    if not isinstance(s, str):
        raise TypeError("输入必须是字符串")

    return sum(1 for ch in s if ch in VOWELS)


def is_palindrome(s: str) -> bool:
    """
    判断字符串是否为回文。
    忽略大小写、空格以及非字母数字字符（例如标点符号），
    因此 "A man, a plan, a canal: Panama" 会被判断为回文。

    参数：
        s: 输入字符串

    返回：
        是回文则返回 True，否则返回 False

    异常：
        TypeError: 当 s 不是字符串时抛出
    """
    if not isinstance(s, str):
        raise TypeError("输入必须是字符串")

    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]
