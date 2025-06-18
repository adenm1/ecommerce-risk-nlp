from enum import Enum


class RiskLabel(Enum):

    """Label & Weight"""

    TECHNICAL = 1
    PAYMENT = 2
    DELIVERY = 3
    ACCOUNT = 4
    SERVICE = 5
    PRICING = 6
    LEGAL = 7
    OTHER = 0


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
    'support', 'no response',
    'unhelpful',
    'agent'
]

keywords_pricing = [
    'expensive', 'price', 'cost', 'overcharged', 'discount', 'price error'
]

keywords_legal = [
    'scam', 'fraud', 'policy', 'privacy', 'misleading', 'illegal', 'terms violation'
]