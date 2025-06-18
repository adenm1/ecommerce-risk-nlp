https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter/code

Content

The dataset is a CSV, where each row is a tweet. The different columns are described below. Every conversation included
has at least one request from a consumer and at least one response from a company. Which user IDs are company user IDs
can be calculated using the inbound field.

tweet_id

A unique, anonymized ID for the Tweet. Referenced by response_tweet_id and in_response_to_tweet_id.

author_id

A unique, anonymized user ID. @s in the dataset have been replaced with their associated anonymized user ID.

inbound

Whether the tweet is "inbound" to a company doing customer support on Twitter. This feature is useful when re-organizing
data for training conversational models.

created_at

Date and time when the tweet was sent.

text

Tweet content. Sensitive information like phone numbers and email addresses are replaced with mask values like __email
__.

response_tweet_id

IDs of tweets that are responses to this tweet, comma-separated.

in_response_to_tweet_id

ID of the tweet this tweet is in response to, if any.

## Labeling Keywords

| 标签        | 关键词示例   ｜                                           |
|-----------|-----------------------------------------------------|
| technical | bug, issue, problem, error, app, crash, support     |
| payment   | charge, refund, billing, payment, money, card       |
| delivery  | shipping, delivery, not arrived, late, order        |
| account   | login, locked, password, access, reset              |
| service   | customer service, rude, slow response, support team |
| pricing   | price, expensive, charged, discount, cost           |
| legal     | policy, terms, scam, privacy, legal, misleading     |


## Category of Risk

| category of risk            | description                     |
|-----------------------------|---------------------------------|
| technical                   | 系统/技术故障，如崩溃、报错                  |
| payment                     | 扣费异常、支付失败                       |
| delivery                    | 配送延误、丢件、送错货等                    |
| account                     | 账号冻结、登录失败、权限问题                  |
| service                     | 客服响应慢、客服态度差等                    |
| pricing                     | 价格争议、不一致                        |
| legal                       | 版权、虚假宣传、数据泄露、违法行为               |
| other                       | 非风险内容、正常咨询、闲聊等                  |
| other_chitchat              | 普通闲聊/打招呼，如 hello、good night     |
| other_general_question      | 普通问题咨询，无风险，如 what is your name? |
| other_language_issues       | 语言翻译请求或非英文内容                    |
| other_spam_or_junk          | 垃圾信息、诱导关注/点击                    |
| other_incomplete_or_unclear | 不完整或难以理解的信息，如 ‘???’ 或 ‘idk’     |
| other_uncategorized         | 无法明确分类的普通内容                     |

## Labeling Sample

| seq | text                                                                                                                                                         | label     |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| 74  | @116062: will you create a “disaster registry” where fire victims can pick the items they need and anyone can fill them? Offer discounts?                    | pricing   |
| 75  | "@AppleSupport Freezing basically all of the time. Apps are messing up, if i turn on airplane mode and then turn it off i can’t get service without restart" | technical |
| 76  | @VirginTrains I’ve lost my tkt back to Wilmslow. I’ve got receipt and it’s on my app but your staff tell me too bad. Surely not right??                      | technical |
| 77  | @AmazonHelp I ordered a package to be delivered tomorrow but I’ve had a notification saying it’ll be a day late now                                          | delivery  |
| 78  | "@AmazonHelp prime membership says it’s suspended, updated payment method but still says it’s suspended? How do I fix it to get Prime back?"                 | payment   |