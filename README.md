# win_py_TalkSpeak
text speaking by python

OpenJtalk�𗘗p�����e�L�X�g�ǂݏグ�v���O����

hts_engine_API-1.10.tar.gz
open_jtalk-1.10.tar.gz
open_jtalk_dic_shift_jis-1.10.tar.gz
hts_voice_nitech_jp_atr503_m001-1.05.tar.gz
���_�E�����[�h

VisualStudio�̃R�}���h�v�����v�g��
hts_engin_API-1.10�t�H���_�Ɉړ���
nmake -f Makefile.mak
nmake -f Makefile.mak install

c:\hts_egine_API
���쐬�����

VisualStudio�̃R�}���h�v�����v�g��
open_jtalk-1.11�t�H���_�Ɉړ���
nmake -f Makefile.mak
nmake -f Makefile.mak install

�G���[���o�邯��open_jtalk.exe���ł����
�Ƃ肠����OK

c:\opej_jtalk
���쐬�����

open_jtalk_dic_shift_jis-1.11
�̖��̂�dic�ɕϊ���
c:\opej_jtalk\bin�ɃR�s�[����

nitech_jp_atr503_m001.htsvoice
��
c:\opej_jtalk\bin�ɃR�s�[����

�����������e�L�X�g��voice.txt�ɏ�������
c:\opej_jtalk\bin�ɃR�s�[����

c:\opej_jtalk\bin��
open_jtalk.exe -m nitech_jp_atr503_m001.htsvoice -x dic -ow output.wav voice.txt
�����s

play.exe��
c:\opej_jtalk\bin�ɃR�s�[����

play output.wav
�����s

��L��g�ݍ��킹���v���O�������쐬
ojtalk.py