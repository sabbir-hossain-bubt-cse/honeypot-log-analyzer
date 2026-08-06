from collections import Counter

def analyze():
    print("Analyzing attack logs...")
    ips = []
    with open("attack_logs.txt", "r") as f:
        for line in f:
            if "IP:" in line:
                ip = line.split("IP: ")[1].split(" ")[0]
                ips.append(ip)

    counts = Counter(ips)
    for ip, count in counts.items():
        print(f"IP: {ip} | Total Attacks: {count}")

if __name__ == "__main__":
    analyze()