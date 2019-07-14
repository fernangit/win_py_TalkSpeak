import subprocess
import os

#カレントディレクトリの取得
path = os.getcwd()
print(path)

#合成音声を生成
cmd = path + '\\' + 'open_jtalk.exe -m voice.htsvoice -x dic -ow output.wav voice.txt'
print(cmd)
subprocess.call(cmd, shell = True)

#合成音声を再生
cmd = path + '\\' + 'play output.wav'
subprocess.call(cmd, shell = True)

