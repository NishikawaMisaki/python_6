import sys
args = sys.argv

'''
    打ち込んだ英文のn番目の単語を表示するプログラム
'''
##########################     英文　＆　index番号の入力       ############################

string = args[1]        #英文を格納
number = int(args[2])   #n番目

##########################     処理の開始　　　##############################################

try:
    '''
    英文をスペースで分割し(split())、単語のリストstring_listを作成します。
    ex) if  string == "hello world"
            string_list = ('hello','world')
    '''
    string_list = string.split()   

    ''' number番目の単語を出力します'''
    print(string_list[number-1])

except:
    '''
    エラー処理
    英文の単語数を超えてしまう数が引数(number)として与えられたとき、エラー分を生成します
    ex error) 
    string_list = ('hello','world')  ※単語数 2 
        number = 3 ※3番目の単語を表示しようとしている時
    '''    
    print(str(number)+"はindex番号として正しくありません")



