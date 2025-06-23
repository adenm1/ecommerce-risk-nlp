"""
Author: Architect Lieu
"""
import pickle
from enum import Enum
import pandas as pd

# pip install jupyterthemes
# jt -t monokai -fs 18 -nfs 18 -tfs 18 -ofs 18 -cellw 90% -T

_ORIGIN    = "../../"
ASSETS     = f"{_ORIGIN}assets/"
DATASETS   = f"{_ORIGIN}datasets/"
PLOT       = f"{_ORIGIN}plot/"

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

custom_stop_words = [
    'rt', 'https', 'co', 'my', 'i',
    'the', 'to', 'and', 'is', 'for',
    'you', 'but', 'we', 'that', 'this',
    'amazonhelp', 'applesupport',
    'hi', 'thanks', 'sorry', 'just', 've',
    'pls', 'please', 'im', 'ive', 'youre',
    'dm', 'know', 'help', 'getting', 'like',
    'amp', 'll', 'let'
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

    def __init__(self, priority=None, weight=None):
        self.priority = priority
        self.weight = weight

    @classmethod
    def get_names(cls):
        return [o.name.lower() for o in cls]

    @classmethod
    def get_name2value(cls):
        return {o.name.lower(): o.value for o in cls}

def auto_label_by_keywords(
        df,
        text_col,
        keywords,
        label_name,
        existing_label_col='label'
):
    """
    根据关键词列表自动为文本打标签
    """
    pattern = '|'.join(keywords)
    mask = df[text_col].str.contains(pattern, case=False, na=False)

    if existing_label_col in df.columns:
        mask = mask & df[existing_label_col].isna()

    df_labeled = df[mask].copy()
    df_labeled[existing_label_col] = label_name
    return df_labeled


def sample_and_clean_enum(_df, _sample_sizes: dict, _seed = 40):

    df_samples = []
    for label_name, size in _sample_sizes.items():
        df_sub = _df[_df['label'].str.lower() == label_name.lower()]
        if len(df_sub) > size:
            df_sub = df_sub.sample(n=size, random_state=_seed)
        df_samples.append(df_sub)

    df_final = pd.concat(df_samples, ignore_index=True)
    return df_final

def save_predictions(y_true, y_pred, filepath):
    with open(filepath, 'wb') as f:
        pickle.dump({'y_true': y_true, 'y_pred': y_pred}, f)
    print(f"Predictions saved to {filepath}")


def load_predictions(filepath):
    with open(filepath, 'rb') as f:
        data = pickle.load(f)
    print(f"Predictions loaded from {filepath}")
    return data['y_true'], data['y_pred']

print("Done! Loaded utils.py")
