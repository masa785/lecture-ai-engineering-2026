# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary_search_glossary
- STEP 2 の [tool call]：glossary_search_glossary({'query': '3レベル'})
- STEP 3 の [tool call]：fetch_fetch({'url': 'https://modelcontextprotocol.io/'})
- STEP 4 の [tool call]：
aws_aws___search_documentation({'search_phrase': 'Amazon S3 バージョニング 概要', 'topics': ['general']})
aws_aws___search_documentation({'search_phrase': 'Using versioning Amazon S3', 'topics': ['general']})
- 気づき・疑問：自分で作成したサーバーより公開サーバーや外部サーバーの方が処理時間が長い

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：基礎
- やったこと： MCPサーバーにツールを追加して、エージェント側を変えなくても、一覧にツールが増え、質問で呼ばれることを確かめた
- 結果：呼び出された　→　glossary_get_lecture_summary({'lecture': 2})
- 気づき・疑問：ツールの設定によって、質問に対してどのツールを使用するのが最適なのかを正しく判別することができている
