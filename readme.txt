https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter/code

Content

The dataset is a CSV, where each row is a tweet. The different columns are described below. Every conversation included has at least one request from a consumer and at least one response from a company. Which user IDs are company user IDs can be calculated using the inbound field.

tweet_id

A unique, anonymized ID for the Tweet. Referenced by response_tweet_id and in_response_to_tweet_id.

author_id

A unique, anonymized user ID. @s in the dataset have been replaced with their associated anonymized user ID.

inbound

Whether the tweet is "inbound" to a company doing customer support on Twitter. This feature is useful when re-organizing data for training conversational models.

created_at

Date and time when the tweet was sent.

text

Tweet content. Sensitive information like phone numbers and email addresses are replaced with mask values like __email__.

response_tweet_id

IDs of tweets that are responses to this tweet, comma-separated.

in_response_to_tweet_id

ID of the tweet this tweet is in response to, if any.


“标签：csv label”
technical	系统/技术故障，如崩溃、报错
payment	    扣费异常、支付失败
delivery	配送延误、丢件、送错货等
account	    账号冻结、登录失败、权限问题
service	    客服响应慢、客服态度差等
pricing	    价格争议、不一致
legal	    版权、虚假宣传、数据泄露、违法行为
other	    非风险内容、正常咨询、闲聊等
other_chitchat 普通闲聊/打招呼，如 hello、good night
other_general_question 普通问题咨询，无风险，如 what is your name?
other_language_issues 语言翻译请求或非英文内容
other_spam_or_junk 垃圾信息、诱导关注/点击
other_incomplete_or_unclear 不完整或难以理解的信息，如 ‘???’ 或 ‘idk’
other_uncategorized 无法明确分类的普通内容
