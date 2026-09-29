import json

out = js("""
(() => {
  const c = document.querySelector('div.content');
  if (!c) return 'no content div';
  function walk(el, depth) {
    if (depth > 4) return '';
    let s = '  '.repeat(depth) + el.tagName + (el.className ? '.' + String(el.className).split(' ').join('.') : '');
    const t = (el.childNodes.length === 1 && el.firstChild.nodeType === 3) ? el.textContent.trim().slice(0, 80) : '';
    if (t) s += ' :: ' + t;
    s += '|NL|';
    for (const ch of el.children) s += walk(ch, depth + 1);
    return s;
  }
  return walk(c, 0);
})()
""")
print(out.replace('|NL|', '\n'))
