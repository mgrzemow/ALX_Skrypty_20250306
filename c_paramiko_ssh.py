import glob
import zipfile

import pickle
from pprint import pprint

import paramiko
import getpass
import paramiko
port = 22
host = "2.tcp.ngrok.io"
# port = 16809
user = 'sluchacz1'
# 2.tcp.ngrok.io:16809
if __name__ == '__main__':
    # passwd = getpass.getpass()
    passwd = 'sluchacz1_passwd'
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host,
                    port,
                    user,
                    passwd
                    )
        stdin, stdout, stderr = ssh.exec_command('cat /etc/passwd')

        # interaktywna praca - bardzo niewygodna, ale czasem trzeba
        # ssh.invoke_shell()

        # chciabym dostać listę userów z polecanie cat /etc/passwd
        ['user1', 'user2']
        stdin, stdout, stderr = ssh.exec_command('cat /etc/passwd')
        l_s = [linia.split(':')[0] for linia in stdout.read().decode().splitlines()]
        pprint(l_s)

        sftp = ssh.open_sftp()
        sftp.put('c13.py', 'c13.py')
        sftp.get('zdalny.txt', 'zdalny.txt')
        # nie jest rekurencyjne
        # sftp.rmdir('michal')
        # stdin, stdout, stderr = ssh.exec_command('cat /etc/passwd')

        with sftp.open('nowy1.txt', 'w') as f:
            f.write('Linia1\n'.encode())
            f.write('Linia2\n'.encode())
            f.write('Linia3\n'.encode())
            f.write('Linia4\n'.encode())

        with sftp.open('lista.pickle', 'w') as f:
            pickle.dump(l_s, f)

        with sftp.open('lista.pickle', 'r') as f:
            nowa_lista = pickle.load(f)
            print(nowa_lista)

        lista_plikow = glob.glob('*.py')

        print('poczatek')
        with sftp.open('newzip.zip', 'w') as f:
            with zipfile.ZipFile(f, 'w') as zf:
                for plik in lista_plikow:
                    zf.write(plik)
        print('koniec')

        # praca na zdalnych plikach zip jest bardzo wolna, fajny bajer, ale szybciej:
        print('poczatek')
        with zipfile.ZipFile('ala.zip', 'w') as zf:
            for plik in lista_plikow:
                zf.write(plik)
        sftp.put('ala.zip', 'ala.zip')
        print('koniec')
