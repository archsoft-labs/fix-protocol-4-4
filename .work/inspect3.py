import json

# Test extraction on tag 40 (OrdType - has enum values) and tag 1 (Account - simple)
for tag in [40, 1]:
    goto_url(f"https://www.onixs.biz/fix-dictionary/4.4/tagNum_{tag}.html")
    wait_for_load()
    out = js("""
(() => {
  const c = document.querySelector('section.fix-dictionary .col-12');
  if (!c) return null;
  const txt = c.innerText;
  return JSON.stringify({text: txt.slice(0, 3500), htmlLen: c.innerHTML.length});
})()
""")
    d = json.loads(out)
    print(f"===== TAG {tag} =====")
    print(d['text'])
    print()
