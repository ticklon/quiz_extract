import re
import csv

# テキストファイルから問題と選択肢を抽出する関数
def extract_questions_and_options(text):
    questions = []
    
    # 正規表現で問題を抽出 (例: 【問 1】, 【問 2】 など)
    question_pattern = re.compile(r"【問\s?\d+】\s?(.*?)\n", re.DOTALL)
    option_pattern = re.compile(r"\n(\d)\s+(.*?)\n")
    
    # 問題と選択肢のブロックを取得
    question_blocks = question_pattern.split(text)[1:]  # 質問番号から始まるブロックを抽出

    for i in range(0, len(question_blocks), 2):
        question_text = question_blocks[i].strip()  # 質問文
        options_block = question_blocks[i+1]  # 選択肢ブロック
        
        # 選択肢を抽出
        options = option_pattern.findall(options_block)
        options = [option[1].strip() for option in options]  # 各選択肢をリストに
        
        if len(options) == 4:  # 選択肢が4つの場合にのみ保存
            questions.append({"question": question_text, "options": options})
    
    return questions

# 抽出したデータをCSVに書き込む関数
def write_to_csv(questions, filename="quiz.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Option 1", "Option 2", "Option 3", "Option 4"])  # ヘッダー行
        for question in questions:
            writer.writerow([question["question"]] + question["options"])

# メイン処理部分
def main():
    # テキストファイルを読み込み
    with open('quiz.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # 問題と選択肢を抽出
    questions = extract_questions_and_options(text)

    # CSVに書き込む
    write_to_csv(questions)

    print("問題と選択肢がCSVファイルに保存されました。")

# 実行
if __name__ == "__main__":
    main()

