# 🛠️ MAAS Extension — WOL (Wake-on‑LAN) Scripts

Extend **Ubuntu MAAS** (Metal as a Service) with handy Wake-on‑LAN and power-control scripts.

---

## 🎯 What Is This Repository?

This project provides a set of **Python scripts** designed to extend Canonical’s MAAS by adding Wake-on‑LAN (WOL) and enhanced shutdown functionality. Ideal for physical data-center environments where remotely powering on/off bare-metal servers is needed.

Inspired by this guide: [MAAS WOL/Wake Manual Shutdown Extension](https://cloudpenguin.blogspot.com/2015/07/maas-wakeonlanetherwake-manual-shutdown.html) from Cloud Penguin.

---

## ⚙️ Features

- 🔌 **Wake-on‑LAN** support for remote booting of servers  
- 📴 Enhanced shutdown using Wake-on‑LAN, plus improved cleanup  
- 🔁 Seamlessly plugs into existing MAAS workflows  
- 🧩 MIT-licensed, easy to modify and adapt  

---

## 🚀 Quickstart

```bash
# Clone this extension into your MAAS script folder:
cd /root
git clone https://github.com/Taximu/maas_extension.git

# Follow any additional setup instructions in the scripts

