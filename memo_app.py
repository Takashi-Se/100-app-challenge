def memo_app():
    print("簡易メモ帳へようこそ!")
    print("コマンド: add (メモ追加), view (閲覧), del (削除), q (終了)")
    
    memo_file = "memos.txt"
    
    # ファイルがなければ作成
    try:
        with open(memo_file, "a"):
            pass
    except:
        print(f"ファイル {memo_file} の作成に失敗しました")
        return
    
    while True:
        command = input("\nコマンドを入力してください: ").lower()
        
        if command == 'q':
            print("メモ帳を終了します。ありがとうございました!")
            break
            
        elif command == 'add':
            memo = input("メモを入力してください: ")
            try:
                with open(memo_file, "a", encoding="utf-8") as f:
                    f.write(memo + "\n")
                print("メモを追加しました")
            except:
                print("メモの追加に失敗しました")
                
        elif command == 'view':
            try:
                with open(memo_file, "r", encoding="utf-8") as f:
                    memos = f.readlines()
                
                if not memos:
                    print("メモはまだありません")
                else:
                    print("\n===== メモ一覧 =====")
                    for i, memo in enumerate(memos, 1):
                        print(f"{i}. {memo.strip()}")
            except:
                print("メモの読み込みに失敗しました")
                
        elif command == 'del':
            try:
                with open(memo_file, "r", encoding="utf-8") as f:
                    memos = f.readlines()
                
                if not memos:
                    print("削除するメモがありません")
                    continue
                    
                print("\n===== メモ一覧 =====")
                for i, memo in enumerate(memos, 1):
                    print(f"{i}. {memo.strip()}")
                
                try:
                    index = int(input("\n削除するメモの番号を入力してください: ")) - 1
                    if 0 <= index < len(memos):
                        del memos[index]
                        
                        with open(memo_file, "w", encoding="utf-8") as f:
                            f.writelines(memos)
                        print("メモを削除しました")
                    else:
                        print("無効な番号です")
                except ValueError:
                    print("数値を入力してください")
            except:
                print("メモの削除に失敗しました")
                
        else:
            print("無効なコマンドです。add, view, del, q のいずれかを入力してください")

# 関数を実行
if __name__ == "__main__":
    memo_app()