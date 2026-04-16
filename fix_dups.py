with open('index.html', encoding='utf-8') as f:
    lines = f.readlines()

# Delete lines 3017 to 3247 inclusive (0-indexed: 3016 to 3246)
# These are the orphaned duplicate block
del_start = 3016  # 0-indexed (line 3017)
del_end   = 3247  # 0-indexed exclusive (line 3247 included = index 3246, so slice to 3247)

cleaned = lines[:del_start] + lines[del_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(cleaned)

print(f'Done. Removed lines 3017-3247. New total: {len(cleaned)}')
