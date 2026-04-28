"""
Export OpenClaw chat history to readable markdown files.
Groups conversations by session type and adds proper titles.
"""
import sqlite3
import os
import sys
import re
from datetime import datetime

DB_PATH = r'C:\Users\Administrator\.qclaw\memory\lossless\lcm.db'
OUTPUT_DIR = r'C:\Users\Administrator\.qclaw\workspace\chat-export'

os.makedirs(OUTPUT_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("SELECT * FROM conversations ORDER BY updated_at DESC")
conversations = cur.fetchall()

print(f"Found {len(conversations)} conversations")

for conv in conversations:
    conv_id = conv['conversation_id']
    session_id = conv['session_id'] or ''
    created = conv['created_at'] or ''
    updated = conv['updated_at'] or ''

    # Get first user message as title hint
    cur.execute("""
        SELECT content FROM messages 
        WHERE conversation_id = ? AND role = 'user' 
        ORDER BY seq ASC LIMIT 1
    """, (conv_id,))
    first_msg_row = cur.fetchone()
    first_msg = ''
    if first_msg_row and first_msg_row['content']:
        first_msg = first_msg_row['content'][:80].replace('\n', ' ').replace('\r', '')
        # Remove JSON metadata blocks
        first_msg = re.sub(r'```json.*?```', '', first_msg, flags=re.DOTALL).strip()
        first_msg = first_msg[:60]

    # Get message count
    cur.execute("SELECT count(*) as cnt FROM messages WHERE conversation_id = ?", (conv_id,))
    msg_count = cur.fetchone()['cnt']

    # Determine session type for label
    if 'auto-memory' in session_id:
        session_type = 'auto-memory'
    elif 'workspace-summary' in session_id:
        session_type = 'workspace-summary'
    elif session_id and '-' in session_id and len(session_id) > 20:
        session_type = 'chat'
    else:
        session_type = 'other'

    # Build filename
    date_str = ''
    if updated:
        try:
            dt = datetime.fromisoformat(updated.replace('Z', '+00:00'))
            date_str = dt.strftime('%Y%m%d')
        except:
            date_str = updated[:10]
    
    if first_msg:
        safe_title = re.sub(r'[^\w\s\u4e00-\u9fff\-\._]', '', first_msg)[:50].strip()
    else:
        safe_title = f'{session_type}-{conv_id}'
    
    filename = f"{date_str}_{safe_title}_{conv_id}.md"
    # Clean filename for Windows
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    filepath = os.path.join(OUTPUT_DIR, filename)

    # Get all messages
    cur.execute("""
        SELECT message_id, seq, role, content, token_count, created_at
        FROM messages
        WHERE conversation_id = ?
        ORDER BY seq ASC
    """, (conv_id,))
    messages = cur.fetchall()

    if not messages:
        continue

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {first_msg or f'Conversation {conv_id}'}\n\n")
        f.write(f"- **Conversation ID:** {conv_id}\n")
        f.write(f"- **Session ID:** {session_id}\n")
        f.write(f"- **Type:** {session_type}\n")
        f.write(f"- **Messages:** {msg_count}\n")
        if created:
            f.write(f"- **Created:** {created}\n")
        if updated:
            f.write(f"- **Updated:** {updated}\n")
        f.write(f"\n---\n\n")

        for msg in messages:
            role = msg['role'] or 'unknown'
            content = msg['content'] or ''
            ts = msg['created_at'] or ''

            role_label = {
                'user': '👤 User',
                'assistant': '🤖 Assistant',
                'system': '⚙️ System',
                'tool': '🔧 Tool',
            }.get(role, f'📋 {role}')

            f.write(f"### {role_label}")
            if ts:
                f.write(f" — {ts}")
            f.write(f"\n\n")

            # Truncate very long messages
            if len(content) > 80000:
                f.write(f"{content[:80000]}\n\n... (truncated, {len(content)} chars total)\n\n")
            else:
                f.write(f"{content}\n\n")

            f.write("---\n\n")

    print(f"  {filename} ({msg_count} msgs)")

conn.close()

# Also create an index file
index_path = os.path.join(OUTPUT_DIR, '_index.md')
cur2 = sqlite3.connect(DB_PATH).cursor()
cur2.execute("""
    SELECT c.conversation_id, c.session_id, c.updated_at, 
           (SELECT count(*) FROM messages m WHERE m.conversation_id = c.conversation_id) as msg_count,
           (SELECT m.content FROM messages m WHERE m.conversation_id = c.conversation_id AND m.role = 'user' ORDER BY m.seq ASC LIMIT 1) as first_msg
    FROM conversations c
    ORDER BY c.updated_at DESC
""")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write("# Chat History Index\n\n")
    f.write("| # | ID | Type | Date | Messages | First Message |\n")
    f.write("|---|----|------|------|----------|---------------|\n")
    for i, row in enumerate(cur2.fetchall(), 1):
        cid, sid, updated, cnt, fmsg = row
        stype = 'chat' if sid and '-' in sid and len(sid) > 20 and 'auto-memory' not in sid and 'workspace-summary' not in sid else ('auto-memory' if 'auto-memory' in sid else 'summary')
        date = (updated or '')[:10]
        fmsg_short = (fmsg or '')[:40].replace('\n',' ').replace('|','/')
        f.write(f"| {i} | {cid} | {stype} | {date} | {cnt} | {fmsg_short} |\n")

cur2.connection.close()
print(f"\nDone! Index: {index_path}")
print(f"Files: {OUTPUT_DIR}")
