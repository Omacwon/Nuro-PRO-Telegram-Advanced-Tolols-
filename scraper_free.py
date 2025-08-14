import asyncio
from telethon import TelegramClient

print("🔹 Free Version - Limited to 5 members")
print("For the full version, contact: powtv@proton.me or https://t.me/EasyStrmx\n")

async def main():
    api_id = int(input("Enter your API_ID: "))
    api_hash = input("Enter your API_HASH: ")
    phone_number = input("Enter your phone number (+1... or +33...): ")
    group_name = input("Enter the group name or @username: ")

    client = TelegramClient(phone_number, api_id, api_hash)
    await client.start()

    print(f"📌 Fetching the first 5 members of: {group_name}\n")
    members = []
    async for user in client.iter_participants(group_name, limit=5):
        members.append(f"{user.first_name or ''} {user.last_name or ''} (@{user.username or 'N/A'})")
    
    print("\n".join(members))
    print("\n✅ Limited functionality. Contact us for the full version!")

    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
