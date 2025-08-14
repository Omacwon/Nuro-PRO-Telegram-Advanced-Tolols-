#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nuro TG Tools – Test Version (Limited)
✅ Connection test only
🔒 Limited features – Buy the full version
"""

import os
import sys
import asyncio
import logging
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError
from colorama import Fore, Style, init as colorama_init
import pyfiglet

# Initialize color output
colorama_init(autoreset=True)

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("NuroTest")

# Contact info
CONTACT = {
    "price": "19€",
    "telegram": "@EasyStrmx",
    "email": "powtv@proton.me"
}

def banner():
    print(Fore.MAGENTA + pyfiglet.figlet_format("Nuro TG Test", font="small"))
    print(Fore.CYAN + "🔒 Demo Version – Limited Features" + Style.RESET_ALL)
    print(Style.BRIGHT + "-" * 60 + Style.RESET_ALL)

def show_upgrade_prompt():
    print("\n" + Fore.RED + "❌ This feature is not available in the free version." + Style.RESET_ALL)
    print(Fore.YELLOW + f"💎 Unlock ALL features for only {CONTACT['price']}!" + Style.RESET_ALL)
    print(Fore.WHITE + "📲 Contact me to buy the full version:")
    print(Fore.CYAN + f"   • Telegram : {CONTACT['telegram']}")
    print(Fore.CYAN + f"   • Email    : {CONTACT['email']}")
    print(Fore.GREEN + "✅ Full features include:")
    print(Fore.WHITE + "   • Unlimited member & message scraping")
    print(Fore.WHITE + "   • Multi-account & proxy support (SOCKS5/HTTP)")
    print(Fore.WHITE + "   • Automated messaging with custom delays")
    print(Fore.WHITE + "   • CSV/JSON exports, Cron jobs, filters, and more")
    print(Fore.MAGENTA + "🎁 Priority support + free updates!\n" + Style.RESET_ALL)

async def test_connection():
    print(Fore.YELLOW + "\n🔧 Telegram Connection Test" + Style.RESET_ALL)
    print(Fore.WHITE + "💡 This version only allows connection testing.")
    print(Fore.WHITE + "➡️  To unlock full features, buy the PRO version.\n")

    api_id = input(Fore.CYAN + "🔹 API ID : ").strip()
    api_hash = input(Fore.CYAN + "🔹 API HASH : ").strip()
    phone = input(Fore.CYAN + "🔹 Phone number (e.g. +33612345678) : ").strip()

    if not all([api_id, api_hash, phone]):
        print(Fore.RED + "❌ All fields are required." + Style.RESET_ALL)
        return

    client = TelegramClient("test_session", api_id, api_hash)

    try:
        await client.connect()
        if not await client.is_user_authorized():
            print(Fore.YELLOW + f"📨 SMS code sent to {phone}..." + Style.RESET_ALL)
            await client.send_code_request(phone)
            code = input(Fore.CYAN + "🔐 Code received : ").strip()
            try:
                await client.sign_in(phone, code)
            except SessionPasswordNeededError:
                pwd = input(Fore.CYAN + "🔑 2FA Password : ").strip()
                await client.sign_in(password=pwd)
            except PhoneCodeInvalidError:
                print(Fore.RED + "❌ Invalid code." + Style.RESET_ALL)
                return

        print(Fore.GREEN + "✅ Connection successful!" + Style.RESET_ALL)
        print(Fore.YELLOW + "🔍 Fetching first 5 members of the group..." + Style.RESET_ALL)

        # List groups
        dialogs = await client.get_dialogs()
        groups = [d for d in dialogs if getattr(d.entity, "megagroup", False)]
        if not groups:
            print(Fore.RED + "❌ No groups found." + Style.RESET_ALL)
            await client.disconnect()
            show_upgrade_prompt()
            return

        print(Fore.WHITE + "📋 Available groups:")
        for i, g in enumerate(groups):
            print(f"  {i}. {g.title}")

        idx = int(input(Fore.CYAN + "👉 Choose a group (number): "))
        if not (0 <= idx < len(groups)):
            print(Fore.RED + "❌ Invalid choice." + Style.RESET_ALL)
            await client.disconnect()
            return

        group = groups[idx]
        members = await client.get_participants(group, limit=5)  # Only 5 members

        print(Fore.GREEN + f"\n👥 First 5 members of '{group.title}':" + Style.RESET_ALL)
        for m in members:
            username = f"@{m.username}" if m.username else "N/A"
            print(f"  • {m.first_name or 'Unknown'} {m.last_name or ''} ({username})")

        print(Fore.YELLOW + "\n💡 That's all you can do here." + Style.RESET_ALL)
        show_upgrade_prompt()

    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}" + Style.RESET_ALL)
    finally:
        await client.disconnect()

def main():
    banner()
    log.info("Welcome to the Nuro TG Tools test version.")
    log.info("Connect to test if the tool works on your system.")
    log.info("Full version available upon request.\n")

    try:
        asyncio.run(test_connection())
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n👋 Thanks for trying the free version!" + Style.RESET_ALL)
        print(Fore.CYAN + f"📩 Contact @EasyStrmx to buy the full version for {CONTACT['price']}.")
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
