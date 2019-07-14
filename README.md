# win_py_TalkSpeak
text speaking by python

OpenJtalkを利用したテキスト読み上げプログラム

hts_engine_API-1.10.tar.gz
open_jtalk-1.10.tar.gz
open_jtalk_dic_shift_jis-1.10.tar.gz
hts_voice_nitech_jp_atr503_m001-1.05.tar.gz
をダウンロード

VisualStudioのコマンドプロンプトで
hts_engin_API-1.10フォルダに移動し
nmake -f Makefile.mak
nmake -f Makefile.mak install

c:\hts_egine_API
が作成される

VisualStudioのコマンドプロンプトで
open_jtalk-1.11フォルダに移動し
nmake -f Makefile.mak
nmake -f Makefile.mak install

エラーが出るけどopen_jtalk.exeができれば
とりあえずOK

c:\opej_jtalk
が作成される

open_jtalk_dic_shift_jis-1.11
の名称をdicに変換し
c:\opej_jtalk\binにコピーする

nitech_jp_atr503_m001.htsvoice
を
c:\opej_jtalk\binにコピーする

合成したいテキストをvoice.txtに書き込む
c:\opej_jtalk\binにコピーする

c:\opej_jtalk\binで
open_jtalk.exe -m nitech_jp_atr503_m001.htsvoice -x dic -ow output.wav voice.txt
を実行

play.exeを
c:\opej_jtalk\binにコピーする

play output.wav
を実行

上記を組み合わせたプログラムを作成
ojtalk.py