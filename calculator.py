def calculator():
    print("簡易計算機へようこそ!")
    print("終了するには 'q' を入力してください")
    
    while True:
        # ユーザー入力の受け取り
        user_input = input("計算式を入力してください (例: 2 + 3): ")
        
        # 終了条件
        if user_input.lower() == 'q':
            print("計算機を終了します。ありがとうございました!")
            break
        
        # 入力を分解して計算
        try:
            # スペースで分割
            parts = user_input.split()
            
            if len(parts) != 3:
                print("無効な入力です。'数値 演算子 数値' の形式で入力してください")
                continue
            
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            # 演算の実行
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("エラー: ゼロで割ることはできません")
                    continue
                result = num1 / num2
            else:
                print(f"サポートされていない演算子です: {operator}")
                continue
            
            # 結果の表示
            print(f"計算結果: {result}")
        
        except ValueError:
            print("数値を正しく入力してください")
        except Exception as e:
            print(f"エラーが発生しました: {e}")

# 関数を実行
if __name__ == "__main__":
    calculator()