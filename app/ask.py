"""第1回: 素のLLMに1回だけ質問するスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする

ツールも会話履歴も持たない「素の」呼び出し。
講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse

from google import genai
from google.genai import errors, types
from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"

MAX_TURNS = 3


def ask(client: genai.Client, history: list, question: str) -> tuple[str, list]:
    contents = history + [types.Content(role="user", parts=[types.Part(text=question)])]
    response = client.models.generate_content(model=MODEL, contents=contents)

    usage = response.usage_metadata
    print(f"[input_tokens] {usage.prompt_token_count}")
    print(f"[output_tokens] {usage.candidates_token_count}")

    answer = response.text or ""
    if not answer:
        return "(応答が空でした)", history  # 空の返答は履歴に入れない

    contents.append(types.Content(role="model", parts=[types.Part(text=answer)]))
    return answer, contents[-MAX_TURNS * 2 :]



def main() -> None:
    parser = argparse.ArgumentParser(description="履歴を保持してLLMに質問する")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    client = genai.Client(api_key=get_api_key())  # ループの外で1回だけ
    history: list = []  # ループの外で1回だけ

    print(f"[model] {MODEL}")
    question = args.question
    while True:
        print(f"[質問] {question}\n")
        try:
            answer, history = ask(client, history, question)
            print(answer)
        except errors.APIError as e:
            print(api_error_message(e.code, e.message))  # 履歴は更新されないので再入力できる

        # 次の質問を受け取る（空入力は無視して聞き直す）
        question = ""
        while not question:
            try:
                question = input("\n> ").strip()
            except (EOFError, KeyboardInterrupt):
                return
        if question.lower() in ("quit", "exit"):
            return


if __name__ == "__main__":
    main()
