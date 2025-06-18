"""
Author: Architect Lieu
"""
from enum import Enum

import pandas as pd

ASSETS     = "../../assets/"
DATASETS   = "../../datasets/"

keywords_technical = [
    'crash',
    'issue',
    'bug',
    'error',
    'glitch',
    'broken',
    'freezing',
    'disconnect',
    'system'
]

keywords_payment = [
    'refund',
    'charge',
    'double',
    'charge',
    'overcharge',
    'billing',
    'payment failed',
    'credit card'
]

keywords_delivery = [
    'delivery',
    'shipping',
    'package',
    'not arrived',
    'late',
    'lost',
    'tracking',
    'missing'
]

keywords_account = [
    'login',
    'password',
    'reset',
    'locked',
    'can’t sign in',
    'access denied'
]

keywords_service = [
    'rude',
    'customer service',
    'support',
    'no response',
    'unhelpful',
    'agent'
]

keywords_pricing = [
    'expensive',
    'price',
    'cost',
    'overcharged',
    'discount',
    'price error'
]

keywords_legal = [
    'scam',
    'fraud',
    'policy',
    'privacy',
    'misleading',
    'illegal',
    'terms violation'
]


class RiskLabel(Enum):

    """
    Label with Priority for Classification <br>
    Label with Weight for LR
    """

    LEGAL = (1, 0.95)
    ACCOUNT = (2, 0.85)
    PAYMENT = (3, 0.8)
    TECHNICAL = (4, 0.75)
    DELIVERY = (5, 0.6)
    SERVICE = (6, 0.5)
    PRICING = (7, 0.4)
    OTHER = (99, 0)

    def __init__(self, priority, weight):
        self.priority = priority
        self.weight = weight


def auto_label_by_keywords(
        df,
        text_col,
        keywords,
        label_name,
        existing_label_col='label'
):
    """
    根据关键词列表自动为文本打标签

    参数：
    - df: 原始 DataFrame
    - text_col: 存放文本的列名
    - keywords: 关键词列表（如 ['refund', 'error']）
    - label_name: 要打上的标签名（如 'technical'）
    - existing_label_col: 默认标签列名（如 'label'）

    返回：
    - 被标注过的 DataFrame 子集（已打标签）
    """
    pattern = '|'.join(keywords)
    mask = df[text_col].str.contains(pattern, case=False, na=False)

    # 避免覆盖已有标签（可选）
    if existing_label_col in df.columns:
        mask = mask & df[existing_label_col].isna()

    df_labeled = df[mask].copy()
    df_labeled[existing_label_col] = label_name
    return df_labeled


def sample_and_clean_enum(_df, _sample_sizes: dict, _seed = 40):

    df_samples = []
    for label_name, size in _sample_sizes.items():
        label_enum = RiskLabel[label_name.upper()]
        df_sub = _df[_df['label'].str.lower() == label_name.lower()]
        if len(df_sub) > size:
            df_sub = df_sub.sample(n=size, random_state=_seed)
        df_samples.append(df_sub)

    df_final = pd.concat(df_samples, ignore_index=True)
    return df_final

