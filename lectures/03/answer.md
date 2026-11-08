# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：今回の回答は用語集の定義と合っている

- `--trace` で見えたツール呼び出し（ツール名と引数）：
```text
--- trace ---
[tool call]   search_glossary({'query': 'LoRA'})
[tool call]   search_glossary({'query': 'QLoRA'})
[tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
[tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…
[usage] RunUsage(cost=Decimal('0.0008994'), details={'text_prompt_tokens': 1198}, input_text_tokens=1198, input_tokens=1198, output_tokens=216, requests=2, tool_calls=2)
```

- 1つの質問での LLM 呼び出し回数（`requests`）：2回

- 追加したツールと、docstring に書いた説明：
```text
make_quiz(lecture: int)を追加した．
「指定した回の用語から1つ選んで確認問題と答えを返す。「第2回の確認問題を出して」のように、復習用の問題を求められたときに使う。」
```

## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
