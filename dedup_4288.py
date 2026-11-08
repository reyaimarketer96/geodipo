import server_worker

data = server_worker.call_mcp_tool('wp_get_post', {'post_id': 4288})
content = data.get('content', '')
first_idx = content.find('<!-- GEODIPO RAG KNOWLEDGE BLOCK')
second_idx = content.find('<!-- GEODIPO RAG KNOWLEDGE BLOCK', first_idx + 10)

if second_idx != -1:
    cleaned = content[:second_idx].strip()
    res = server_worker.call_mcp_tool('wp_update_post', {'post_id': 4288, 'content': cleaned})
    print("Post 4288 successfully cleaned. Occurrences now:", cleaned.count('<!-- GEODIPO RAG KNOWLEDGE BLOCK'))
