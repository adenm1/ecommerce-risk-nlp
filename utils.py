import re

# 重写清洗方法，重新清洗数据以后在手动数据标注->语义分析

def clean_text(text):
    if not isinstance(text, str):
        return ""
    # 移除 @用户名 和 长数字ID
    text = re.sub(r'@\w+|\d{5,}', '', text)
    # 移除网址
    text = re.sub(r'http\S+|www\S+', '', text)
    # 移除标点符号（如果对任务无关）
    text = re.sub(r'[^\w\s]', '', text)
    # 多余空格压缩
    text = re.sub(r'\s+', ' ', text).strip()
    return text

