"""
JSON 配置文件读写器
====================
读取 config.json（用户偏好设置：主题、语言、字体大小），
通过命令行让用户修改任意一个设置，并带数据验证，最后保存回 config.json。

使用方法（在 VS Code 终端中运行）：
    python config_editor.py
    python config_editor.py my_config.json   # 指定其他配置文件路径
"""

import sys
import json
from pathlib import Path


# 默认配置（当 config.json 不存在时，用于创建初始文件）
DEFAULT_CONFIG = {
    "theme": "dark",
    "language": "zh-CN",
    "font_size": 14,
}

# 每个设置项的合法取值 / 取值范围，用于校验
VALID_THEMES = {"dark", "light"}
VALID_LANGUAGES = {"zh-CN", "en-US", "ja-JP"}
FONT_SIZE_MIN, FONT_SIZE_MAX = 8, 32


def load_config(path: Path) -> dict:
    """读取配置文件；不存在则创建一个带默认值的新文件。"""
    if not path.exists():
        print(f"⚠️  未找到 {path}，将创建一个默认配置文件。")
        save_config(path, DEFAULT_CONFIG)
        return dict(DEFAULT_CONFIG)

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ {path} 内容不是合法的 JSON：{e}")
        sys.exit(1)


def save_config(path: Path, config: dict) -> None:
    """把配置写回文件（UTF-8，中文不转码，缩进美化）。"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


def validate_theme(value: str):
    """校验主题：必须是 dark 或 light。"""
    value = value.strip().lower()
    if value not in VALID_THEMES:
        return None, f"主题必须是 {', '.join(VALID_THEMES)} 之一"
    return value, None


def validate_language(value: str):
    """校验语言代码：必须在受支持列表内。"""
    value = value.strip()
    if value not in VALID_LANGUAGES:
        return None, f"语言必须是 {', '.join(VALID_LANGUAGES)} 之一"
    return value, None


def validate_font_size(value: str):
    """校验字体大小：必须是 8-32 之间的整数。"""
    try:
        size = int(value.strip())
    except ValueError:
        return None, "字体大小必须是一个整数"

    if not (FONT_SIZE_MIN <= size <= FONT_SIZE_MAX):
        return None, f"字体大小必须在 {FONT_SIZE_MIN} 到 {FONT_SIZE_MAX} 之间"

    return size, None


# 每个设置项对应的校验函数
VALIDATORS = {
    "theme": validate_theme,
    "language": validate_language,
    "font_size": validate_font_size,
}


def print_config(config: dict) -> None:
    print("\n当前配置：")
    for key, value in config.items():
        print(f"  {key}: {value}")
    print()


def choose_key(config: dict) -> str:
    """让用户从现有设置项中选择一个要修改的键。"""
    keys = list(config.keys())
    print("请选择要修改的设置：")
    for i, key in enumerate(keys, start=1):
        print(f"  {i}. {key} (当前值: {config[key]})")

    while True:
        choice = input(f"输入编号 (1-{len(keys)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(keys):
            return keys[int(choice) - 1]
        print("❌ 无效的选择，请重新输入。")


def update_value(config: dict, key: str) -> None:
    """让用户输入新值，校验通过后更新到 config 字典。"""
    validator = VALIDATORS.get(key)

    while True:
        new_value = input(f"请输入 {key} 的新值: ")

        if validator:
            cleaned, error = validator(new_value)
            if error:
                print(f"❌ {error}，请重新输入。")
                continue
            config[key] = cleaned
        else:
            # 没有专门校验规则的字段，直接保存为字符串
            config[key] = new_value.strip()

        print(f"✅ {key} 已更新为: {config[key]}")
        break


def main():
    config_path = Path(sys.argv[1] if len(sys.argv) > 1 else "config.json")

    config = load_config(config_path)
    print_config(config)

    key = choose_key(config)
    update_value(config, key)

    save_config(config_path, config)
    print(f"\n✅ 配置已保存到: {config_path}")
    print_config(config)


if __name__ == "__main__":
    main()
