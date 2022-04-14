"""
加密解密基础
"""

#base64
import base64

#DES
"""
加密key必须8字节
使用ecb
3des加密长度168位
"""
#pip install pycrypto

from Cryptodome.Cipher import DES
import binascii

"""
AES
key长度必须为8字节,被加密的数据必须是8的倍数
"""
#AES
from Cryptodome.Cipher import AES

#MD5
from hashlib import md5


def md5hs(str1):

    #MD5
    s=str1
    new_md5 = md5()
    new_md5.update(s.encode(encoding='utf-8'))
    return new_md5.hexdigest()


def main():
    #base64 enc
    s='haha123'
    bs = base64.b64encode(s.encode('utf-8'))
    print(bs.decode('utf-8'))
    #dec
    s1 = 'aGFoYTEyMw=='
    bs1 = str(base64.b64decode(s1),"utf-8")
    print(bs1)
    print('---------')

    #DES enc
    key = b'abcdefgh'
    des = DES.new(key,DES.MODE_ECB)
    text = "ahah123 nihao"
    text = text+(8-(len(text)%8))*'='
    encrypt_text = des.encrypt(text.encode())
    encrypt_res = binascii.b2a_hex(encrypt_text)
    print(encrypt_res)

    #dec
    encrypt_res = b'2360463f28a46ed65c8a05ab571f5927'
    encrypt_text = binascii.a2b_hex(encrypt_res)
    decrypt_res = des.decrypt(encrypt_text)
    print(decrypt_res)
    print('--------------')

    #AES enc
    key=b'abcdefghabcdefgh'
    text = 'haha123 nihao'
    text = text + (16 - (len(text) % 16)) * '='
    aes = AES.new(key,AES.MODE_ECB)
    encrypt_text = aes.encrypt(text.encode())
    encrypt_res = binascii.b2a_hex(encrypt_text)
    print(encrypt_res)

    #dec
    encrypt_res = b'6c9694e90c571fbe1f2da94a45f5b39e'
    encrypt_text = binascii.a2b_hex(encrypt_res)
    decrypt_res = aes.decrypt(encrypt_text)
    print(decrypt_res)
    print('--------------')

    a=md5hs('admin')
    print(a)


    pass



if __name__ == '__main__':
    main()